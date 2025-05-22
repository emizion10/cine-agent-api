# Cine Agent API

A FastAPI-based backend application for movie search and personalized suggestions using The Movie Database (TMDB) API.

## Features

- Movie search functionality
- Movie details retrieval
- Popular movies listing
- Movie recommendations
- Genre listing
- User authentication
- User favorites management

## Project Structure

```
cine-agent-api/
├── src/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── movies.py
│   │       │   └── auth.py
│   │       └── api.py
│   ├── config/
│   │   └── settings.py
│   ├── core/
│   │   └── security.py
│   ├── crud/
│   │   └── user.py
│   ├── db/
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── services/
│   │   └── tmdb_service.py
│   └── main.py
├── alembic/
│   ├── versions/
│   │   └── initial_migration.py
│   └── env.py
├── .env
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- TMDB API key (Get it from https://www.themoviedb.org/settings/api)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd cine-agent-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
TMDB_API_KEY=your_tmdb_api_key_here
TMDB_API_BASE_URL=https://api.themoviedb.org/3
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=cine_agent
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

5. Start the PostgreSQL database using Docker Compose:
```bash
docker-compose up -d
```

6. Run database migrations:
```bash
# Set PYTHONPATH to include the project root directory
export PYTHONPATH=$PYTHONPATH:$(pwd)  # On Unix/macOS
# or
set PYTHONPATH=%PYTHONPATH%;%cd%  # On Windows

# Initialize the database with the first migration
alembic upgrade head
```

7. Run the application:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Movies
- `GET /api/v1/movies/search` - Search for movies
- `GET /api/v1/movies/{movie_id}` - Get movie details
- `GET /api/v1/movies/popular` - Get popular movies
- `GET /api/v1/movies/{movie_id}/recommendations` - Get movie recommendations
- `GET /api/v1/movies/genres` - Get movie genres

### Authentication
- `POST /api/v1/auth/signup` - Create a new user account
- `POST /api/v1/auth/login` - Login and get access token

### User Favorites
- `GET /api/v1/users/favorites` - Get user favorites
- `POST /api/v1/users/favorites/{movie_id}` - Add movie to favorites
- `DELETE /api/v1/users/favorites/{movie_id}` - Remove movie from favorites

## Database Management

### Running Migrations

To create a new migration:
```bash
# Make sure PYTHONPATH is set
export PYTHONPATH=$PYTHONPATH:$(pwd)  # On Unix/macOS
# or
set PYTHONPATH=%PYTHONPATH%;%cd%  # On Windows

alembic revision --autogenerate -m "description of changes"
```

To apply migrations:
```bash
# Make sure PYTHONPATH is set
export PYTHONPATH=$PYTHONPATH:$(pwd)  # On Unix/macOS
# or
set PYTHONPATH=%PYTHONPATH%;%cd%  # On Windows

alembic upgrade head
```

To rollback migrations:
```bash
# Make sure PYTHONPATH is set
export PYTHONPATH=$PYTHONPATH:$(pwd)  # On Unix/macOS
# or
set PYTHONPATH=%PYTHONPATH%;%cd%  # On Windows

alembic downgrade -1  # Rollback one migration
# or
alembic downgrade base  # Rollback all migrations
```

### Database Backup and Restore

To backup the database:
```bash
docker exec cine_agent_db pg_dump -U postgres cine_agent > backup.sql
```

To restore from backup:
```bash
docker exec -i cine_agent_db psql -U postgres cine_agent < backup.sql
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request