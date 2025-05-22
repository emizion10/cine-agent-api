# Cine Agent API

A FastAPI-based backend application for movie search and personalized suggestions using The Movie Database (TMDB) API.

## Features

- Movie search functionality
- Movie details retrieval
- Popular movies listing
- Movie recommendations
- Genre listing
- (Planned) User authentication
- (Planned) User favorites management

## Project Structure

```
cine-agent-api/
├── src/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── movies.py
│   │       └── api.py
│   ├── config/
│   │   └── settings.py
│   ├── core/
│   ├── models/
│   ├── services/
│   │   └── tmdb_service.py
│   └── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.8+
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
```

5. Run the application:
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

### Authentication (To be implemented)
- `POST /api/v1/token` - Login endpoint
- `GET /api/v1/users/me` - Get user profile

### User Favorites (To be implemented)
- `GET /api/v1/users/favorites` - Get user favorites
- `POST /api/v1/users/favorites/{movie_id}` - Add movie to favorites
- `DELETE /api/v1/users/favorites/{movie_id}` - Remove movie from favorites

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 