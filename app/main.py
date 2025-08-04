from fastapi import FastAPI

# Create our FastAPI application
app = FastAPI(
    title="Natural Language to SQL Query Generator",
    description="Transform natural language questions into SQL queries",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Welcome page for our application."""
    return {
        "message": "🚀 Welcome to Natural Language to SQL Query Generator!",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "nl-to-sql-generator"}