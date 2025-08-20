import React from 'react';
import { ShoppingCart, Star } from 'lucide-react';

const ProductCard = ({ product }) => {
  const handleAddToCart = () => {
    console.log('Adding to cart:', product.name);
    // TODO: Implement cart functionality
  };

  return (
    <div className="product-card">
      <div className="product-image">
        <img 
          src={product.image_url || '/api/placeholder/300/200'} 
          alt={product.name}
          onError={(e) => {
            e.target.src = '/api/placeholder/300/200';
          }}
        />
        <div className="product-badge">New</div>
      </div>
      
      <div className="product-info">
        <div className="product-category">
          {product.category || 'Gaming'}
        </div>
        
        <h3 className="product-name">{product.name}</h3>
        
        <div className="product-rating">
          {[1, 2, 3, 4, 5].map(star => (
            <Star 
              key={star} 
              size={16} 
              className={star <= 4 ? 'star-filled' : 'star-empty'}
            />
          ))}
          <span className="rating-text">(4.0)</span>
        </div>
        
        <div className="product-price">
          <span className="current-price">${product.price}</span>
          <span className="original-price">${(product.price * 1.2).toFixed(2)}</span>
        </div>
        
        <button 
          className="add-to-cart-btn"
          onClick={handleAddToCart}
        >
          <ShoppingCart size={18} />
          Add to Cart
        </button>
      </div>
    </div>
  );
};

export default ProductCard;
