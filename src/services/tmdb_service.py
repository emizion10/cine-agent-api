import httpx
from typing import Dict, List, Optional
from src.config.settings import get_settings
from fastapi import HTTPException

settings = get_settings()

class TMDBService:
    def __init__(self):
        if not settings.TMDB_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="TMDB API key not found. Please check your .env file and ensure TMDB_API_KEY is set."
            )
        
        self.api_key = settings.TMDB_API_KEY
        self.base_url = settings.TMDB_API_BASE_URL or "https://api.themoviedb.org/3"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    async def search_movies(self, query: str, page: int = 1) -> Dict:
        """Search for movies using TMDB API"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/search/movie",
                    params={"query": query, "page": page},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching data from TMDB API: {str(e)}"
            )

    async def get_movie_details(self, movie_id: int) -> Dict:
        """Get detailed information about a specific movie"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/movie/{movie_id}",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching movie details from TMDB API: {str(e)}"
            )

    async def get_popular_movies(self, page: int = 1) -> Dict:
        """Get list of popular movies"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/movie/popular",
                    params={"page": page},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching popular movies from TMDB API: {str(e)}"
            )

    async def get_movie_recommendations(self, movie_id: int, page: int = 1) -> Dict:
        """Get movie recommendations based on a specific movie"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/movie/{movie_id}/recommendations",
                    params={"page": page},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching movie recommendations from TMDB API: {str(e)}"
            )

    async def get_movie_genres(self) -> Dict:
        """Get list of movie genres"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/genre/movie/list",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching movie genres from TMDB API: {str(e)}"
            ) 