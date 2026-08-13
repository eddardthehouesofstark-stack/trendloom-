"""Supabase database connection and operations"""

from supabase import create_client, Client
from app.config import settings
from typing import Optional, List, Dict, Any
import logging

logger = logging.getLogger(__name__)

# Global Supabase client
supabase: Optional[Client] = None


def get_supabase() -> Client:
    """Get Supabase client instance"""
    global supabase
    
    if supabase is None:
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
            raise ValueError("Supabase credentials not configured")
        
        supabase = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        logger.info("✅ Supabase client initialized")
    
    return supabase


async def init_database():
    """Initialize database connection and create tables if needed"""
    try:
        client = get_supabase()
        logger.info("✅ Database connection established")
        
        # Test connection
        response = client.table('trends').select("id").limit(1).execute()
        logger.info("✅ Database tables verified")
        
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        # Don't raise - allow app to start even if tables don't exist yet


# Database helper functions
class TrendDB:
    """Trends database operations"""
    
    @staticmethod
    def get_all_trends(limit: int = 100) -> List[Dict[str, Any]]:
        """Get all trends"""
        try:
            response = get_supabase().table('trends').select("*").limit(limit).order('created_at', desc=True).execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching trends: {e}")
            return []
    
    @staticmethod
    def get_trending_now(limit: int = 10) -> List[Dict[str, Any]]:
        """Get currently trending items"""
        try:
            response = get_supabase().table('trends').select("*").eq('status', 'trending').limit(limit).order('momentum_score', desc=True).execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching trending items: {e}")
            return []
    
    @staticmethod
    def create_trend(data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new trend record"""
        try:
            response = get_supabase().table('trends').insert(data).execute()
            return response.data[0] if response.data else {}
        except Exception as e:
            logger.error(f"Error creating trend: {e}")
            return {}
    
    @staticmethod
    def update_trend(trend_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a trend record"""
        try:
            response = get_supabase().table('trends').update(data).eq('id', trend_id).execute()
            return response.data[0] if response.data else {}
        except Exception as e:
            logger.error(f"Error updating trend: {e}")
            return {}


class RegionalDB:
    """Regional trends database operations"""
    
    @staticmethod
    def get_by_country(country_code: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get trends by country"""
        try:
            response = get_supabase().table('regional_trends').select("*").eq('country_code', country_code).limit(limit).execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching regional trends: {e}")
            return []
    
    @staticmethod
    def get_by_state(country_code: str, state_code: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Get trends by state/region"""
        try:
            response = get_supabase().table('regional_trends').select("*").eq('country_code', country_code).eq('state_code', state_code).limit(limit).execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching state trends: {e}")
            return []


class SeasonalDB:
    """Seasonal trends database operations"""
    
    @staticmethod
    def get_by_season(season: str, year: int) -> List[Dict[str, Any]]:
        """Get trends by season"""
        try:
            response = get_supabase().table('seasonal_trends').select("*").eq('season', season).eq('year', year).execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching seasonal trends: {e}")
            return []
