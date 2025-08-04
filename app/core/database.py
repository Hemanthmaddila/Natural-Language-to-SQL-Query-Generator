"""Database connection and session management."""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG  # Shows SQL queries in logs when DEBUG=True
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_database_connection():
    """Get a database connection for LangChain SQL agent."""
    return engine

def test_connection():
    """Test if database connection works."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM products"))
            count = result.scalar()
            return f"✅ Database connected! Found {count} products."
    except Exception as e:
        return f"❌ Database connection failed: {e}"