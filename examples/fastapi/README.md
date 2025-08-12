# FastAPI Configuration

This example provides a complete Claude Code configuration for FastAPI Python applications.

## What's Included

### 🐍 Python Development Tools
- **Python Package Management**: pip, poetry, pipenv support
- **Testing Framework**: pytest with async support
- **Database Tools**: Alembic migrations, SQLAlchemy ORM
- **Development Server**: Uvicorn with hot reloading

### 🔒 Enhanced Security
- **Database Migration Protection**: Prevents accidental migration edits
- **Environment Protection**: Blocks .env file modifications
- **Virtual Environment Safety**: Prevents venv deletion
- **Dependency Monitoring**: Alerts for security vulnerabilities

### 📊 Python-Specific Hooks
- **Dependency Tracking**: Monitors pip and poetry installations
- **Security Alerts**: Suggests pip-audit after dependency changes
- **Poetry Integration**: Tracks outdated packages

## Quick Setup

```bash
# Copy configuration to your FastAPI project
cp -r examples/fastapi/.claude ./
cp examples/fastapi/CLAUDE.md ./

# Customize for your specific needs
$EDITOR .claude/settings.json
$EDITOR CLAUDE.md

# Verify setup
claude detect-stack python
```

## Key Features

### FastAPI Best Practices
- **Async/Await Patterns**: Full async support configuration
- **Type Safety**: Comprehensive type hinting guidelines
- **API Documentation**: Automatic OpenAPI/Swagger integration
- **Database Patterns**: SQLAlchemy with Alembic migrations

### Development Workflow
- **Hot Reloading**: Uvicorn development server
- **Testing**: pytest with async and API testing
- **Code Quality**: Black, flake8, mypy integration
- **Database**: PostgreSQL with migration support

### Claude Code Integration
- **Smart Agents**: Performance Engineer, Error Detective
- **Security**: Protects sensitive files and dangerous operations
- **Monitoring**: Comprehensive development analytics

## Recommended Agents

For FastAPI projects, these agents are particularly useful:

```bash
# API development and optimization
claude performance-engineer

# Database and backend debugging
claude error-detective

# Development workflow optimization
claude dx-optimizer

# API documentation generation
claude generate-docs api
```

## Environment Variants

### Development Setup
```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Or with Poetry
poetry install
poetry shell
```

### Docker Development
```bash
# Add Docker support to permissions
"allow": [
  "Bash(docker:*)",
  "Bash(docker-compose:*)"
]
```

### Production Considerations
```json
// Restrict permissions for production
"deny": [
  "Bash(pip:install)",
  "Bash(poetry:add)",
  "Write(**/app/**)"
]
```

## Testing Configuration

The configuration supports comprehensive testing:

```bash
# Run tests with coverage
claude "Run pytest with coverage and generate report"

# API endpoint testing
claude "Test all API endpoints with different scenarios"

# Database testing
claude "Run database tests with test fixtures"
```

## Database Management

### Migration Workflow
```bash
# Create new migration
claude "Create Alembic migration for user model changes"

# Apply migrations
claude "Apply all pending database migrations"

# Review migration
claude "Review the latest database migration for safety"
```

### Query Optimization
```bash
# Analyze slow queries
claude performance-engineer "Analyze database query performance"

# Optimize endpoints
claude "Optimize the user endpoints for better performance"
```

## API Development

### Endpoint Creation
```bash
# Create new endpoint
claude "Create a new user registration endpoint with validation"

# Add authentication
claude "Add JWT authentication to the API endpoints"

# Error handling
claude "Implement comprehensive error handling for the API"
```

### Documentation
```bash
# Generate API docs
claude generate-docs api

# Create integration guide
claude "Create API integration guide with examples"
```

## Security Best Practices

The configuration includes security-focused permissions:

- **Environment Protection**: Prevents .env file access
- **Migration Safety**: Protects database migration files
- **Virtual Environment**: Prevents accidental venv deletion
- **Dependency Security**: Alerts for security vulnerabilities

### Security Enhancements
```bash
# Security audit
claude "Perform security audit of API endpoints"

# Authentication review
claude "Review JWT implementation for security issues"

# Input validation
claude "Ensure all API inputs are properly validated"
```

## Performance Optimization

### Database Performance
```bash
# Query optimization
claude performance-engineer "Optimize database queries for user endpoints"

# Index analysis
claude "Analyze and suggest database indexes for better performance"
```

### API Performance
```bash
# Endpoint optimization
claude "Optimize API response times and throughput"

# Caching strategy
claude "Implement caching strategy for frequently accessed data"
```

## Common Tasks

```bash
# Project setup and initialization
claude setup-project fastapi

# Development workflow optimization
claude optimize-workflow backend

# API documentation generation
claude generate-docs

# Performance analysis
claude performance-engineer "Full API performance audit"

# Error investigation
claude error-detective "Investigate API response errors"
```

## Troubleshooting

### Python Environment Issues
```bash
# Check Python version and virtual environment
python --version
which python
```

### Database Connection Issues
```bash
# Test database connection
claude "Test database connection and troubleshoot issues"
```

### Permission Issues
If Claude can't run certain Python commands, verify the `allow` list includes the necessary tools.

## Related Examples

- **[React TypeScript](../react-typescript/)** - Frontend companion

### Coming Soon
- Django - Alternative Python web framework
- Go API - High-performance API alternative
- Microservices - Distributed architecture