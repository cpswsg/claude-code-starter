# FastAPI Project

## Project Overview

This is a modern Python API built with FastAPI, focusing on high performance, automatic API documentation, and type safety with Python type hints.

**Project Type**: API/Backend Service
**Primary Language**: Python 3.9+
**Framework/Stack**: FastAPI + Pydantic + SQLAlchemy + PostgreSQL

## Development Guidelines

### Code Style & Conventions

- Use **snake_case** for functions, variables, and file names
- Use **PascalCase** for classes and Pydantic models
- Use **UPPER_CASE** for constants and environment variables
- Follow **PEP 8** style guidelines with 88-character line length
- Use **type hints** for all function parameters and return values
- Prefer **async/await** for I/O operations
- Use **f-strings** for string formatting

### API Architecture

- Follow **RESTful** API design principles
- Use **dependency injection** for database sessions and auth
- Implement **proper HTTP status codes** and error responses
- Use **Pydantic models** for request/response validation
- Group related endpoints into **routers**
- Implement **comprehensive error handling** with custom exceptions
- Use **background tasks** for non-blocking operations

### File Structure

```
app/
├── main.py              # FastAPI application entry point
├── core/                # Core functionality
│   ├── config.py        # Settings and configuration
│   ├── database.py      # Database connection and session
│   ├── security.py      # Authentication and authorization
│   └── exceptions.py    # Custom exception handlers
├── models/              # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   └── base.py
├── schemas/             # Pydantic models (request/response)
│   ├── __init__.py
│   ├── user.py
│   └── common.py
├── api/                 # API endpoints
│   ├── __init__.py
│   ├── deps.py          # Dependencies
│   └── v1/              # API version 1
│       ├── __init__.py
│       ├── endpoints/
│       │   ├── users.py
│       │   └── auth.py
│       └── api.py       # Router aggregation
├── crud/                # CRUD operations
│   ├── __init__.py
│   ├── base.py
│   └── user.py
├── services/            # Business logic
│   ├── __init__.py
│   └── user_service.py
└── utils/               # Utility functions
    ├── __init__.py
    └── helpers.py
```

## Testing Strategy

- **Testing Framework**: pytest + pytest-asyncio + httpx
- **Coverage Requirements**: Maintain 85%+ coverage for API endpoints
- **Test Types**: Unit tests, integration tests, API endpoint tests
- Use **test fixtures** for database setup and teardown
- Test with **test database** separate from development
- Mock external services with **respx** or similar libraries

### Testing Patterns

```python
# API endpoint testing example
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/users/",
            json={"email": "test@example.com", "password": "testpass123"}
        )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

## Dependencies & Package Management

- Use **Poetry** for dependency management (pyproject.toml)
- Pin dependency versions for production stability
- Separate development and production dependencies
- Use **virtual environments** for isolation
- Keep dependencies up to date with security patches

### Key Dependencies

- **FastAPI**: Modern, fast web framework for APIs
- **Pydantic**: Data validation using Python type annotations
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **Uvicorn**: ASGI server implementation
- **python-jose**: JWT token handling
- **passlib**: Password hashing
- **psycopg2-binary**: PostgreSQL adapter

## Database Management

- **Database**: PostgreSQL (primary), SQLite (development/testing)
- **ORM**: SQLAlchemy with async support
- **Migrations**: Alembic for schema versioning
- Use **foreign keys** and **constraints** properly
- Implement **database connection pooling**
- Use **transactions** for data consistency

### Database Patterns

```python
# SQLAlchemy model example
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

## Authentication & Security

- Use **JWT tokens** for stateless authentication
- Implement **OAuth2** with password flow
- Hash passwords with **bcrypt**
- Use **CORS** middleware for cross-origin requests
- Implement **rate limiting** to prevent abuse
- Validate all inputs with **Pydantic** models
- Use **HTTPS** in production

## Performance Requirements

- **Response Time**: API endpoints < 200ms for simple queries
- **Throughput**: Handle 1000+ requests per second
- **Database**: Optimize queries with proper indexing
- Use **async/await** for I/O bound operations
- Implement **connection pooling** for database
- Add **caching** with Redis for frequently accessed data
- Monitor with **application performance monitoring**

## API Documentation

- **Automatic Docs**: FastAPI generates OpenAPI/Swagger docs
- **Docs URL**: `/docs` for Swagger UI, `/redoc` for ReDoc
- Use **comprehensive docstrings** for all endpoints
- Include **examples** in Pydantic models
- Document **error responses** and status codes

## Development Commands

### Environment Setup
```bash
poetry install           # Install dependencies
poetry shell            # Activate virtual environment
```

### Database Operations
```bash
alembic upgrade head    # Apply migrations
alembic revision --autogenerate -m "message"  # Create migration
```

### Development Server
```bash
uvicorn app.main:app --reload              # Development server
uvicorn app.main:app --host 0.0.0.0 --port 8000  # Expose to network
```

### Testing & Quality
```bash
pytest                  # Run test suite
pytest --cov=app       # Run tests with coverage
pytest -v              # Verbose output
black app/             # Format code
flake8 app/            # Lint code
mypy app/              # Type checking
```

## Environment Configuration

Use environment variables for all configuration:

```python
# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/dbname"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"
```

## Security Considerations

- **Input Validation**: Use Pydantic for all request data
- **SQL Injection**: Use SQLAlchemy ORM, avoid raw SQL
- **Authentication**: Implement proper JWT handling
- **Rate Limiting**: Prevent abuse with slowapi or similar
- **CORS**: Configure allowed origins properly
- **Environment Variables**: Never commit secrets to repository
- **Error Handling**: Don't expose internal errors to clients

## Deployment & Environment

- **Development**: Local development with SQLite/PostgreSQL
- **Production**: Docker containers with PostgreSQL and Redis
- **Environment Variables**: Use .env files for configuration
- **Health Checks**: Implement `/health` endpoint for monitoring
- **Logging**: Use structured logging with loguru or standard logging

## Common Commands

- `poetry run uvicorn app.main:app --reload` - Start development server
- `poetry run pytest` - Run test suite
- `poetry run black .` - Format code
- `poetry run flake8` - Lint code
- `poetry run mypy app` - Type checking
- `alembic upgrade head` - Apply database migrations
- `poetry add package-name` - Add new dependency

## Important Notes

- This project uses async FastAPI - use `async def` for endpoint handlers
- Database operations should be async using `asyncpg` driver
- All models must have proper type hints for automatic API docs
- Use dependency injection for database sessions and authentication
- Performance is critical - optimize database queries and use caching
- API versioning is implemented - add new versions without breaking existing

## External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)