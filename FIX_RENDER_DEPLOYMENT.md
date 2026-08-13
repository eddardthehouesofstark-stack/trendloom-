# 🔧 Fix Render Backend Deployment

## 📋 **Step-by-Step Render Configuration Check**

Your backend is returning 404 errors. Let's verify and fix the Render configuration.

---

## **Step 1: Check Service Exists**

1. Go to **https://dashboard.render.com**
2. Sign in
3. You should see your service: **trendloom-3aux** (or similar name)

✅ **If you see it:** Continue to Step 2  
❌ **If you DON'T see it:** The service was deleted or never created. See "Create New Service" below.

---

## **Step 2: Check Service Status**

Click on your **trendloom-3aux** service.

Look at the top status indicator:

### ✅ **Status: "Live" (Green)**
- Service is running
- But still showing 404? Jump to Step 5 (Check Logs)

### ⏸️ **Status: "Suspended" (Yellow)**
- Free tier suspended after inactivity
- **Fix:** Click **"Resume Service"** button
- Wait 2 minutes, then test again

### ❌ **Status: "Deploy failed" (Red)**
- Last deployment had errors
- Continue to Step 3 to fix

### 🔵 **Status: "Deploying..." (Blue)**
- Deployment in progress
- Wait 5 minutes, then refresh page

---

## **Step 3: Verify Build Configuration**

In your service dashboard, click **"Settings"** (left sidebar).

### ✅ **Check These Settings:**

**Root Directory:**
```
backend
```
⚠️ Or leave **EMPTY** (depends on your setup)

**Build Command:**
```
pip install -r requirements.txt
```
⚠️ If rootDir is empty, use:
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
⚠️ Or:
```
python main.py
```

**Python Version:** (under Advanced)
```
3.11
```
⚠️ Or `3.10` or `3.9` (Python 3.13 might have compatibility issues)

---

## **Step 4: Verify Environment Variables**

Still in **Settings**, scroll to **Environment Variables** section.

### ✅ **Required Variables (Must have ALL 3):**

```
SUPABASE_URL = https://xxxxx.supabase.co
SUPABASE_KEY = eyJhbGci...
SUPABASE_SERVICE_KEY = eyJhbGci... (longer)
```

### ❌ **If Missing:**

1. Click **"Add Environment Variable"**
2. Add each one:
   - Key: `SUPABASE_URL`
   - Value: (from Supabase Settings → API)
3. Click **"Save Changes"**
4. Service will auto-restart

### ⚠️ **Optional Variables:**

```
ENVIRONMENT = production
API_HOST = 0.0.0.0
API_PORT = 8000
FRONTEND_URL = https://your-vercel-app.vercel.app
VERCEL_URL = https://your-vercel-app.vercel.app
```

---

## **Step 5: Check Deployment Logs**

Click **"Logs"** tab (left sidebar).

### ✅ **Look for SUCCESS messages:**

```
✅ "Build succeeded"
✅ "Starting service..."
✅ "🚀 Starting TrendLoom API..."
✅ "✅ Database connection established"
✅ "✅ TrendLoom API is ready!"
✅ "Uvicorn running on http://0.0.0.0:XXXX"
```

### ❌ **Look for ERROR messages:**

**Error 1: ModuleNotFoundError**
```
ModuleNotFoundError: No module named 'xxx'
```
**Fix:** Add missing package to `requirements.txt`, commit, push

**Error 2: Database connection failed**
```
Error: Database connection failed
Could not connect to Supabase
```
**Fix:** Check environment variables are set correctly

**Error 3: Port binding error**
```
Error: Port already in use
```
**Fix:** Make sure start command uses `--port $PORT`

**Error 4: Python version error**
```
Python version not supported
```
**Fix:** Change Python version in Settings → Advanced

**Error 5: File not found**
```
Error: cannot stat 'main.py'
```
**Fix:** Check Root Directory setting matches your folder structure

---

## **Step 6: Test Correct Configuration**

### **Option A: Correct Setup (rootDir = backend)**

If your files are in `backend/` folder:

```yaml
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### **Option B: Correct Setup (rootDir = empty)**

If your files are in root:

```yaml
Root Directory: (empty)
Build Command: cd backend && pip install -r requirements.txt
Start Command: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

### **Option C: Using Python directly**

```yaml
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: python main.py
```

**Note:** Make sure `main.py` has this at the bottom:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000))
    )
