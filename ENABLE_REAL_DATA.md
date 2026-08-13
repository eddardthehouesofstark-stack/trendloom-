# 🌍 Enable Real-World Fashion Data

## Current State vs Real Data

### ✅ What's Already Working
- **Infrastructure**: 100% complete and functional
- **API Endpoints**: All working perfectly
- **Database**: Structure ready for real data
- **Frontend Integration**: Connects to backend
- **Scheduled Jobs**: Auto-runs every 6 hours

### 📊 What's Currently Mock Data
- Trend scores (hardcoded numbers)
- Regional trends (sample data)
- Competitor info (placeholder)
- KPIs (static values)
- Seasonal forecasts (examples)

---

## 🚀 How to Enable Real Data (3 Options)

### Option 1: Quick Start with Google Trends (30 min)

**Install Dependencies:**
```bash
pip install pytrends instaloader
```

**Update requirements.txt:**
```txt
pytrends==4.9.2
instaloader==4.11
```

**Use the Real Data Scraper:**
```python
# In backend/app/services/scheduler.py
from app.services.real_data_scraper import RealFashionDataScraper

async def scrape_trends_job():
    """Job to scrape REAL trend data"""
    logger.info("🔄 Running REAL data scraping...")
    
    scraper = RealFashionDataScraper()
    results = await scraper.scrape_all_sources()
    
    if results['success']:
        # Save to database
        for trend in results['trends']:
            TrendDB.create_trend({
                'name': trend['name'],
                'category': trend.get('category', 'General'),
                'momentum_score': trend['momentum_score'],
                'status': 'trending' if trend['momentum_score'] > 70 else 'active',
                'source': ', '.join(trend['sources'])
            })
    
    logger.info(f"✅ Saved {len(results['trends'])} real trends to database")
```

**This gives you:**
- ✅ Google Trends data (search volume)
- ✅ Instagram hashtag counts
- ✅ Basic web scraping from fashion sites

---

### Option 2: Full Integration with APIs (2-3 hours)

#### 1. Google Trends API (Free)
```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

# Track fashion keywords
keywords = [
    'oversized blazer',
    'wide leg trousers', 
    'cottagecore aesthetic',
    'y2k fashion',
    'sustainable fashion'
]

pytrends.build_payload(keywords, timeframe='today 3-m')
trends_data = pytrends.interest_over_time()
```

#### 2. Instagram Graph API (Requires Business Account)
```python
# Setup:
# 1. Create Facebook Developer account
# 2. Create app and get access token
# 3. Connect Instagram Business account

import requests

def get_instagram_hashtag_data(hashtag, access_token):
    url = f"https://graph.facebook.com/v18.0/ig_hashtag_search"
    params = {
        'user_id': 'YOUR_IG_USER_ID',
        'q': hashtag,
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()
```

#### 3. Fashion API Services

**A) ShopStyle API (E-commerce trends)**
- Sign up: https://www.shopstyle.com/api
- Free tier: 5,000 requests/month
```python
import requests

def get_trending_products():
    url = "https://api.shopstyle.com/api/v2/products"
    params = {
        'pid': 'YOUR_PARTNER_ID',
        'fts': 'trending',
        'cat': 'womens-clothes'
    }
    return requests.get(url, params=params).json()
```

**B) Pinterest Trends API**
- Sign up: https://developers.pinterest.com
```python
def get_pinterest_trends(keyword):
    url = f"https://api.pinterest.com/v5/search/pins"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'query': keyword, 'limit': 50}
    return requests.get(url, headers=headers, params=params).json()
```

---

### Option 3: AI-Powered Analysis (Advanced)

#### OpenAI for Trend Analysis
```python
from openai import OpenAI

client = OpenAI(api_key='your-api-key')

def analyze_fashion_trends(scraped_data):
    """Use GPT-4 to analyze and score fashion trends"""
    
    prompt = f"""
    Analyze these fashion trends and provide momentum scores (0-100):
    
    {json.dumps(scraped_data, indent=2)}
    
    For each trend, provide:
    1. Momentum score (0-100)
    2. Category (Tailoring, Knitwear, etc.)
    3. Status (trending, stable, declining)
    4. Reasoning (why this score)
    
    Return JSON format.
    """
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)
```

