from fastapi import APIRouter, HTTPException, Query
from src.services.tmdb_service import TMDBService

router = APIRouter()
tmdb_service = TMDBService()


@router.get("/search")
async def search_movies(
    query: str = Query(..., description="Search query for movies"),
    page: int = Query(1, description="Page number for pagination")
):
    """Search for movies using TMDB API"""
    try:
        results = await tmdb_service.search_movies(query, page)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/popular")
async def get_popular_movies(page: int = Query(1, description="Page number for pagination")):
    """Get list of popular movies"""
    try:
        movies = await tmdb_service.get_popular_movies(page)
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/genres")
async def get_movie_genres():
    """Get list of movie genres"""
    try:
        genres = await tmdb_service.get_movie_genres()
        return genres
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{movie_id}")
async def get_movie_details(movie_id: int):
    """Get detailed information about a specific movie"""
    try:
        movie = await tmdb_service.get_movie_details(movie_id)
        return movie
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{movie_id}/recommendations")
async def get_movie_recommendations(
    movie_id: int,
    page: int = Query(1, description="Page number for pagination")
):
    """Get movie recommendations based on a specific movie"""
    try:
        recommendations = await tmdb_service.get_movie_recommendations(movie_id, page)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 