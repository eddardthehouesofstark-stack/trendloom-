"""
India & Tamil Nadu Fashion Data Scraper
Real-world fashion trend data specific to India and Tamil Nadu market
"""

import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import logging
from datetime import datetime
import asyncio

logger = logging.getLogger(__name__)


class IndiaFashionScraper:
    """
    Scrapes real fashion trend data for India and Tamil Nadu
    
    Data Sources:
    1. Google Trends India - Fashion keywords for India/Tamil Nadu
    2. Myntra - Top Indian fashion e-commerce
    3. Ajio - Indian fashion trends
    4. Flipkart Fashion
    5. Indian fashion publications
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'en-IN,en;q=0.9'
        }
        
        # Fashion keywords specific to India/Tamil Nadu
        self.indian_fashion_keywords = [
            # Traditional wear
            'saree', 'salwar kameez', 'kurti', 'lehenga', 'anarkali',
            'churidar', 'dupatta', 'palazzo', 'ethnic wear', 'indo western',
            
            # Western wear popular in India
            'crop top', 'jeans', 'maxi dress', 'jumpsuit', 'denim jacket',
            
            # Fabrics popular in India
            'cotton', 'silk saree', 'khadi', 'chanderi', 'banarasi',
            
            # Trending styles
            'fusion wear', 'sustainable fashion india', 'handloom',
            'bollywood fashion', 'festive wear'
        ]
        
        # Tamil Nadu specific keywords
        self.tamilnadu_keywords = [
            'kanchipuram saree', 'pattu saree', 'madurai cotton',
            'kovai kora', 'salem silk', 'chettinad cotton',
            'temple jewellery', 'south indian fashion'
        ]
    
    # ============ GOOGLE TRENDS INDIA ============
    
    async def get_india_google_trends(self) -> Dict[str, Any]:
        """
        Get Google Trends data specifically for India and Tamil Nadu
        Using pytrends library (free, no API key needed)
        """
        try:
            from pytrends.request import TrendReq
            
            # Initialize with India settings
            pytrends = TrendReq(hl='en-IN', tz=330)  # IST timezone
            
            all_trends = []
            
            # Fetch trends for India (national level)
            for i in range(0, len(self.indian_fashion_keywords), 5):
                batch = self.indian_fashion_keywords[i:i+5]
                
                try:
                    # India-wide trends
                    pytrends.build_payload(
                        batch, 
                        timeframe='today 3-m',
                        geo='IN'  # India
                    )
                    
                    interest_data = pytrends.interest_over_time()
                    
                    for keyword in batch:
                        if keyword in interest_data.columns:
                            avg_interest = interest_data[keyword].mean()
                            recent_interest = interest_data[keyword].tail(7).mean()
                            
                            # Calculate momentum (recent vs average)
                            momentum = (recent_interest / avg_interest * 100) if avg_interest > 0 else 50
                            
                            all_trends.append({
                                'keyword': keyword,
                                'country': 'India',
                                'region': 'National',
                                'momentum_score': float(momentum),
                                'avg_interest': float(avg_interest),
                                'recent_interest': float(recent_interest),
                                'source': 'Google Trends India',
                                'timestamp': datetime.utcnow().isoformat()
                            })
                    
                    await asyncio.sleep(1)  # Rate limiting
                    
                except Exception as e:
                    logger.warning(f"Failed to fetch batch {batch}: {e}")
                    continue
            
            # Fetch Tamil Nadu specific trends
            for i in range(0, len(self.tamilnadu_keywords), 5):
                batch = self.tamilnadu_keywords[i:i+5]
                
                try:
                    pytrends.build_payload(
                        batch,
                        timeframe='today 3-m',
                        geo='IN-TN'  # Tamil Nadu
                    )
                    
                    interest_data = pytrends.interest_over_time()
                    
                    for keyword in batch:
                        if keyword in interest_data.columns:
                            avg_interest = interest_data[keyword].mean()
                            recent_interest = interest_data[keyword].tail(7).mean()
                            momentum = (recent_interest / avg_interest * 100) if avg_interest > 0 else 50
                            
                            all_trends.append({
                                'keyword': keyword,
                                'country': 'India',
                                'region': 'Tamil Nadu',
                                'momentum_score': float(momentum),
                                'avg_interest': float(avg_interest),
                                'recent_interest': float(recent_interest),
                                'source': 'Google Trends Tamil Nadu',
                                'timestamp': datetime.utcnow().isoformat()
                            })
                    
                    await asyncio.sleep(1)
                    
                except Exception as e:
                    logger.warning(f"Failed to fetch TN batch {batch}: {e}")
                    continue
            
            logger.info(f"✅ Fetched {len(all_trends)} trends from Google Trends India")
            return {'success': True, 'data': all_trends}
            
        except ImportError:
            logger.error("pytrends not installed. Run: pip install pytrends")
            return {'success': False, 'error': 'pytrends not installed', 'data': []}
        except Exception as e:
            logger.error(f"Google Trends India error: {e}")
            return {'success': False, 'error': str(e), 'data': []}
    
    # ============ MYNTRA SCRAPING ============
    
    async def scrape_myntra_trends(self) -> List[Dict[str, Any]]:
        """
        Scrape Myntra (India's top fashion e-commerce)
        """
        trends = []
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=20) as client:
                # Myntra trending section
                urls = [
                    "https://www.myntra.com/women-ethnic-wear",
                    "https://www.myntra.com/women-western-wear",
                    "https://www.myntra.com/fusion-wear"
                ]
                
                for url in urls:
                    try:
                        response = await client.get(url)
                        
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            
                            # Find product cards
                            products = soup.find_all('li', class_='product-base')
                            
                            for product in products[:15]:
                                name_elem = product.find('h3', class_='product-brand')
                                product_name = product.find('h4', class_='product-product')
                                
                                if name_elem and product_name:
                                    trends.append({
                                        'name': f"{product_name.text.strip()}",
                                        'brand': name_elem.text.strip(),
                                        'category': 'E-commerce India',
                                        'country': 'India',
                                        'region': 'National',
                                        'source': 'Myntra',
                                        'momentum_score': 75,
                                        'timestamp': datetime.utcnow().isoformat()
                                    })
                        
                        await asyncio.sleep(1)
                        
                    except Exception as e:
                        logger.warning(f"Failed to scrape {url}: {e}")
                        continue
        
        except Exception as e:
            logger.error(f"Myntra scraping error: {e}")
        
        logger.info(f"✅ Scraped {len(trends)} trends from Myntra")
        return trends
    
    # ============ AJIO SCRAPING ============
    
    async def scrape_ajio_trends(self) -> List[Dict[str, Any]]:
        """
        Scrape Ajio (Reliance's fashion platform)
        """
        trends = []
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=20) as client:
                url = "https://www.ajio.com/shop/women"
                response = await client.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    products = soup.find_all('div', class_='item')[:20]
                    
                    for product in products:
                        name = product.find('div', class_='nameCls')
                        if name:
                            trends.append({
                                'name': name.text.strip(),
                                'category': 'E-commerce India',
                                'country': 'India',
                                'region': 'National',
                                'source': 'Ajio',
                                'momentum_score': 72,
                                'timestamp': datetime.utcnow().isoformat()
                            })
        
        except Exception as e:
            logger.error(f"Ajio scraping error: {e}")
        
        logger.info(f"✅ Scraped {len(trends)} trends from Ajio")
        return trends
    
    # ============ FLIPKART FASHION ============
    
    async def scrape_flipkart_fashion(self) -> List[Dict[str, Any]]:
        """
        Scrape Flipkart Fashion
        """
        trends = []
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=20) as client:
                url = "https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo"
                response = await client.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    products = soup.find_all('div', class_='_1AtVbE')[:20]
                    
                    for product in products:
                        name = product.find('a', class_='IRpwTa')
                        if name:
                            trends.append({
                                'name': name.text.strip(),
                                'category': 'E-commerce India',
                                'country': 'India',
                                'region': 'National',
                                'source': 'Flipkart',
                                'momentum_score': 70,
                                'timestamp': datetime.utcnow().isoformat()
                            })
        
        except Exception as e:
            logger.error(f"Flipkart scraping error: {e}")
        
        logger.info(f"✅ Scraped {len(trends)} trends from Flipkart")
        return trends
    
    # ============ AGGREGATE ALL INDIA DATA ============
    
    async def scrape_all_india_sources(self) -> Dict[str, Any]:
        """
        Scrape all Indian data sources in parallel
        """
        logger.info("🇮🇳 Starting India & Tamil Nadu fashion data scraping...")
        
        # Run all scrapers in parallel
        results = await asyncio.gather(
            self.get_india_google_trends(),
            self.scrape_myntra_trends(),
            self.scrape_ajio_trends(),
            self.scrape_flipkart_fashion(),
            return_exceptions=True
        )
        
        # Combine all results
        all_trends = []
        for result in results:
            if isinstance(result, dict) and 'data' in result:
                all_trends.extend(result['data'])
            elif isinstance(result, list):
                all_trends.extend(result)
            elif isinstance(result, Exception):
                logger.warning(f"Scraper failed: {result}")
        
        # Aggregate and deduplicate
        aggregated = self._aggregate_india_trends(all_trends)
        
        # Separate Tamil Nadu and India-wide trends
        tamilnadu_trends = [t for t in aggregated if t.get('region') == 'Tamil Nadu']
        india_trends = [t for t in aggregated if t.get('region') == 'National']
        
        logger.info(f"✅ Scraped {len(india_trends)} India trends and {len(tamilnadu_trends)} Tamil Nadu trends")
        
        return {
            'success': True,
            'total_count': len(aggregated),
            'india_count': len(india_trends),
            'tamilnadu_count': len(tamilnadu_trends),
            'trends': aggregated,
            'india_trends': india_trends,
            'tamilnadu_trends': tamilnadu_trends,
            'timestamp': datetime.utcnow().isoformat(),
            'sources': ['Google Trends India', 'Myntra', 'Ajio', 'Flipkart']
        }
    
    def _aggregate_india_trends(self, trends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Aggregate trends from multiple sources
        Handle duplicates and calculate average momentum
        """
        trend_dict = {}
        
        for trend in trends:
            # Use keyword or name as key
            key = trend.get('keyword', trend.get('name', '')).lower().strip()
            if not key:
                continue
            
            # Create composite key with region
            region = trend.get('region', 'National')
            composite_key = f"{key}_{region}"
            
            if composite_key in trend_dict:
                # Average momentum scores
                existing = trend_dict[composite_key]
                existing['momentum_score'] = (
                    existing['momentum_score'] + trend.get('momentum_score', 50)
                ) / 2
                if 'sources' not in existing:
                    existing['sources'] = []
                existing['sources'].append(trend.get('source', 'Unknown'))
            else:
                trend['sources'] = [trend.get('source', 'Unknown')]
                trend_dict[composite_key] = trend
        
        # Sort by momentum score
        aggregated = sorted(
            trend_dict.values(),
            key=lambda x: x.get('momentum_score', 0),
            reverse=True
        )
        
        return aggregated
    
    # ============ INSERT INTO DATABASE ============
    
    async def save_to_database(self, db_client, trends_data: Dict[str, Any]):
        """
        Save scraped trends to Supabase database
        """
        try:
            # Insert India-wide trends
            for trend in trends_data['india_trends']:
                data = {
                    'name': trend.get('keyword', trend.get('name', 'Unknown'))[:200],
                    'category': self._categorize_trend(trend.get('keyword', trend.get('name', ''))),
                    'status': 'trending' if trend.get('momentum_score', 0) > 60 else 'emerging',
                    'momentum_score': int(trend.get('momentum_score', 50)),
                    'description': f"Trending in India. Source: {', '.join(trend.get('sources', ['Unknown']))}",
                    'image_url': self._get_placeholder_image(trend.get('category', 'fashion')),
                    'search_volume': int(trend.get('avg_interest', 50)),
                    'growth_rate': float(trend.get('momentum_score', 50) - 50),
                    'season': self._get_current_season(),
                    'target_audience': 'India',
                    'confidence_score': min(int(trend.get('momentum_score', 50)), 95)
                }
                
                await db_client.table('trends').insert(data).execute()
            
            # Insert Tamil Nadu specific trends
            for trend in trends_data['tamilnadu_trends']:
                # Insert into trends table
                trend_data = {
                    'name': trend.get('keyword', trend.get('name', 'Unknown'))[:200],
                    'category': self._categorize_trend(trend.get('keyword', trend.get('name', ''))),
                    'status': 'trending' if trend.get('momentum_score', 0) > 60 else 'emerging',
                    'momentum_score': int(trend.get('momentum_score', 50)),
                    'description': f"Trending in Tamil Nadu. Source: {', '.join(trend.get('sources', ['Unknown']))}",
                    'image_url': self._get_placeholder_image(trend.get('category', 'fashion')),
                    'search_volume': int(trend.get('avg_interest', 50)),
                    'growth_rate': float(trend.get('momentum_score', 50) - 50),
                    'season': self._get_current_season(),
                    'target_audience': 'Tamil Nadu',
                    'confidence_score': min(int(trend.get('momentum_score', 50)), 95)
                }
                
                result = await db_client.table('trends').insert(trend_data).execute()
                
                # Also insert into regional_trends table
                if result.data:
                    trend_id = result.data[0]['id']
                    regional_data = {
                        'trend_id': trend_id,
                        'country': 'India',
                        'country_code': 'IN',
                        'state': 'Tamil Nadu',
                        'city': 'Chennai',
                        'momentum_score': int(trend.get('momentum_score', 50)),
                        'demand_level': 'high' if trend.get('momentum_score', 0) > 70 else 'medium',
                        'growth_velocity': float(trend.get('momentum_score', 50) - 50),
                        'local_preferences': f"Popular in Tamil Nadu region",
                        'top_category': self._categorize_trend(trend.get('keyword', trend.get('name', '')))
                    }
                    
                    await db_client.table('regional_trends').insert(regional_data).execute()
            
            logger.info(f"✅ Saved {len(trends_data['trends'])} trends to database")
            return {'success': True, 'saved_count': len(trends_data['trends'])}
            
        except Exception as e:
            logger.error(f"Database save error: {e}")
            return {'success': False, 'error': str(e)}
    
    def _categorize_trend(self, name: str) -> str:
        """Categorize trend based on keywords"""
        name_lower = name.lower()
        
        if any(word in name_lower for word in ['saree', 'lehenga', 'kurti', 'salwar', 'ethnic']):
            return 'Ethnic Wear'
        elif any(word in name_lower for word in ['jeans', 'dress', 'top', 'western']):
            return 'Western Wear'
        elif any(word in name_lower for word in ['silk', 'cotton', 'khadi', 'chanderi']):
            return 'Fabrics'
        elif any(word in name_lower for word in ['jewellery', 'accessories']):
            return 'Accessories'
        else:
            return 'Fashion'
    
    def _get_placeholder_image(self, category: str) -> str:
        """Get placeholder image URL"""
        return f"https://source.unsplash.com/400x300/?{category.lower().replace(' ', '-')},fashion"
    
    def _get_current_season(self) -> str:
        """Get current season for India"""
        month = datetime.now().month
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Summer'
        elif month in [6, 7, 8, 9]:
            return 'Monsoon'
        else:
            return 'Autumn'


# ============ USAGE EXAMPLE ============

async def main():
    """Example usage"""
    scraper = IndiaFashionScraper()
    
    # Scrape all India data
    results = await scraper.scrape_all_india_sources()
    
    print(f"\n🇮🇳 India Fashion Trends: {results['india_count']}")
    for trend in results['india_trends'][:10]:
        name = trend.get('keyword', trend.get('name', 'Unknown'))
        score = trend.get('momentum_score', 0)
        print(f"  - {name} (Score: {score:.0f})")
    
    print(f"\n📍 Tamil Nadu Fashion Trends: {results['tamilnadu_count']}")
    for trend in results['tamilnadu_trends'][:10]:
        name = trend.get('keyword', trend.get('name', 'Unknown'))
        score = trend.get('momentum_score', 0)
        print(f"  - {name} (Score: {score:.0f})")


if __name__ == "__main__":
    asyncio.run(main())
