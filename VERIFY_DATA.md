# ✅ Verify India Data is Working

## 🔍 **Step-by-Step Verification Guide**

---

## **Step 1: Check Database (Supabase)**

### ✅ Verify Data is in Database:

1. Go to **https://app.supabase.com**
2. Open your **trendloom** project
3. Click **Table Editor** (left sidebar)

**Check `trends` table:**
- Should have **25+ rows** with India trends
- Look for: "Ethnic Wear", "Saree", "Kurti", etc.
- Check `momentum_score` column has values (75-155)
- Check `source` column says "Google Trends India"

**Check `regional_trends` table:**
- Should have **10+ rows** with Tamil Nadu trends
- Look for: "Kanchipuram Saree", "Pattu Saree", etc.
- Check `country_code` = "IN"
- Check `state_code` = "TN"

✅ **If data is there: Database is good! Move to Step 2**  
❌ **If no data: Re-import the SQL file**

---

## **Step 2: Check Backend API (Render)**

### ✅ Test Backend Health:

**Option A: Open in Browser**

Visit these URLs (wait 30 seconds if backend is sleeping):

```
1. https://trendloom-3aux.onrender.com/
   Expected: {"status": "online", "service": "TrendLoom API", ...}

2. https://trendloom-3aux.onrender.com/health
   Expected: {"status": "healthy", "database": "connected", ...}

3. https://trendloom-3aux.onrender.com/api/trends/
   Expected: JSON array with trends data
```

**Option B: Use PowerShell**

```powershell
# Test root endpoint
Invoke-WebRequest -Uri "https://trendloom-3aux.onrender.com/" | Select-Object -ExpandProperty Content

# Test trends endpoint
Invoke-WebRequest -Uri "https://trendloom-3aux.onrender.com/api/trends/" | Select-Object -ExpandProperty Content
```

---

### ⚠️ **If Backend Returns "Not Found" or Errors:**

#### **Issue 1: Backend Sleeping (Free Tier)**
**Symptom:** First request fails, second works  
**Solution:** Wait 30-60 seconds, try again  
**Why:** Free tier sleeps after 15 min inactivity

#### **Issue 2: Backend Not Deployed**
**Check Render Dashboard:**
1. Go to **https://dashboard.render.com**
2. Click your **trendloom-3aux** service
3. Check **Events** tab - should show "Deploy succeeded"
4. Check **Logs** tab - look for errors

**If deploy failed:**
- Look for Python errors in logs
- Missing dependencies? Update requirements.txt
- Supabase credentials set? Check Environment variables

#### **Issue 3: Wrong Backend URL**
**Verify URL:**
- Check Render dashboard for actual URL
- Should be: `https://trendloom-3aux.onrender.com`
- Update `frontend/js/api.js` if different

---

## **Step 3: Check Frontend Connection**

### ✅ Test Frontend API Client:

1. **Open your Vercel URL** (or local: `http://localhost:5500/dashboard.html`)
2. **Press F12** to open Browser Console
3. **Look for these messages:**

```
✅ Good:
   "🔌 TrendLoom API Client loaded"
   "📊 Loading dashboard data..."
   "✅ Dashboard data loaded successfully"

❌ Bad:
   "CORS error"
   "Failed to fetch"
   "404 Not Found"
   "Network error"
```

---

### ⚠️ **If Frontend Shows Errors:**

#### **Issue 1: API URL Wrong**

**Check:** `frontend/js/api.js`

```javascript
const API_CONFIG = {
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://trendloom-3aux.onrender.com',  // ← Must match Render URL
    timeout: 10000
};
```

**Fix:** Update URL to match your Render service

---

#### **Issue 2: CORS Error**

**Symptom:** Console shows `Access to fetch blocked by CORS policy`

**Fix:** Update `backend/main.py` CORS origins:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-actual-vercel-url.vercel.app",  # ← Add your Vercel URL
        "http://localhost:5500",
        "*"  # Remove in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then commit and push to redeploy.

---

#### **Issue 3: Cache Issue**

**Fix:**
- Hard refresh: **Ctrl + Shift + R**
- Clear browser cache
- Try incognito window
- Add `?v=2` to URL: `https://your-site.vercel.app/dashboard.html?v=2`

---

## **Step 4: Verify Data is Displaying**

### ✅ **Dashboard Page:**

**What to check:**
- [ ] Trending cards show India trends (Saree, Kurti, etc.)
- [ ] Momentum scores are visible (75-155 range)
- [ ] Images are loading
- [ ] Categories are correct (Ethnic Wear, Western Wear, etc.)
- [ ] KPI cards show real numbers

**If showing old/sample data:**
- Hard refresh (Ctrl + Shift + R)
- Check browser console for errors
- Verify API returns new data

---