---

## 📊 Data Sources Comparison

| Source | Cost | Setup Time | Data Quality | Rate Limits |
|--------|------|------------|--------------|-------------|
| **Google Trends** | Free | 10 min | High | None |
| **Instagram (instaloader)** | Free | 15 min | Medium | ~500/hr |
| **Web Scraping** | Free | 30 min | Medium | Varies |
| **ShopStyle API** | Free tier | 20 min | High | 5K/month |
| **Pinterest API** | Free | 30 min | High | 1K/day |
| **Instagram Graph API** | Free | 1 hour | High | 200/hr |
| **OpenAI GPT-4** | $0.01/1K tokens | 10 min | Very High | High |

---

## 🔧 Step-by-Step: Enable Google Trends (Easiest)

### Step 1: Install Library
```bash
pip install pytrends
```

### Step 2: Update Scraper
Replace `backend/app/services/scraper.py` with:

```python
from pytrends.request import TrendReq
from app.database import TrendDB
import logging

logger = logging.getLogger(__name__)

def scrape_real_trends():
    """Scrape REAL Google Trends data"""
    
    # Initialize Google Trends
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Fashion keywords to track
    keywords = [
        'oversized blazer',
        'wide leg trousers',
        'sheer fabric',
        'cottagecore',
        'y2k fashion',
        'sustainable fashion',
        'minimalist style',
        'dopamine dressing'
    ]
    
    trends = []
    
    # Process keywords in batches of 5 (Google Trends limit)
    for i in range(0, len(keywords), 5):
        batch = keywords[i:i+5]
        
        try:
            # Build payload
            pytrends.build_payload(batch, timeframe='today 3-m')
            
            # Get interest over time
            interest_data = pytrends.interest_over_time()
            
            if not interest_data.empty:
                for keyword in batch:
                    if keyword in interest_data.columns:
                        avg_score = float(interest_data[keyword].mean())
                        
                        # Save to database
                        TrendDB.create_trend({
                            'name': keyword.title(),
                            'category': 'Fashion',
                            'momentum_score': avg_score,
                            'status': 'trending' if avg_score > 50 else 'stable',
                            'source': 'Google Trends'
                        })
                        
                        trends.append({
                            'name': keyword,
                            'score': avg_score
                        })
                        
                        logger.info(f"✅ {keyword}: {avg_score:.1f}")
        
        except Exception as e:
            logger.error(f"Error processing batch {batch}: {e}")
            continue
    
    return {
        'count': len(trends),
        'trends': trends,
        'source': 'Google Trends (Real Data)'
    }
```

### Step 3: Update Scheduler
```python
# In backend/app/services/scheduler.py
from app.services.scraper import scrape_real_trends

def scrape_trends_job():
    """Scheduled job to scrape real trends"""
    logger.info("🔄 Scraping REAL fashion trends...")
    
    result = scrape_real_trends()
    
    logger.info(f"✅ Updated {result['count']} trends from {result['source']}")
```

### Step 4: Test It
```bash
cd backend
python -c "from app.services.scraper import scrape_real_trends; print(scrape_real_trends())"
```

You should see REAL Google Trends scores! 🎉

---

## 🌐 Data Flow with Real Data

