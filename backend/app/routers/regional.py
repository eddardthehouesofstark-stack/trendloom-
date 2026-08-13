"""Regional trends API endpoints"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.database import RegionalDB

router = APIRouter()


@router.get("/countries")
async def get_countries():
    """Get available countries"""
    return {
        "success": True,
        "data": [
            {"code": "in", "name": "India"},
            {"code": "jp", "name": "Japan"},
            {"code": "fr", "name": "France"},
            {"code": "ae", "name": "UAE"},
            {"code": "ng", "name": "Nigeria"},
            {"code": "uk", "name": "United Kingdom"},
            {"code": "us", "name": "United States"}
        ]
    }


@router.get("/states")
async def get_states(country: str = Query("in")):
    """Get states/regions for a country"""
    states_by_country = {
        "in": [
            {"code": "mh", "name": "Maharashtra"},
            {"code": "dl", "name": "Delhi"},
            {"code": "ka", "name": "Karnataka"},
            {"code": "gj", "name": "Gujarat"},
            {"code": "tn", "name": "Tamil Nadu"}
        ],
        "us": [
            {"code": "ny", "name": "New York"},
            {"code": "ca", "name": "California"},
            {"code": "tx", "name": "Texas"},
            {"code": "fl", "name": "Florida"}
        ],
        "uk": [
            {"code": "eng", "name": "England"},
            {"code": "sct", "name": "Scotland"},
            {"code": "wls", "name": "Wales"}
        ]
    }
    
    return {
        "success": True,
        "data": states_by_country.get(country, [])
    }


@router.get("/trends")
async def get_regional_trends(
    country: str = Query("in"),
    state: Optional[str] = Query(None),
    limit: int = Query(10, ge=1, le=50)
):
    """Get trends by country and optionally by state"""
    try:
        if state:
            trends = RegionalDB.get_by_state(country, state, limit=limit)
        else:
            trends = RegionalDB.get_by_country(country, limit=limit)
        
        # If no data in DB, return mock data
        if not trends:
            trends = get_mock_regional_trends(country, state)
        
        return {
            "success": True,
            "count": len(trends),
            "country": country,
            "state": state,
            "data": trends
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/growth")
async def get_regional_growth(
    country: str = Query("in"),
    state: Optional[str] = Query(None)
):
    """Get growth metrics for a region"""
    growth_data = {
        "in": {
            "mh": {"velocity": 48, "top_categories": ["Eco-Silk", "Tech-Fabric", "Heritage Denim"]},
            "dl": {"velocity": 35, "top_categories": ["Contemporary Fusion", "Luxury Textiles"]},
            "ka": {"velocity": 42, "top_categories": ["Tech-Wear", "Minimalist Design"]},
        },
        "jp": {"velocity": 38, "top_categories": ["Minimalist", "Tech-Fabric", "Traditional Fusion"]},
        "fr": {"velocity": 45, "top_categories": ["Haute Couture", "Vintage Revival", "Sustainable Luxury"]},
    }
    
    if state and country in growth_data and isinstance(growth_data[country], dict):
        data = growth_data[country].get(state, {"velocity": 30, "top_categories": ["Fashion Forward"]})
    else:
        data = growth_data.get(country, {"velocity": 30, "top_categories": ["Fashion Forward"]})
    
    return {
        "success": True,
        "country": country,
        "state": state,
        "data": data
    }


def get_mock_regional_trends(country: str, state: Optional[str] = None):
    """Mock regional trends data"""
    return [
        {
            "id": 1,
            "name": "Bandra Streetstyle",
            "image_url": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400",
            "country_code": "in",
            "state_code": "mh"
        },
        {
            "id": 2,
            "name": "Parisian Chic",
            "image_url": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=400",
            "country_code": "fr",
            "state_code": None
        },
        {
            "id": 3,
            "name": "Dubai Gold Label",
            "image_url": "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=400",
            "country_code": "ae",
            "state_code": None
        },
        {
            "id": 4,
            "name": "Tokyo Minimalist",
            "image_url": "https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?w=400",
            "country_code": "jp",
            "state_code": None
        }
    ]
