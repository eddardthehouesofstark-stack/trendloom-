"""
TrendLoom Backend API
FastAPI + Supabase for real-time fashion trend intelligence
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from app.config import settings
from app.routers import trends, regional, seasonal, competitors, recommendations, attributes
from app.services.scheduler import start_scheduler, stop_scheduler
from app.database import init_database

# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    # Startup
    print("🚀 Starting TrendLoom API...")
    await init_database()
    start_scheduler()
    print("✅ TrendLoom API is ready!")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down TrendLoom API...")
    stop_scheduler()
    print("✅ TrendLoom API stopped gracefully")


# Initialize FastAPI app
app = FastAPI(
    title="TrendLoom API",
    description="Real-time Fashion Intelligence & Trend Analysis Platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        settings.FRONTEND_URL,
        settings.VERCEL_URL,
        "*"  # Remove in production, specify exact domains
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/")
async def root():
    """API health check"""
    return {
        "status": "online",
        "service": "TrendLoom API",
        "version": "1.0.0",
        "message": "Fashion Intelligence API is running"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "scheduler": "active",
        "environment": settings.ENVIRONMENT
    }


# Include routers
app.include_router(trends.router, prefix="/api/trends", tags=["Trends"])
app.include_router(regional.router, prefix="/api/regional", tags=["Regional"])
app.include_router(seasonal.router, prefix="/api/seasonal", tags=["Seasonal"])
app.include_router(competitors.router, prefix="/api/competitors", tags=["Competitors"])
app.include_router(recommendations.router, prefix="/api/recommendations", tags=["Recommendations"])
app.include_router(attributes.router, prefix="/api/attributes", tags=["Attributes"])


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True if settings.ENVIRONMENT == "development" else False
    )
