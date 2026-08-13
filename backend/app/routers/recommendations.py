"""AI Recommendations API endpoints"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime

router = APIRouter()


@router.get("/")
async def get_recommendations(
    category: Optional[str] = None,
    limit: int = Query(10, ge=1, le=50)
):
    """Get AI-powered production recommendations"""
    recommendations = [
        {
            "id": 1,
            "title": "Increase Production: Wide-Leg Trousers",
            "category": "Tailoring",
            "priority": "HIGH",
            "confidence": 92,
            "reasoning": "Strong momentum across EU and APAC markets. 3-month sustained growth.",
            "suggested_action": "Scale production by 40%",
            "expected_roi": "+28%",
            "time_horizon": "Q2 2025"
        },
        {
            "id": 2,
            "title": "Hold: Sheer Fabrics",
            "category": "Textiles",
            "priority": "MEDIUM",
            "confidence": 68,
            "reasoning": "Mixed signals. Strong in fashion-forward markets, weak in conservative regions.",
            "suggested_action": "Maintain current levels, monitor for 2 weeks",
            "expected_roi": "+8%",
            "time_horizon": "Q2 2025"
        },
        {
            "id": 3,
            "title": "Reduce: Neon Colors",
            "category": "Colors",
            "priority": "HIGH",
            "confidence": 87,
            "reasoning": "Declining interest globally. Peak passed 6 weeks ago.",
            "suggested_action": "Phase out gradually, clear inventory",
            "expected_roi": "-5% (minimize loss)",
            "time_horizon": "Next 4 weeks"
        },
        {
            "id": 4,
            "title": "Explore: Sustainable Silk Alternatives",
            "category": "Textiles",
            "priority": "MEDIUM",
            "confidence": 75,
            "reasoning": "Emerging trend with strong sustainability angle. Early adopter advantage.",
            "suggested_action": "Small batch test production",
            "expected_roi": "+15%",
            "time_horizon": "Q3 2025"
        }
    ]
    
    # Filter by category if provided
    if category:
        recommendations = [r for r in recommendations if r["category"] == category]
    
    return {
        "success": True,
        "count": len(recommendations),
        "generated_at": datetime.utcnow().isoformat(),
        "data": recommendations[:limit]
    }


@router.get("/{recommendation_id}")
async def get_recommendation_detail(recommendation_id: int):
    """Get detailed recommendation analysis"""
    return {
        "success": True,
        "data": {
            "id": recommendation_id,
            "title": "Increase Production: Wide-Leg Trousers",
            "detailed_analysis": {
                "market_signals": [
                    "EU market: +45% search volume",
                    "APAC market: +32% social mentions",
                    "US market: +28% retail sales"
                ],
                "competitor_actions": [
                    "Zara increased inventory by 35%",
                    "H&M launched dedicated collection"
                ],
                "risk_factors": [
                    "Low: Market saturation risk minimal",
                    "Medium: Supply chain considerations"
                ],
                "supporting_data": {
                    "google_trends_score": 89,
                    "social_sentiment": 0.84,
                    "retail_velocity": 1.42
                }
            }
        }
    }


@router.post("/feedback")
async def submit_recommendation_feedback(
    recommendation_id: int,
    action_taken: str,
    outcome: Optional[str] = None
):
    """Submit feedback on recommendation outcomes"""
    return {
        "success": True,
        "message": "Feedback recorded successfully",
        "data": {
            "recommendation_id": recommendation_id,
            "action_taken": action_taken,
            "outcome": outcome,
            "recorded_at": datetime.utcnow().isoformat()
        }
    }
