"""Application configuration settings."""

import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Project info
    PROJECT_NAME: str = "Natural Language to SQL Generator"
    DEBUG: bool = True
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    
    # Database Configuration
    DATABASE_URL: str = "postgresql://postgres@localhost:5433/nl_to_sql_db"
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields in .env file

# Create global settings instance
settings = Settings()