### ✅ **Regional Page:**

**What to check:**
1. Open `/regional.html`
2. **Country dropdown** → Should have "India"
3. Select "India"
4. **State dropdown** → Should have "Tamil Nadu"
5. Select "Tamil Nadu"
6. Should display **10 Tamil Nadu trends**:
   - Kanchipuram Saree
   - Pattu Saree
   - Temple Jewellery
   - etc.

**If not showing:**
- Check API: `https://trendloom-3aux.onrender.com/api/regional/trends?country_code=in`
- Should return Tamil Nadu trends in JSON

---

## **Quick Diagnostic Commands:**

### **Test Everything at Once:**

```powershell
# 1. Test backend root
Write-Host "`n1. Testing backend root..." -ForegroundColor Yellow
try { (Invoke-WebRequest "https://trendloom-3aux.onrender.com/").Content } catch { "❌ Failed: $($_.Exception.Message)" }

# 2. Test health endpoint
Write-Host "`n2. Testing health endpoint..." -ForegroundColor Yellow
try { (Invoke-WebRequest "https://trendloom-3aux.onrender.com/health").Content } catch { "❌ Failed: $($_.Exception.Message)" }

# 3. Test trends endpoint
Write-Host "`n3. Testing trends endpoint..." -ForegroundColor Yellow
try { (Invoke-WebRequest "https://trendloom-3aux.onrender.com/api/trends/").Content | ConvertFrom-Json | Select -First 3 } catch { "❌ Failed: $($_.Exception.Message)" }

# 4. Test regional endpoint
Write-Host "`n4. Testing regional endpoint..." -ForegroundColor Yellow
try { (Invoke-WebRequest "https://trendloom-3aux.onrender.com/api/regional/countries").Content } catch { "❌ Failed: $($_.Exception.Message)" }

Write-Host "`n✅ Diagnostic complete!" -ForegroundColor Green
```

Copy and paste this entire block into PowerShell!

---

## **Common Issues & Solutions:**

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Backend Sleeping** | First request fails | Wait 30 seconds, retry |
| **Wrong URL** | 404 errors | Check Render dashboard for actual URL |
| **CORS Error** | Blocked by CORS policy | Add Vercel URL to CORS origins |
| **No Data** | Empty arrays | Re-import SQL to Supabase |
| **Old Data** | Sample data still showing | Hard refresh (Ctrl+Shift+R) |
| **Deploy Failed** | 404 on all endpoints | Check Render logs, fix errors |
| **Credentials Missing** | Database connection failed | Set SUPABASE_* env vars in Render |

---

## **Still Not Working?**

### **Check Render Logs:**

1. Go to **https://dashboard.render.com**
2. Click **trendloom-3aux** service
3. Click **Logs** tab
4. Look for:
   - ✅ "TrendLoom API is ready!"
   - ✅ "Database connection established"
   - ❌ Python errors
   - ❌ "ModuleNotFoundError"
   - ❌ "Connection refused"

### **Manual Redeploy:**

1. In Render dashboard
2. Click **"Manual Deploy"**
3. Select **"Clear build cache & deploy"**
4. Wait 5 minutes
5. Test again

---

## **Success Checklist:**

After following these steps, you should have:

- [ ] ✅ Data visible in Supabase tables
- [ ] ✅ Backend API responds with JSON
- [ ] ✅ `/api/trends/` returns India trends
- [ ] ✅ Frontend console shows no errors
- [ ] ✅ Dashboard displays India fashion trends
- [ ] ✅ Regional page shows Tamil Nadu trends
- [ ] ✅ Images are loading
- [ ] ✅ Momentum scores are visible

---

## **🎯 Expected Results:**

### **Backend API Response:**

```json
[
  {
    "id": 1,
    "name": "Ethnic Wear",
    "category": "Ethnic Wear",
    "momentum_score": 155,
    "status": "trending",
    "description": "Trending in India. Based on Google Trends...",
    "image_url": "https://source.unsplash.com/...",
    "source": "Google Trends India",
    "created_at": "2026-08-13T...",
    "updated_at": "2026-08-13T..."
  },
  ...
]
```

### **Frontend Display:**

**Dashboard:**
- Cards showing: "Ethnic Wear (155)", "Saree (148)", "Kurti (142)"
- Indian fashion images
- Real momentum scores

**Regional Page:**
- India → Tamil Nadu → Shows "Kanchipuram Saree", "Pattu Saree", etc.

---

## **Need More Help?**

If you're still having issues after following this guide:

1. **Share the error message** from browser console
2. **Share Render logs** (last 50 lines)
3. **Confirm which step fails** (Database? Backend? Frontend?)

Then I can provide specific fixes! 🔧

---

Last Updated: August 13, 2026  
Status: Comprehensive verification guide ✅

