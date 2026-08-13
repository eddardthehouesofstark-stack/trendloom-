"""
Import India & Tamil Nadu Fashion Data
Run this script to fetch and import real-world fashion data
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app.services.india_data_scraper import IndiaFashionScraper
from app.database import SupabaseClient
from app.config import get_settings
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def import_india_data():
    """
    Main function to import India and Tamil Nadu fashion data
    """
    print("\n" + "="*60)
    print("🇮🇳 INDIA & TAMIL NADU FASHION DATA IMPORTER")
    print("="*60 + "\n")
    
    try:
        # Initialize
        settings = get_settings()
        db = SupabaseClient(settings)
        scraper = IndiaFashionScraper()
        
        print("📡 Step 1: Scraping fashion data from multiple sources...")
        print("   Sources: Google Trends, Myntra, Ajio, Flipkart")
        print("   Regions: India (National) + Tamil Nadu (State)")
        print("\n⏳ This may take 2-3 minutes...\n")
        
        # Scrape all data
        results = await scraper.scrape_all_india_sources()
        
        if not results['success']:
            print("❌ Failed to scrape data")
            return
        
        print("\n✅ Scraping Complete!")
        print(f"   Total trends found: {results['total_count']}")
        print(f"   India (National): {results['india_count']} trends")
        print(f"   Tamil Nadu: {results['tamilnadu_count']} trends")
        
        # Display top trends
        print("\n🔥 TOP INDIA TRENDS:")
        for i, trend in enumerate(results['india_trends'][:10], 1):
            name = trend.get('keyword', trend.get('name', 'Unknown'))
            score = trend.get('momentum_score', 0)
            sources = ', '.join(trend.get('sources', [])[:2])
            print(f"   {i}. {name:<30} Score: {score:>5.1f} [{sources}]")
        
        print("\n📍 TOP TAMIL NADU TRENDS:")
        for i, trend in enumerate(results['tamilnadu_trends'][:10], 1):
            name = trend.get('keyword', trend.get('name', 'Unknown'))
            score = trend.get('momentum_score', 0)
            sources = ', '.join(trend.get('sources', [])[:2])
            print(f"   {i}. {name:<30} Score: {score:>5.1f} [{sources}]")
        
        # Ask user confirmation
        print("\n" + "="*60)
        response = input("📥 Import this data into database? (yes/no): ").lower().strip()
        
        if response not in ['yes', 'y']:
            print("❌ Import cancelled")
            return
        
        print("\n💾 Step 2: Importing data into Supabase...")
        
        # Save to database
        save_result = await scraper.save_to_database(db.client, results)
        
        if save_result['success']:
            print(f"\n✅ SUCCESS! Imported {save_result['saved_count']} trends")
            print("\n📊 Database Updated:")
            print(f"   - trends table: {results['total_count']} new records")
            print(f"   - regional_trends table: {results['tamilnadu_count']} new records")
            
            print("\n🎉 Your TrendLoom platform now has REAL India & Tamil Nadu data!")
            print("\n🌐 View your data:")
            print("   Dashboard: https://your-vercel-url.vercel.app/dashboard.html")
            print("   Regional: https://your-vercel-url.vercel.app/regional.html")
            print("   API: https://trendloom-3aux.onrender.com/api/trends/")
        else:
            print(f"❌ Database import failed: {save_result.get('error')}")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Import cancelled by user")
    except Exception as e:
        logger.error(f"Import error: {e}")
        print(f"\n❌ Error: {e}")
        print("\n💡 Troubleshooting:")
        print("   1. Install pytrends: pip install pytrends")
        print("   2. Check internet connection")
        print("   3. Verify Supabase credentials in .env or Render")


async def test_scraper_only():
    """
    Test the scraper without saving to database
    """
    print("\n🧪 TESTING INDIA DATA SCRAPER (No Database)\n")
    
    scraper = IndiaFashionScraper()
    
    print("📡 Fetching data...\n")
    results = await scraper.scrape_all_india_sources()
    
    if results['success']:
        print(f"✅ Found {results['total_count']} trends")
        print(f"   India: {results['india_count']}")
        print(f"   Tamil Nadu: {results['tamilnadu_count']}")
        
        print("\n🔝 Sample India Trends:")
        for trend in results['india_trends'][:5]:
            name = trend.get('keyword', trend.get('name'))
            print(f"   - {name} (Score: {trend.get('momentum_score', 0):.1f})")
        
        print("\n🔝 Sample Tamil Nadu Trends:")
        for trend in results['tamilnadu_trends'][:5]:
            name = trend.get('keyword', trend.get('name'))
            print(f"   - {name} (Score: {trend.get('momentum_score', 0):.1f})")
    else:
        print(f"❌ Scraping failed: {results.get('error')}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("TRENDLOOM - INDIA DATA IMPORTER")
    print("="*60)
    print("\nChoose an option:")
    print("1. Import data into database (Full import)")
    print("2. Test scraper only (No database changes)")
    print("3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        asyncio.run(import_india_data())
    elif choice == "2":
        asyncio.run(test_scraper_only())
    else:
        print("👋 Goodbye!")
