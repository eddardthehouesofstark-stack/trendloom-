"""Trends API endpoints"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from app.database import TrendDB

router = APIRouter()


# Pydantic models
class TrendResponse(BaseModel):
    id: int
    name: str
    category: str
    momentum_score: float
    status: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    created_at: str
    updated_at: str


class KPIResponse(BaseModel):
    market_coverage: float
    trend_accuracy: float
    signal_strength: str
    active_signals: int


@router.get("/")
async def get_all_trends(
    limit: int = Query(100, ge=1, le=500),
    category: Optional[str] = None
):
    """Get all fashion trends"""
    try:
        trends = TrendDB.get_all_trends(limit=limit)
        
        # Filter by category if provided
        if category:
            trends = [t for t in trends if t.get('category') == category]
        
        return {
            "success": True,
            "count": len(trends),
            "data": trends
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/trending")
async def get_trending_now(limit: int = Query(10, ge=1, le=50)):
    """Get currently trending items"""
    try:
        trends = TrendDB.get_trending_now(limit=limit)
        
        return {
            "success": True,
            "count": len(trends),
            "data": trends,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/kpis")
async def get_kpis():
    """Get dashboard KPIs"""
    try:
        # In production, calculate these from actual data
        return {
            "success": True,
            "data": {
                "market_coverage": 78.0,
                "market_coverage_change": 2.0,
                "trend_accuracy": 94.0,
                "trend_accuracy_change": 5.0,
                "signal_strength": "High",
                "active_signals": 124
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/action-board")
async def get_action_board():
    """Get prioritized production recommendations"""
    try:
        return {
            "success": True,
            "data": [
                {
                    "category": "PRODUCE NOW",
                    "certainty": 85,
                    "name": "Neutral Wide-Leg Trousers",
                    "momentum": 85,
                    "color": "green"
                },
                {
                    "category": "WAIT / MONITOR",
                    "certainty": 45,
                    "name": "Heavy Embellishments",
                    "momentum": 45,
                    "color": "yellow",
                    "note": "Early APAC indicators"
                },
                {
                    "category": "AVOID",
                    "certainty": 15,
                    "name": "Neon Synthetics",
                    "momentum": 15,
                    "color": "red",
                    "note": "Crashed below baseline"
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/categories")
async def get_categories():
    """Get all trend categories"""
    try:
        return {
            "success": True,
            "data": [
                "Tailoring",
                "Knitwear",
                "Denim",
                "Outerwear",
                "Footwear",
                "Accessories",
                "Textiles",
                "Colors",
                "Patterns",
                "Silhouettes"
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
