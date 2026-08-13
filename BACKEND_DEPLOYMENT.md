# 🚀 Backend Deployment Guide

## Quick Deploy to Render.com (Recommended - Free Tier)

### Why Render?
- ✅ **Free tier available** (750 hours/month)
- ✅ **Automatic deploys** from GitHub
- ✅ **Easy setup** (5 minutes)
- ✅ **No credit card** required for free tier

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure you have:

- [x] ✅ GitHub repository with all code pushed
- [x] ✅ Backend running locally (tested)
- [ ] ⏳ Supabase project created
- [ ] ⏳ Supabase credentials ready

---

## 🌐 Option 1: Render.com (Easiest - Recommended)

### Step 1: Sign Up for Render

1. Go to [render.com](https://render.com)
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your GitHub

### Step 2: Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your repository:
   - Click **"Connect repository"**
   - Find `trendloom-` in the list
   - Click **"Connect"**

### Step 3: Configure Service

Fill in these settings:

**Basic Settings:**
```
Name:                 trendloom-api
Region:              Oregon (US West) - or closest to you
Branch:              main
Root Directory:      backend
Runtime:             Python 3
```

**Build Settings:**
```
Build Command:       pip install -r ../requirements.txt
Start Command:       uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:**
```
Select:              Free ($0/month)
```

### Step 4: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables (one by one):

```
SUPABASE_URL              = your_supabase_project_url
SUPABASE_KEY              = your_supabase_anon_key  
SUPABASE_SERVICE_KEY      = your_supabase_service_key
API_HOST                  = 0.0.0.0
API_PORT                  = 8000
ENVIRONMENT               = production
FRONTEND_URL              = https://your-vercel-app.vercel.app
VERCEL_URL                = https://your-vercel-app.vercel.app
```

**Where to get Supabase credentials:**
1. Go to your Supabase project
2. Click **Settings** (gear icon)
3. Click **API**
4. Copy:
   - **Project URL** → `SUPABASE_URL`
   - **anon public** key → `SUPABASE_KEY`
   - **service_role** key → `SUPABASE_SERVICE_KEY`

### Step 5: Deploy!

1. Click **"Create Web Service"**
2. Wait 3-5 minutes for deployment
3. ✅ Your API will be live!

**Your API URL will be:**
```
https://trendloom-api.onrender.com
```

### Step 6: Test Your Deployment

Visit these URLs to confirm it's working:

```
https://trendloom-api.onrender.com/
https://trendloom-api.onrender.com/health
https://trendloom-api.onrender.com/docs
```

You should see:
- `/` → `{"status": "online", "service": "TrendLoom API"}`
- `/health` → `{"status": "healthy"}`
- `/docs` → Interactive API documentation

---

## 🔧 Option 2: Railway.app (Alternative)

### Step 1: Sign Up

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"**

### Step 2: Deploy from GitHub

1. Select **"Deploy from GitHub repo"**
2. Choose `trendloom-`
3. Railway auto-detects Python

### Step 3: Configure

1. Click on your service
2. Go to **"Variables"** tab
3. Add environment variables (same as Render above)

### Step 4: Configure Build

1. Go to **"Settings"** tab
2. **Root Directory**: `backend`
3. **Build Command**: `pip install -r ../requirements.txt`
4. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 5: Deploy

1. Click **"Deploy"**
2. Wait 3-5 minutes
3. Get your URL from the **"Domains"** section

---

## ☁️ Option 3: Fly.io

### Step 1: Install Fly CLI

```powershell
# Windows (PowerShell)
irm https://fly.io/install.ps1 | iex
```

### Step 2: Sign Up & Login

```powershell
fly auth signup
# or if you have an account:
fly auth login
```

### Step 3: Deploy

```powershell
cd backend

# Initialize (creates fly.toml)
fly launch

# When prompted:
# App name: trendloom-api
# Region: Choose closest
# Setup PostgreSQL? No (we use Supabase)
# Deploy now? Yes
```

### Step 4: Set Environment Variables

```powershell
fly secrets set SUPABASE_URL="your_url"
fly secrets set SUPABASE_KEY="your_key"
fly secrets set SUPABASE_SERVICE_KEY="your_service_key"
fly secrets set ENVIRONMENT="production"
```

---

## 🐳 Option 4: Docker + Any Platform

### Create Dockerfile

Already created at `backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and Run Locally

```powershell
cd backend
docker build -t trendloom-api .
docker run -p 8000:8000 trendloom-api
```

### Deploy to Any Platform

- **Google Cloud Run**: `gcloud run deploy`
- **AWS ECS**: Use Fargate
- **Azure Container Apps**: `az containerapp create`

---

## 🔄 Auto-Deploy Setup

### Enable Automatic Deployments

**Render.com:**
- Already enabled by default
- Every push to `main` triggers deploy

**Railway:**
- Go to Settings → Enable auto-deploy

**Fly.io:**
- Use GitHub Actions (see below)

---

## 🎯 Post-Deployment Steps

### 1. Update Frontend API URL

Edit `frontend/js/api.js`:

```javascript
const API_CONFIG = {
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://trendloom-api.onrender.com', // Your deployed URL
    timeout: 10000
};
```

### 2. Update CORS in Backend

Edit `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-vercel-app.vercel.app",  # Your Vercel URL
        "http://localhost:5500",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Push Changes

```powershell
git add .
git commit -m "Update API URLs for production"
git push origin main
```

### 4. Test Everything

1. Visit your frontend: `https://your-app.vercel.app`
2. Open browser console (F12)
3. Check for API calls
4. Should see data loading from your deployed backend!

---

## 📊 Monitoring & Logs

### Render.com
- Dashboard → Your Service → **Logs** tab
- Real-time log streaming
- Download logs

### Railway
- Project → **Logs** tab
- Real-time logs

### Fly.io
```powershell
fly logs
```

---

## 🐛 Troubleshooting

### Deployment Failed

**Check Build Logs:**
- Look for error messages
- Usually shows which package failed to install

**Common Issues:**

1. **Missing dependencies:**
   ```
   Error: pip install failed
   ```
   **Fix:** Ensure `requirements.txt` is up to date

2. **Port binding error:**
   ```
   Error: Address already in use
   ```
   **Fix:** Use `$PORT` environment variable in start command

3. **Supabase connection fails:**
   ```
   Error: Supabase credentials not configured
   ```
   **Fix:** Check environment variables are set correctly

### API Not Responding

1. **Check deployment status** in Render/Railway dashboard
2. **Check logs** for errors
3. **Test health endpoint:** `https://your-api.com/health`
4. **Verify environment variables** are set

### CORS Errors in Frontend

```
Error: CORS policy blocked
```

**Fix:** Add your frontend URL to `allow_origins` in `backend/main.py`

---

## 💰 Cost Breakdown

### Free Tier Limits

**Render.com Free:**
- 750 hours/month (enough for 1 service 24/7)
- 512MB RAM
- Sleeps after 15 min inactivity
- Wakes up on first request (~30 seconds)

**Railway Free:**
- $5 free credit/month
- ~87 hours of uptime
- Better for testing

**Fly.io Free:**
- 3 shared VMs
- 160GB bandwidth
- Always-on

### Paid Options (When Scaling)

**Render Starter: $7/month**
- Always-on (no sleep)
- 1GB RAM
- Worth it for production

**Railway Pro: $20/month**
- $20 credit/month
- Scales automatically

**Fly.io: Pay-as-you-go**
- ~$5-10/month for small app

---

## 🎯 Recommended Flow

### For Development/Testing:
```
1. Render.com Free Tier
2. Accepts 15-min sleep time
3. Test everything works
```

### For Production:
```
1. Upgrade to Render Starter ($7/month)
2. OR Railway Pro ($20/month)  
3. OR Fly.io Pay-as-you-go
4. Always-on, faster response
```

---

## ✅ Deployment Checklist

Before going live:

- [ ] Backend runs locally without errors
- [ ] Supabase project created and schema loaded
- [ ] Environment variables configured
- [ ] Deployed to Render/Railway/Fly
- [ ] Tested `/health` endpoint
- [ ] Frontend API URL updated
- [ ] CORS configured for frontend URL
- [ ] Changes pushed to GitHub
- [ ] End-to-end test: Frontend → API → Database

---

## 🚀 Quick Commands Reference

### Render.com
```
1. Connect GitHub repo
2. Configure build/start commands
3. Add environment variables
4. Click "Create Web Service"
```

### Railway
```powershell
railway login
railway init
railway up
railway variables set KEY=value
```

### Fly.io
```powershell
fly auth login
fly launch
fly secrets set KEY=value
fly deploy
fly logs
```

### Update Deployment
```powershell
# Just push to GitHub (auto-deploys)
git add .
git commit -m "Update"
git push origin main
```

---

## 🎉 You're Done!

Once deployed, your TrendLoom API will be live at:
```
https://trendloom-api.onrender.com/docs
```

And your frontend on Vercel will connect to it automatically!

For help, check:
- Render docs: https://render.com/docs
- Railway docs: https://docs.railway.app
- Fly.io docs: https://fly.io/docs
