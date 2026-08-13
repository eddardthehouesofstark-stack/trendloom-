# 🇮🇳 Import Real India & Tamil Nadu Fashion Data

## 🎉 Congratulations!

Your database is connected! Now let's fill it with **REAL fashion trend data** specifically for **India and Tamil Nadu**.

---

## 📊 What Data You'll Get

### India (National Level)
- **40+ fashion keywords** tracked via Google Trends
- **Ethnic wear**: Sarees, kurtis, lehengas, salwar kameez
- **Western wear**: Jeans, crop tops, maxi dresses, jumpsuits
- **Fabrics**: Cotton, silk, khadi, chanderi, banarasi
- **Trending styles**: Fusion wear, sustainable fashion, handloom
- **E-commerce data**: Myntra, Ajio, Flipkart trending items

### Tamil Nadu (State Level)
- **Regional specialties**: Kanchipuram sarees, pattu sarees
- **Local fabrics**: Madurai cotton, Kovai kora, Salem silk
- **Traditional wear**: Chettinad cotton, temple jewellery
- **South Indian fashion** specific trends

### Data Sources (All FREE!)
✅ **Google Trends India** - Search volume & momentum  
✅ **Myntra** - India's top fashion e-commerce  
✅ **Ajio** - Reliance fashion platform  
✅ **Flipkart Fashion** - E-commerce trends  

**No API keys required!** Everything uses free public data.

---

## 🚀 QUICK START (3 Steps)

### Step 1: Install Google Trends Library (1 minute)

```powershell
# Navigate to project root
cd "d:\projects\srcas hackathon"

# Install pytrends (Google Trends - FREE, no API key!)
pip install pytrends
```

That's it! No API keys, no authentication needed! 🎉

---

### Step 2: Run Import Script (2-3 minutes)

```powershell
# Navigate to backend folder
cd backend

# Run the import script
python import_india_data.py
```

**You'll see:**
```
============================================================
TRENDLOOM - INDIA DATA IMPORTER
============================================================

Choose an option:
1. Import data into database (Full import)
2. Test scraper only (No database changes)
3. Exit

Enter choice (1-3):
```

**Choose option 1** for full import.

---

### Step 3: Confirm and Import (30 seconds)

The script will:
1. ✅ Fetch data from Google Trends (India & Tamil Nadu)
2. ✅ Scrape Myntra, Ajio, Flipkart
3. ✅ Show you the top trends found
4. ⏸️ Ask for confirmation before importing

**Example output:**
```
🔥 TOP INDIA TRENDS:
   1. saree                        Score:  85.2 [Google Trends India]
   2. kurti                        Score:  78.5 [Google Trends India, Myntra]
   3. ethnic wear                  Score:  76.3 [Google Trends India]
   4. sustainable fashion india    Score:  72.1 [Google Trends India]
   5. fusion wear                  Score:  68.9 [Myntra, Ajio]

📍 TOP TAMIL NADU TRENDS:
   1. kanchipuram saree           Score:  92.3 [Google Trends Tamil Nadu]
   2. pattu saree                 Score:  87.5 [Google Trends Tamil Nadu]
   3. temple jewellery            Score:  75.2 [Google Trends Tamil Nadu]
   4. chettinad cotton            Score:  70.8 [Google Trends Tamil Nadu]

============================================================
📥 Import this data into database? (yes/no):
```

Type **yes** and press Enter!

---

## ✅ What Gets Imported

### Database Tables Updated:

**1. `trends` table** - Main trends
- India national trends (40+ items)
- Tamil Nadu specific trends (10+ items)
- With momentum scores, categories, descriptions

**2. `regional_trends` table** - Location data
- Tamil Nadu trends with regional details
- Demand levels (high/medium/low)
- Growth velocity
- Local preferences

### Example Data Imported:

```json
{
  "name": "Kanchipuram Saree",
  "category": "Ethnic Wear",
  "status": "trending",
  "momentum_score": 92,
  "description": "Trending in Tamil Nadu. Source: Google Trends Tamil Nadu",
  "country": "India",
  "region": "Tamil Nadu",
  "search_volume": 87,
  "growth_rate": 42.3,
  "season": "Festival",
  "confidence_score": 92
}
```

