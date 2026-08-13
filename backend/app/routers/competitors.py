"""Competitor trends API endpoints"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

router = APIRouter()


@router.get("/")
async def get_competitors(limit: int = Query(10, ge=1, le=50)):
    """Get competitor list"""
    competitors = [
        {"id": 1, "name": "Zara", "market_share": 15.2, "trend_score": 88},
        {"id": 2, "name": "H&M", "market_share": 12.8, "trend_score": 82},
        {"id": 3, "name": "Uniqlo", "market_share": 10.5, "trend_score": 85},
        {"id": 4, "name": "Shein", "market_share": 18.3, "trend_score": 79},
        {"id": 5, "name": "Nike", "market_share": 9.7, "trend_score": 91}
    ]
    
    return {
        "success": True,
        "count": len(competitors),
        "data": competitors[:limit]
    }


@router.get("/{competitor_id}")
async def get_competitor_detail(competitor_id: int):
    """Get detailed competitor analysis"""
    mock_data = {
        "id": competitor_id,
        "name": "Zara",
        "market_share": 15.2,
        "trend_score": 88,
        "recent_collections": [
            {"name": "Spring Essentials", "launch_date": "2025-02-15"},
            {"name": "Summer Preview", "launch_date": "2025-03-01"}
        ],
        "top_categories": ["Fast Fashion", "Contemporary", "Basics"],
        "pricing_strategy": "Mid-range",
        "growth_velocity": "+12%"
    }
    
    return {
        "success": True,
        "data": mock_data
    }


@router.get("/trends/comparison")
async def compare_trends(competitors: str = Query("1,2,3")):
    """Compare trends across competitors"""
    competitor_ids = [int(x) for x in competitors.split(",")]
    
    return {
        "success": True,
        "data": {
            "compared_competitors": competitor_ids,
            "common_trends": ["Oversized Silhouettes", "Sustainable Materials", "Neutral Palettes"],
            "unique_trends": {
                "1": ["Spanish-inspired Prints"],
                "2": ["Scandinavian Minimalism"],
                "3": ["Japanese Basics"]
            }
        }
    }
