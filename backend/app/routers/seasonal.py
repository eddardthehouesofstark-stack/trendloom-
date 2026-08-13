"""Seasonal trends API endpoints"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from app.database import SeasonalDB

router = APIRouter()


@router.get("/current")
async def get_current_season():
    """Get current season information"""
    # Determine current season based on month
    month = datetime.now().month
    
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Fall"
    
    return {
        "success": True,
        "data": {
            "season": season,
            "year": datetime.now().year,
            "month": datetime.now().month
        }
    }


@router.get("/trends")
async def get_seasonal_trends(
    season: str = Query("Spring"),
    year: int = Query(2025),
    limit: int = Query(20, ge=1, le=100)
):
    """Get trends for a specific season"""
    try:
        trends = SeasonalDB.get_by_season(season, year)
        
        # If no data, return mock data
        if not trends:
            trends = get_mock_seasonal_trends(season, year)
        
        return {
            "success": True,
            "season": season,
            "year": year,
            "count": len(trends),
            "data": trends[:limit]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forecast")
async def get_seasonal_forecast(
    season: str = Query("Fall"),
    year: int = Query(2025)
):
    """Get forecast for upcoming season"""
    forecasts = {
        "Spring": {
            "key_trends": ["Pastel Revival", "Lightweight Linens", "Floral Maximalism"],
            "colors": ["Soft Pink", "Mint Green", "Butter Yellow"],
            "confidence": 87
        },
        "Summer": {
            "key_trends": ["Breathable Tech-Fabrics", "Coastal Minimalism", "Bold Prints"],
            "colors": ["Ocean Blue", "Coral", "White"],
            "confidence": 82
        },
        "Fall": {
            "key_trends": ["Layered Textures", "Earth Tones", "Oversized Silhouettes"],
            "colors": ["Rust", "Forest Green", "Chocolate Brown"],
            "confidence": 91
        },
        "Winter": {
            "key_trends": ["Cozy Maximalism", "Metallic Accents", "Statement Outerwear"],
            "colors": ["Deep Burgundy", "Navy", "Silver"],
            "confidence": 89
        }
    }
    
    return {
        "success": True,
        "season": season,
        "year": year,
        "data": forecasts.get(season, forecasts["Spring"])
    }


def get_mock_seasonal_trends(season: str, year: int):
    """Mock seasonal trends data"""
    base_trends = [
        {
            "id": 1,
            "name": "Oversized Blazers",
            "category": "Tailoring",
            "momentum_score": 92,
            "season": season,
            "year": year
        },
        {
            "id": 2,
            "name": "Sustainable Denim",
            "category": "Denim",
            "momentum_score": 88,
            "season": season,
            "year": year
        },
        {
            "id": 3,
            "name": "Chunky Knits",
            "category": "Knitwear",
            "momentum_score": 85,
            "season": season,
            "year": year
        }
    ]
    return base_trends
