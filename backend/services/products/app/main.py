import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncpg
import redis.asyncio as redis
import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Modele Pydantic
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int
    sku: Optional[str] = None
    brand: Optional[str] = None
    stock_quantity: int = 0

class Product(ProductBase):
    id: int
    image_url: Optional[str] = None
    is_active: bool = True
    created_at: str

class Category(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    slug: str

# FastAPI app
app = FastAPI(
    title="AI E-commerce Products API",
    description="Products microservice for AI-powered e-commerce platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ecom:ecom_pass123@db:5432/ecomdb")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

# Connection pools (będą inicjalizowane przy starcie)
db_pool = None
redis_pool = None

@app.on_event("startup")
async def startup():
    global db_pool, redis_pool
    try:
        # PostgreSQL connection pool
        db_pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=10)
        logger.info("PostgreSQL connection pool created")
        
        # Redis connection
        redis_pool = redis.from_url(REDIS_URL, decode_responses=True)
        await redis_pool.ping()
        logger.info("Redis connection established")
        
    except Exception as e:
        logger.error(f"Failed to connect to databases: {e}")

@app.on_event("shutdown")
async def shutdown():
    global db_pool, redis_pool
    if db_pool:
        await db_pool.close()
    if redis_pool:
        await redis_pool.close()

# Dependency do uzyskania connection
async def get_db():
    async with db_pool.acquire() as connection:
        yield connection

# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        # Test database
        async with db_pool.acquire() as conn:
            await conn.fetchval("SELECT 1")
        
        # Test Redis
        await redis_pool.ping()
        
        return {"status": "healthy", "services": {"database": "ok", "redis": "ok"}}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AI E-commerce Products API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Products endpoints
@app.get("/api/v1/products", response_model=List[Product])
async def get_products(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(50, ge=1, le=100, description="Number of products to return"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    search: Optional[str] = Query(None, description="Search in product name and description"),
    db: asyncpg.Connection = Depends(get_db)
):
    """Get list of products with optional filtering and pagination"""
    
    # Cache key
    cache_key = f"products:skip={skip}:limit={limit}:cat={category_id}:search={search}"
    
    # Try cache first
    try:
        cached = await redis_pool.get(cache_key)
        if cached:
            import json
            logger.info("Returning cached products")
            return json.loads(cached)
    except Exception as e:
        logger.warning(f"Cache error: {e}")
    
    # Build query
    query = """
        SELECT p.*, c.name as category_name 
        FROM products p 
        LEFT JOIN categories c ON p.category_id = c.id 
        WHERE p.is_active = true
    """
    params = []
    param_count = 0
    
    if category_id:
        param_count += 1
        query += f" AND p.category_id = ${param_count}"
        params.append(category_id)
    
    if search:
        param_count += 1
        query += f" AND (p.name ILIKE ${param_count} OR p.description ILIKE ${param_count})"
        search_term = f"%{search}%"
        params.extend([search_term, search_term])
        param_count += 1
    
    query += f" ORDER BY p.created_at DESC LIMIT ${param_count + 1} OFFSET ${param_count + 2}"
    params.extend([limit, skip])
    
    try:
        rows = await db.fetch(query, *params)
        products = []
        for row in rows:
            product = Product(
                id=row['id'],
                name=row['name'],
                description=row['description'],
                price=float(row['price']),
                category_id=row['category_id'],
                sku=row['sku'],
                brand=row['brand'],
                stock_quantity=row['stock_quantity'],
                image_url=row['image_url'],
                is_active=row['is_active'],
                created_at=row['created_at'].isoformat()
            )
            products.append(product)
        
        # Cache results for 5 minutes
        try:
            import json
            await redis_pool.setex(
                cache_key, 
                300, 
                json.dumps([p.dict() for p in products], default=str)
            )
        except Exception as e:
            logger.warning(f"Cache set error: {e}")
        
        return products
        
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/api/v1/products/{product_id}", response_model=Product)
async def get_product(product_id: int, db: asyncpg.Connection = Depends(get_db)):
    """Get single product by ID"""
    
    # Cache key
    cache_key = f"product:{product_id}"
    
    # Try cache first
    try:
        cached = await redis_pool.get(cache_key)
        if cached:
            import json
            logger.info(f"Returning cached product {product_id}")
            return json.loads(cached)
    except Exception as e:
        logger.warning(f"Cache error: {e}")
    
    query = """
        SELECT * FROM products 
        WHERE id = $1 AND is_active = true
    """
    
    try:
        row = await db.fetchrow(query, product_id)
        if not row:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product = Product(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            price=float(row['price']),
            category_id=row['category_id'],
            sku=row['sku'],
            brand=row['brand'],
            stock_quantity=row['stock_quantity'],
            image_url=row['image_url'],
            is_active=row['is_active'],
            created_at=row['created_at'].isoformat()
        )
        
        # Cache for 10 minutes
        try:
            import json
            await redis_pool.setex(cache_key, 600, json.dumps(product.dict(), default=str))
        except Exception as e:
            logger.warning(f"Cache set error: {e}")
        
        return product
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/api/v1/categories", response_model=List[Category])
async def get_categories(db: asyncpg.Connection = Depends(get_db)):
    """Get all product categories"""
    
    # Try cache first
    try:
        cached = await redis_pool.get("categories:all")
        if cached:
            import json
            logger.info("Returning cached categories")
            return json.loads(cached)
    except Exception as e:
        logger.warning(f"Cache error: {e}")
    
    query = "SELECT * FROM categories ORDER BY name"
    
    try:
        rows = await db.fetch(query)
        categories = []
        for row in rows:
            category = Category(
                id=row['id'],
                name=row['name'],
                description=row['description'],
                slug=row['slug']
            )
            categories.append(category)
        
        # Cache for 30 minutes
        try:
            import json
            await redis_pool.setex(
                "categories:all", 
                1800, 
                json.dumps([c.dict() for c in categories])
            )
        except Exception as e:
            logger.warning(f"Cache set error: {e}")
        
        return categories
        
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
