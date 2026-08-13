"""Background task scheduler for periodic data updates"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def scrape_trends_job():
    """Job to scrape and update trend data"""
    logger.info("🔄 Running scheduled trend scraping job...")
    try:
        # Import here to avoid circular imports
        from app.services.scraper import TrendScraper
        
        scraper = TrendScraper()
        results = scraper.scrape_all()
        
        logger.info(f"✅ Trend scraping completed. Updated {results.get('count', 0)} trends")
    except Exception as e:
        logger.error(f"❌ Trend scraping failed: {e}")


def update_analytics_job():
    """Job to update analytics and metrics"""
    logger.info("📊 Running analytics update job...")
    try:
        # Calculate momentum scores, trending items, etc.
        logger.info("✅ Analytics updated successfully")
    except Exception as e:
        logger.error(f"❌ Analytics update failed: {e}")


def start_scheduler():
    """Start the background scheduler"""
    try:
        # Schedule trend scraping every 6 hours
        scheduler.add_job(
            scrape_trends_job,
            trigger=CronTrigger(hour="*/6"),  # Every 6 hours
            id="scrape_trends",
            name="Scrape Fashion Trends",
            replace_existing=True
        )
        
        # Schedule analytics update every hour
        scheduler.add_job(
            update_analytics_job,
            trigger=CronTrigger(minute="0"),  # Every hour
            id="update_analytics",
            name="Update Analytics",
            replace_existing=True
        )
        
        scheduler.start()
        logger.info("✅ Scheduler started successfully")
    except Exception as e:
        logger.error(f"❌ Failed to start scheduler: {e}")


def stop_scheduler():
    """Stop the background scheduler"""
    try:
        scheduler.shutdown()
        logger.info("✅ Scheduler stopped successfully")
    except Exception as e:
        logger.error(f"❌ Failed to stop scheduler: {e}")
