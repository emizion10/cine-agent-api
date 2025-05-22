from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the root directory of the project
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from .env file
load_dotenv(dotenv_path=ROOT_DIR / ".env")

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Cine Agent API"
    VERSION: str = "1.0.0"
    
    # TMDB Settings
    TMDB_API_KEY: str = os.getenv("TMDB_API_KEY")
    TMDB_API_BASE_URL: str = os.getenv("TMDB_API_BASE_URL", "https://api.themoviedb.org/3")
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    class Config:
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings() 