---

## 🎨 See Your Data Live

After import is complete:

### Frontend Dashboard
Visit your Vercel URL and see:
- **Dashboard**: Real India fashion trends with momentum scores
- **Regional Page**: Select India → Tamil Nadu to see localized trends
- **Seasonal Page**: India-specific seasonal trends

### Backend API
Test your new data:

```bash
# All trends (includes India data)
https://trendloom-3aux.onrender.com/api/trends/

# Filter Tamil Nadu trends
https://trendloom-3aux.onrender.com/api/regional/trends?country_code=in&state=Tamil%20Nadu

# India KPIs
https://trendloom-3aux.onrender.com/api/trends/kpis
```

### Supabase Dashboard
1. Go to https://app.supabase.com
2. Open your `trendloom` project
3. Click **Table Editor**
4. View `trends` and `regional_trends` tables
5. See your real India data! 🎉

---

## 🔄 Update Data Regularly

### Option 1: Manual Updates

Run the import script whenever you want fresh data:

```powershell
cd backend
python import_india_data.py
```

Recommended: **Weekly** or before major fashion seasons.

### Option 2: Automated Daily Updates

Add this to your scheduler (future enhancement):

```python
# In app/services/scheduler.py
from app.services.india_data_scraper import IndiaFashionScraper

scheduler.add_job(
    func=import_india_data,
    trigger='cron',
    hour=2,  # Run at 2 AM daily
    id='india_data_refresh'
)
```

---

## 🧪 Test Before Full Import

Want to see what data you'll get **without** importing?

```powershell
cd backend
python import_india_data.py
```

Choose **option 2** (Test scraper only)

This will:
- ✅ Fetch all data
- ✅ Show you the results
- ❌ NOT save to database

Perfect for testing!

---

## 🛠️ Troubleshooting

### Issue: "pytrends not installed"

**Solution:**
```powershell
pip install pytrends
```

### Issue: "Too many requests" from Google

**Solution:**
Google Trends has rate limits. The script includes automatic delays, but if you see this:
- Wait 5-10 minutes
- Run the script again
- It will pick up where it left off

### Issue: "Database connection failed"

**Solution:**
1. Check Supabase credentials in Render environment variables
2. Verify you completed the database setup
3. Test: https://trendloom-3aux.onrender.com/health

### Issue: "No data found for Tamil Nadu"

**Possible causes:**
- Some keywords may have low search volume
- Google Trends requires sufficient data
- Try running again in a few hours

**Workaround:**
The script will still import India-wide trends successfully.

### Issue: E-commerce scraping fails

**Don't worry!**
- Google Trends data is the most important (and most reliable)
- E-commerce sites often block scrapers
- You'll still get 40+ trends from Google Trends alone
- The script continues even if some sources fail

---

## 📊 Data Quality

### Momentum Scores Explained:

| Score | Meaning | Status |
|-------|---------|--------|
| **90-100** | Extremely hot trend | Trending |
| **70-89** | Strong trend | Trending |
| **50-69** | Growing trend | Emerging |
| **30-49** | Moderate interest | Stable |
| **0-29** | Declining trend | Declining |

### Data Freshness:

- **Google Trends**: Last 3 months of data
- **E-commerce**: Current listings (daily)
- **Update frequency**: Run script weekly for best results

---

## 🎯 Customize for Your Needs

### Add More Keywords

Edit `backend/app/services/india_data_scraper.py`:

```python
self.indian_fashion_keywords = [
    # Add your keywords here
    'your custom keyword',
    'another trend to track',
]

self.tamilnadu_keywords = [
    # Add Tamil Nadu specific keywords
    'chennai fashion',
    'coimbatore fashion',
]
```

### Track Other States

Replace `'IN-TN'` with other state codes:

