"""
Test India Fashion Data Scraper
Run this to see what data will be collected (no database required)
"""

import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.services.india_data_scraper import IndiaFashionScraper
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_scraper():
    """
    Test the scraper and show results without database
    """
    print("\n" + "="*70)
    print("🇮🇳 INDIA & TAMIL NADU FASHION DATA SCRAPER - TEST MODE")
    print("="*70 + "\n")
    
    print("📡 Fetching real-time fashion data from:")
    print("   ✅ Google Trends India (National)")
    print("   ✅ Google Trends Tamil Nadu (State)")
    print("   ✅ Indian E-commerce sites (Myntra, Ajio, Flipkart)")
    print("\n⏳ This may take 2-3 minutes (fetching live data)...\n")
    
    try:
        scraper = IndiaFashionScraper()
        
        # Scrape all data
        results = await scraper.scrape_all_india_sources()
        
        if not results['success']:
            print(f"❌ Scraping failed: {results.get('error')}")
            return
        
        # Display results
        print("\n" + "="*70)
        print("✅ SCRAPING COMPLETE!")
        print("="*70)
        
        print(f"\n📊 SUMMARY:")
        print(f"   Total Trends Found: {results['total_count']}")
        print(f"   India (National): {results['india_count']} trends")
        print(f"   Tamil Nadu (State): {results['tamilnadu_count']} trends")
        print(f"   Data Sources: {', '.join(results['sources'])}")
        
        # Top India trends
        print("\n" + "="*70)
        print("🔥 TOP 15 INDIA NATIONAL TRENDS")
        print("="*70)
        print(f"{'#':<3} {'Trend Name':<35} {'Score':<6} {'Sources':<20}")
        print("-"*70)
        
        for i, trend in enumerate(results['india_trends'][:15], 1):
            name = trend.get('keyword', trend.get('name', 'Unknown'))[:34]
            score = trend.get('momentum_score', 0)
            sources = ', '.join(trend.get('sources', [])[:2])[:19]
            print(f"{i:<3} {name:<35} {score:>5.1f}  {sources:<20}")
        
        # Top Tamil Nadu trends
        print("\n" + "="*70)
        print("📍 TOP 10 TAMIL NADU REGIONAL TRENDS")
        print("="*70)
        print(f"{'#':<3} {'Trend Name':<35} {'Score':<6} {'Sources':<20}")
        print("-"*70)
        
        for i, trend in enumerate(results['tamilnadu_trends'][:10], 1):
            name = trend.get('keyword', trend.get('name', 'Unknown'))[:34]
            score = trend.get('momentum_score', 0)
            sources = ', '.join(trend.get('sources', [])[:2])[:19]
            print(f"{i:<3} {name:<35} {score:>5.1f}  {sources:<20}")
        
        # Category breakdown
        categories = {}
        for trend in results['trends']:
            cat = trend.get('category', 'Unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        print("\n" + "="*70)
        print("📂 CATEGORY BREAKDOWN")
        print("="*70)
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"   {cat:<30} {count:>3} trends")
        
        # Sample data structure
        print("\n" + "="*70)
        print("💾 SAMPLE DATA STRUCTURE")
        print("="*70)
        
        if results['tamilnadu_trends']:
            sample = results['tamilnadu_trends'][0]
            print(f"\nExample Tamil Nadu Trend:")
            print(f"  Name: {sample.get('keyword', sample.get('name'))}")
            print(f"  Region: {sample.get('region')}")
            print(f"  Country: {sample.get('country')}")
            print(f"  Momentum Score: {sample.get('momentum_score'):.1f}")
            print(f"  Sources: {', '.join(sample.get('sources', []))}")
            if 'avg_interest' in sample:
                print(f"  Search Volume: {sample.get('avg_interest'):.1f}")
            if 'recent_interest' in sample:
                print(f"  Recent Interest: {sample.get('recent_interest'):.1f}")
        
        print("\n" + "="*70)
        print("🎉 SUCCESS! Data is ready for import")
        print("="*70)
        
        print("\n💡 NEXT STEPS:")
        print("   1. Review the trends above")
        print("   2. Verify Supabase credentials are set in Render")
        print("   3. Run: python backend/import_india_data.py")
        print("   4. Choose option 1 to import this data")
        
        print("\n✅ This data will populate your TrendLoom dashboard!")
        print("   - Dashboard will show real India trends")
        print("   - Regional page: India → Tamil Nadu will work")
        print("   - All with real momentum scores and search volumes")
        
        return results
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Scraping cancelled by user")
    except Exception as e:
        logger.error(f"Error during scraping: {e}", exc_info=True)
        print(f"\n❌ Error: {e}")
        print("\n💡 Troubleshooting:")
        print("   1. Check internet connection")
        print("   2. Verify pytrends is installed: python -m pip install pytrends")
        print("   3. Try again in a few minutes (rate limits)")


if __name__ == "__main__":
    asyncio.run(test_scraper())
