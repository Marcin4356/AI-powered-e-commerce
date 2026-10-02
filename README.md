# AI-Powered E-commerce

A containerized e-commerce application with a React frontend and a Python FastAPI product service backed by PostgreSQL, Redis and MinIO.

## Architecture

```text
React frontend
      |
      v
FastAPI Products API
      |
  +---+----------------+
  |                    |
PostgreSQL            Redis
                         |
                    application cache

MinIO
  |
object storage
```

The repository also contains ML-related application modules, including recommendation and dynamic-pricing components.

## Backend

The products service is implemented with FastAPI and provides:

- product endpoints
- category endpoints
- pagination
- category filtering
- text search
- PostgreSQL connection pooling
- Redis caching
- health checks
- application logging
- CORS configuration

The service exposes an HTTP health endpoint at `/health`.

## Frontend

The frontend is implemented with React and includes product listing, product cards, navigation, footer and client-side routing. Axios is used for communication with the backend API.

## Infrastructure

Docker Compose defines services for:

- products API
- PostgreSQL 16
- Redis 7
- MinIO
- React frontend

The services share a Docker network and PostgreSQL/MinIO use persistent volumes.

## Technologies

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- Redis
- MinIO
- React
- Axios
- Docker
- Docker Compose

## Run locally

```bash
docker compose up -d
```

The products API is exposed on port 8000 and the frontend on port 3000.

This is a personal full-stack and DevOps learning project; some application functionality is still under development.