- **Karnataka**: `'IN-KA'`
- **Maharashtra**: `'IN-MH'`
- **Delhi**: `'IN-DL'`
- **Gujarat**: `'IN-GJ'`
- **West Bengal**: `'IN-WB'`

### Change Time Range

In `india_data_scraper.py`:

```python
# Current: Last 3 months
timeframe='today 3-m'

# Options:
timeframe='today 1-m'   # Last month
timeframe='today 6-m'   # Last 6 months
timeframe='today 12-m'  # Last year
```

---

## 💡 Pro Tips

### 1. Best Time to Import
- **Before festivals**: Diwali, Pongal, Onam seasons
- **Fashion weeks**: India Fashion Week, Lakme Fashion Week
- **Monday mornings**: Fresh weekend shopping data

### 2. Combine with Manual Research
- Add specific designer collections manually
- Track local boutique trends
- Include customer feedback data

### 3. Validate the Data
- Cross-reference with actual sales
- Check social media buzz
- Verify with fashion magazines

### 4. Export for Analysis
Use Supabase to export data:
```sql
-- Export Tamil Nadu trends
SELECT * FROM regional_trends 
WHERE state = 'Tamil Nadu' 
ORDER BY momentum_score DESC;
```

---

## 📈 Expected Results

After importing, you should see:

### Dashboard Page
✅ **40-50 trending items** from India  
✅ **Top categories**: Ethnic Wear, Western Wear, Fabrics  
✅ **Momentum scores**: 60-95 range  
✅ **Real search volumes** from Google Trends  

### Regional Page
✅ **India** in country selector  
✅ **Tamil Nadu** in state selector  
✅ **10-15 Tamil Nadu specific trends**  
✅ **Regional data cards** with growth metrics  

### API Endpoints
✅ All endpoints return real India data  
✅ Regional filtering works  
✅ Momentum scores are accurate  
✅ Categories are properly assigned  

---

## 🎉 Success Checklist

After running the import script:

- [ ] Installed pytrends (`pip install pytrends`)
- [ ] Ran import script (`python import_india_data.py`)
- [ ] Chose option 1 (Full import)
- [ ] Saw 40+ trends listed
- [ ] Confirmed import (typed "yes")
- [ ] Import succeeded
- [ ] Checked Supabase Table Editor (data visible)
- [ ] Tested API endpoint (returns India data)
- [ ] Viewed dashboard (shows real trends)
- [ ] Checked regional page (Tamil Nadu data visible)

---

## 🚀 Next Steps

After successful import:

### Immediate (Today)
1. ✅ Test all frontend pages
2. ✅ Verify data accuracy
3. ✅ Share with your team

### This Week
1. Add more Indian fashion keywords
2. Customize categories for your use case
3. Set up weekly data refresh

### This Month
1. Add automated daily updates
2. Track additional states (Karnataka, Maharashtra)
3. Integrate Instagram India data
4. Add competitor analysis (Indian brands)

---

## 📞 Need Help?

### Common Questions

**Q: Do I need to pay for Google Trends API?**  
A: No! pytrends is completely FREE. No API key, no payment.

**Q: How often should I update the data?**  
A: Weekly is good. Daily for high-volume seasons.

**Q: Can I track other countries?**  
A: Yes! Change `geo='IN'` to other country codes (US, UK, etc.)

**Q: What if scraping fails?**  
A: Google Trends still works and gives you 40+ trends. That's the core!

**Q: Is this legal?**  
A: Yes! Google Trends is public data. E-commerce scraping follows robots.txt.

---

## 🎯 Summary

**Time Required**: 5 minutes  
**Cost**: $0 (completely free)  
**Data Points**: 50+ fashion trends  
**Sources**: 4 (Google, Myntra, Ajio, Flipkart)  
**Regions**: India + Tamil Nadu  
**Update Frequency**: Weekly recommended  

**One command:**
```powershell
cd backend && python import_india_data.py
```

**Result:** Real Indian fashion intelligence! 🇮🇳🎉

---

Last Updated: August 13, 2026  
Status: Ready to import 🚀

