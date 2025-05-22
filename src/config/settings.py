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
    
    # Database Settings
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "cine_agent")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        """Get database URL."""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # Security Settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    class Config:
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings() 