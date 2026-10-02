# AI-Powered E-commerce

A modular e-commerce platform built as a containerized application stack, with a FastAPI product service, PostgreSQL, Redis, MinIO, and a frontend.

## Overview

The current implementation focuses on a product microservice exposing a REST API and communicating with PostgreSQL and Redis.

The product service provides:

- Product and category endpoints
- Pagination and filtering
- PostgreSQL connection pooling
- Redis caching
- Health checks
- Structured application logging

## Architecture

```
Frontend
   |
Products API (FastAPI)
   |          |
PostgreSQL   Redis
   |
MinIO for object storage
```

The services can be run together with Docker Compose on a shared application network.

## Technologies

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- Redis
- MinIO
- Docker
- Docker Compose
- React frontend

## Running locally

```bash
docker compose up -d
```

The product API is exposed on port 8000 and provides a health endpoint at `/health`.

## DevOps aspects

The repository is also useful as a containerization and deployment lab, covering:

- Multi-service Docker Compose architecture
- Service-to-service networking
- Persistent volumes
- Environment-based configuration
- Health checks
- Backend containerization

The repository is a personal full-stack/DevOps project and is still under development.