```
┌─────────────────────────────────────────┐
│   Real-World Data Sources               │
│  • Google Trends (search volume)        │
│  • Instagram (hashtag counts)           │
│  • Zara/H&M (product launches)          │
│  • Vogue/BoF (editorial trends)         │
└──────────────┬──────────────────────────┘
               │
               ↓ Scraping (Every 6 hours)
┌──────────────────────────────────────────┐
│   Backend Scraper                        │
│  • Fetches latest data                   │
│  • Calculates momentum scores            │
│  • Aggregates from multiple sources      │
└──────────────┬───────────────────────────┘
               │
               ↓ Saves to Database
┌──────────────────────────────────────────┐
│   Supabase Database                      │
│  • trends table                          │
│  • regional_trends table                 │
│  • Updated every 6 hours                 │
└──────────────┬───────────────────────────┘
               │
               ↓ API Queries
┌──────────────────────────────────────────┐
│   FastAPI Backend                        │
│  • Serves fresh data via endpoints       │
│  • /api/trends/trending                  │
└──────────────┬───────────────────────────┘
               │
               ↓ HTTP Requests
┌──────────────────────────────────────────┐
│   Frontend Dashboard                     │
│  • Displays REAL trend data              │
│  • Auto-refreshes every 5 minutes        │
└──────────────────────────────────────────┘
```

---

## 📈 Recommended Real Data Sources

### Tier 1: Free & Easy (Start Here)
1. ✅ **Google Trends** - Search volume data
2. ✅ **Instagram (instaloader)** - Hashtag counts  
3. ✅ **Web Scraping** - Vogue, BoF articles

### Tier 2: APIs (Better Quality)
4. **ShopStyle API** - E-commerce trends
5. **Pinterest Trends** - Visual trend data
6. **TikTok Creative Center** - Viral fashion trends

### Tier 3: Premium (Best Quality)
7. **WGSN API** - Professional trend forecasting ($$$)
8. **Edited API** - Retail analytics ($$$)
9. **OpenAI GPT-4** - AI-powered analysis ($)

---

## 🎯 Quick Win: Enable Real Data in 30 Minutes

```bash
# 1. Install dependencies
pip install pytrends instaloader

# 2. Update requirements.txt
echo "pytrends==4.9.2" >> requirements.txt
echo "instaloader==4.11" >> requirements.txt

# 3. Copy real_data_scraper.py
# (Already created in your backend/app/services/ folder)

# 4. Update scheduler.py to use real scraper
# Replace scrape_trends_job() with real data version

# 5. Test it
cd backend
python main.py

# 6. Check database
# Go to Supabase → Table Editor → trends
# You should see real Google Trends data!
```

---

## ✅ Verification Checklist

After enabling real data, verify:

- [ ] Google Trends scores are different each day
- [ ] Instagram hashtag counts update
- [ ] Database shows `source: 'Google Trends'`
- [ ] Frontend displays updated scores
- [ ] Scheduler runs every 6 hours
- [ ] Logs show "✅ Saved X real trends to database"

---

## 🚨 Important Notes

### Legal & Ethical Scraping
- ✅ Respect robots.txt files
- ✅ Add delays between requests (rate limiting)
- ✅ Use official APIs when available
- ✅ Don't overwhelm servers
- ⚠️ Some sites prohibit scraping in ToS

### Rate Limits
- Google Trends: No hard limit, but use responsibly
- Instagram: ~500 requests/hour
- E-commerce sites: Add 2-3 second delays

### API Keys Needed
- Instagram Graph API: Free (requires Facebook Developer account)
- ShopStyle API: Free tier (5K requests/month)
- OpenAI: Paid ($0.01/1K tokens for GPT-4)

---

## 📞 Need Help?

**Check these first:**
1. Is `pytrends` installed? Run: `pip list | grep pytrends`
2. Are scrapers running? Check logs: `python backend/main.py`
3. Is data saving? Check Supabase dashboard

**Common Issues:**
- **"pytrends not found"** → Run `pip install pytrends`
- **"Rate limit exceeded"** → Add delays in scraper
- **"No data returned"** → Check internet connection

---

## 🎉 Summary

**Current State:**
- Infrastructure: 100% ready ✅
- Data: Mock/sample data 📊

**To Enable Real Data:**
1. Install pytrends (2 min)
2. Use real_data_scraper.py (included!)
3. Update scheduler.py (5 min)
4. Test and verify (10 min)

**Total Time: 30 minutes** ⏱️

Your TrendLoom platform will then use REAL Google Trends data, Instagram hashtag counts, and web-scraped fashion articles! 🚀
