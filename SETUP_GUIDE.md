# 🚀 TrendLoom Complete Setup Guide

## Complete Real-Time Fashion Intelligence Platform
**Frontend (HTML/CSS/JS) + Backend (FastAPI) + Database (Supabase)**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Supabase Setup](#supabase-setup)
3. [Backend Setup](#backend-setup)
4. [Frontend Setup](#frontend-setup)
5. [Deployment](#deployment)
6. [Testing](#testing)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software
- **Python 3.9+** ([download](https://www.python.org/downloads/))
- **Git** ([download](https://git-scm.com/downloads))
- **Code Editor** (VS Code recommended)
- **Modern Browser** (Chrome, Firefox, Edge)

### Required Accounts
- **Supabase** - [supabase.com](https://supabase.com) (Free tier available)
- **GitHub** - [github.com](https://github.com) (Already set up ✅)
- **Vercel** - [vercel.com](https://vercel.com) (For frontend)
- **Render.com** - [render.com](https://render.com) (For backend - free tier)

---

## 🗄️ Supabase Setup (Database)

### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Click **"New Project"**
3. Fill in:
   - **Name**: `trendloom`
   - **Database Password**: (Save this somewhere safe!)
   - **Region**: Choose closest to you
4. Click **"Create new project"** (takes ~2 minutes)

### Step 2: Run Database Schema

1. In your Supabase dashboard, go to **SQL Editor** (left sidebar)
2. Click **"New Query"**
3. Open `backend/supabase_schema.sql` from this project
4. Copy ALL the contents
5. Paste into Supabase SQL Editor
6. Click **"Run"** button
7. ✅ You should see "Success. No rows returned"

### Step 3: Get API Credentials

1. Go to **Settings** (gear icon) > **API**
2. Copy these values:
   - **Project URL** (looks like: `https://xxxxx.supabase.co`)
   - **anon/public key** (starts with `eyJ...`)
   - **service_role key** (starts with `eyJ...`)
3. Save these for the next step

---

## ⚙️ Backend Setup (FastAPI)

### Step 1: Install Python Dependencies

```powershell
# Navigate to project root
cd "d:\projects\srcas hackathon"

# Install requirements
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

1. Copy the example env file:
```powershell
copy .env.example .env
```

2. Open `.env` in your code editor
3. Fill in your Supabase credentials from previous step:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key_here
SUPABASE_SERVICE_KEY=your_service_role_key_here

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=development

# Frontend URLs
FRONTEND_URL=http://localhost:5500
VERCEL_URL=https://your-vercel-app.vercel.app
```

### Step 3: Test Backend Locally

```powershell
# Navigate to backend folder
cd backend

# Run the API
python main.py
```

You should see:
```
🚀 Starting TrendLoom API...
✅ Database connection established
✅ TrendLoom API is ready!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 4: Test API Endpoints

Open your browser and test:
- http://localhost:8000 (Health check)
- http://localhost:8000/docs (API documentation)
- http://localhost:8000/api/trends/ (Get trends)

---

## 🎨 Frontend Setup

### Step 1: Update API Configuration

1. Open `frontend/js/api.js`
2. Update the `API_CONFIG` object:

```javascript
const API_CONFIG = {
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://your-backend-api.render.com', // Update after backend deployment
    timeout: 10000
};
```

### Step 2: Add Script Tags to HTML Files

Add these lines before the closing `</body>` tag in each HTML file:

```html
<!-- API Client -->
<script src="js/api.js"></script>

<!-- Page-specific scripts -->
<script src="js/dashboard.js"></script> <!-- For dashboard.html -->
<script src="js/regional.js"></script> <!-- For regional.html -->
<!-- etc. -->
```

### Step 3: Test Frontend Locally

1. **Option A: VS Code Live Server**
   - Install "Live Server" extension in VS Code
   - Right-click `dashboard.html` > "Open with Live Server"

2. **Option B: Python Simple Server**
   ```powershell
   cd frontend
   python -m http.server 5500
   ```
   - Open http://localhost:5500/dashboard.html

3. **Option C: Direct File**
   - Just double-click `dashboard.html`

### Step 4: Check Console

1. Open browser DevTools (F12)
2. Go to **Console** tab
3. You should see:
   - `🔌 TrendLoom API Client loaded`
   - `📊 Loading dashboard data...`
   - `✅ Dashboard data loaded successfully`

---

## 🚀 Deployment

### Deploy Backend to Render.com

1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click **"New +" > "Web Service"**
4. Connect your GitHub repository: `trendloom-`
5. Configure:
   - **Name**: `trendloom-api`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r ../requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add **Environment Variables**:
   - `SUPABASE_URL` = (your Supabase URL)
   - `SUPABASE_KEY` = (your anon key)
   - `SUPABASE_SERVICE_KEY` = (your service role key)
   - `ENVIRONMENT` = `production`
   - `VERCEL_URL` = `https://your-app.vercel.app` (add after frontend deployment)
7. Click **"Create Web Service"**
8. Wait ~5 minutes for deployment
9. Copy your API URL (looks like: `https://trendloom-api.onrender.com`)

### Deploy Frontend to Vercel (Already Done ✅)

Your frontend is already on Vercel! Now update it:

1. Update `frontend/js/api.js`:
```javascript
const API_CONFIG = {
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://trendloom-api.onrender.com', // Your Render URL
    timeout: 10000
};
```

2. Commit and push:
```powershell
git add .
git commit -m "Connect frontend to backend API"
git push origin main
```

3. Vercel will auto-deploy (takes ~1 minute)

### Update CORS in Backend

1. Open `backend/main.py`
2. Update `allow_origins`:
```python
allow_origins=[
    "https://your-vercel-app.vercel.app",  # Your Vercel URL
    "http://localhost:5500",
    "*"  # Remove in production
],
```

3. Commit and push to trigger Render redeploy

---

## ✅ Testing

### Test Backend API

```powershell
# Health check
curl http://localhost:8000/health

# Get trends
curl http://localhost:8000/api/trends/

# Get KPIs
curl http://localhost:8000/api/trends/kpis
```

### Test Frontend Connection

1. Open dashboard in browser
2. Open DevTools Console (F12)
3. Run:
```javascript
// Test API connection
TrendLoomAPI.healthCheck().then(console.log)

// Get trends
TrendLoomAPI.getTrends().then(console.log)

// Get KPIs
TrendLoomAPI.getKPIs().then(console.log)
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem: `ModuleNotFoundError`**
```powershell
# Solution: Install dependencies
pip install -r requirements.txt
```

**Problem: Supabase connection fails**
- Check `.env` file has correct credentials
- Verify Supabase project is active
- Check if `supabase_schema.sql` was run

**Problem: Port 8000 already in use**
```powershell
# Solution: Use different port
uvicorn main:app --port 8001
```

### Frontend Issues

**Problem: CORS errors**
- Make sure backend is running
- Check `allow_origins` in `backend/main.py`
- Verify API URL in `frontend/js/api.js`

**Problem: API requests fail**
- Check backend is running: http://localhost:8000/health
- Check browser console for errors
- Verify API URL is correct

**Problem: Data not loading**
- Check browser console for errors
- Verify Supabase has data (run schema SQL)
- Test API endpoints directly: http://localhost:8000/docs

---

## 📊 Monitoring

### Backend Health
- API Health: `http://your-api.onrender.com/health`
- Render Logs: Dashboard > Logs tab
- Supabase: Dashboard > Database > Tables

### Frontend Performance
- Vercel Analytics: Dashboard > Analytics
- Browser DevTools: Network tab

---

## 🔐 Security Checklist

- [ ] `.env` file is in `.gitignore` (✅ Already done)
- [ ] API keys are not in frontend code
- [ ] CORS is restricted in production
- [ ] Supabase RLS policies enabled
- [ ] Rate limiting configured (add in production)

---

## 🎯 Next Steps

### Phase 1: Basic Real-Time (Current)
- ✅ Backend API running
- ✅ Frontend connected
- ✅ Mock data working

### Phase 2: Real Data Scraping
- [ ] Implement web scraping for fashion sites
- [ ] Add Google Trends integration
- [ ] Set up scheduled jobs

### Phase 3: AI Recommendations
- [ ] Integrate OpenAI API
- [ ] Train custom models
- [ ] Add sentiment analysis

### Phase 4: Advanced Features
- [ ] User authentication
- [ ] Saved trends & favorites
- [ ] Email alerts
- [ ] Export reports

---

## 📚 Documentation Links

- **FastAPI**: https://fastapi.tiangolo.com
- **Supabase**: https://supabase.com/docs
- **Vercel**: https://vercel.com/docs
- **Render**: https://render.com/docs

---

## 💡 Quick Start Summary

```powershell
# 1. Setup Supabase (database)
# - Create project at supabase.com
# - Run supabase_schema.sql
# - Copy API credentials

# 2. Setup Backend (API)
cd backend
pip install -r ../requirements.txt
# Edit .env with Supabase credentials
python main.py

# 3. Setup Frontend
cd ../frontend
# Open dashboard.html in browser
# Check console for API connection

# 4. Deploy
# - Backend: render.com
# - Frontend: Already on Vercel!
```

---

## 🎉 You're Done!

Your TrendLoom platform should now be running with:
- ✅ Real-time API backend
- ✅ Interactive frontend
- ✅ Supabase database
- ✅ Live deployment

Visit your Vercel URL to see it in action!

For questions or issues, check the troubleshooting section above.
