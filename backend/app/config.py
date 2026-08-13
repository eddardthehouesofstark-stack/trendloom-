"""Configuration settings for TrendLoom API"""

from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    SUPABASE_SERVICE_KEY: str = os.getenv("SUPABASE_SERVICE_KEY", "")
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Frontend URLs
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    VERCEL_URL: str = os.getenv("VERCEL_URL", "")
    
    # External APIs (Optional)
    GOOGLE_TRENDS_API_KEY: Optional[str] = os.getenv("GOOGLE_TRENDS_API_KEY")
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # Scheduler settings
    SCRAPE_INTERVAL_HOURS: int = 6  # Scrape trends every 6 hours
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