```

---

## **Step 7: Manual Redeploy**

After fixing configuration:

1. Click **"Manual Deploy"** (top right)
2. Select **"Clear build cache & deploy"**
3. Click **"Deploy"**
4. Wait 5 minutes
5. Watch the logs for success messages

---

## **Step 8: Test After Deploy**

After deployment completes:

```powershell
# Run the test script
powershell -ExecutionPolicy Bypass -File test-backend.ps1
```

Or manually test:

```powershell
# Wait 30 seconds for service to wake up
Start-Sleep -Seconds 30

# Test root endpoint
Invoke-WebRequest -Uri "https://trendloom-3aux.onrender.com/" | Select-Object -ExpandProperty Content
```

---

## **QUICK FIX CHECKLIST:**

Go through this in Render dashboard:

- [ ] **Service exists** and is visible
- [ ] **Status is "Live"** (not suspended or failed)
- [ ] **Root Directory** is set correctly (`backend` or empty)
- [ ] **Build Command** is correct
- [ ] **Start Command** is correct and uses `$PORT`
- [ ] **Python Version** is 3.9, 3.10, or 3.11
- [ ] **SUPABASE_URL** environment variable is set
- [ ] **SUPABASE_KEY** environment variable is set
- [ ] **SUPABASE_SERVICE_KEY** environment variable is set
- [ ] **Logs show** "TrendLoom API is ready!"
- [ ] **Test endpoint** returns JSON (not 404)

---

## **CREATE NEW SERVICE (If service doesn't exist)**

If you don't see any service on Render:

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `trendloom-`
3. Configure:
   - **Name:** `trendloom-api`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** `backend`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add Environment Variables (3 Supabase vars)
5. Click **"Create Web Service"**
6. Wait 5 minutes for first deploy

---

## **COMMON ISSUES & SOLUTIONS:**

| Issue | Cause | Solution |
|-------|-------|----------|
| **404 on all endpoints** | Service not deployed | Manual deploy |
| **"Deploy failed"** | Build errors | Check logs, fix errors |
| **"Suspended"** | Free tier inactivity | Resume service |
| **"ModuleNotFoundError"** | Missing package | Add to requirements.txt |
| **"Database connection failed"** | Missing env vars | Add Supabase credentials |
| **"Port already in use"** | Wrong start command | Use `--port $PORT` |
| **Empty logs** | Service never started | Check build command |
| **Timeout errors** | Service sleeping | Wait 30 seconds |

---

## **VERIFY YOUR CURRENT SETTINGS:**

### **What Your Render Settings SHOULD Be:**

```
==================================================
RENDER SERVICE CONFIGURATION
==================================================

Service Name: trendloom-3aux (or trendloom-api)
Region: Any (Oregon, Ohio, Frankfurt, Singapore)
Plan: Free

Git Configuration:
  Repository: trendloom-
  Branch: main
  Root Directory: backend

Build & Deploy:
  Runtime: Python 3
  Build Command: pip install -r requirements.txt
  Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
  
Advanced:
  Python Version: 3.11 (or 3.10, 3.9)
  Health Check Path: /health

Environment Variables:
  SUPABASE_URL: https://xxxxx.supabase.co
  SUPABASE_KEY: eyJhbGci...
  SUPABASE_SERVICE_KEY: eyJhbGci... (longer)
  ENVIRONMENT: production (optional)

==================================================
```

---

## **AFTER FIXING:**

Once everything is configured correctly and deployed:

1. Service status will be **"Live" (Green)**
2. Logs will show **"TrendLoom API is ready!"**
3. Test script will show **✅ SUCCESS** for all endpoints
4. Your Vercel website will load India fashion data

---

## **NEED HELP?**

**If still not working after following ALL steps:**

1. **Share these with me:**
   - Screenshot of Render service status
   - Last 50 lines of Render logs
   - Current Root Directory setting
   - Current Build Command
   - Current Start Command

2. **Then I can provide specific fix!**

---

## **TEST AFTER FIX:**

```powershell
# Test backend
powershell -ExecutionPolicy Bypass -File test-backend.ps1

# Expected output:
# ✅ SUCCESS - Status: online
# ✅ SUCCESS - Database: connected
# ✅ SUCCESS - Trends Found: 35
```

---

**Go to Render dashboard now and check each setting!** 🔧

https://dashboard.render.com

