from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import engine, get_db

app = FastAPI(
    title="MIZAN API",
    description="AI Multi-Agent financial",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MIZAN API",
        "status": "running"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }