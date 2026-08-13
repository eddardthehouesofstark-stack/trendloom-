# 🔧 Render Environment Variables Setup

## 🎯 Quick Access

**Render Dashboard**: https://dashboard.render.com  
**Your Service**: trendloom-3aux

---

## 📋 REQUIRED Environment Variables

You need to add **3 variables** from Supabase to make your backend work with the database.

### Step-by-Step Guide:

1. Go to: https://dashboard.render.com
2. Click on your **"trendloom-3aux"** service
3. Click **"Environment"** in the left sidebar
4. Click **"Add Environment Variable"** button

---

## ✅ Variables to Add

### Variable 1: SUPABASE_URL

```
Key:   SUPABASE_URL
Value: https://xxxxxxxxxxxxx.supabase.co
```

**Where to get this:**
1. Go to https://app.supabase.com
2. Open your `trendloom` project
3. Click **Settings** (gear icon) → **API**
4. Copy the **"Project URL"**

**Example:**
```
https://abcdefghijklmnop.supabase.co
```

---

### Variable 2: SUPABASE_KEY

```
Key:   SUPABASE_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Where to get this:**
1. In Supabase project
2. Settings → API
3. Under **"Project API keys"**
4. Copy the **"anon" / "public"** key (the shorter one)

**Starts with:** `eyJ...`  
**Length:** ~250 characters

---

### Variable 3: SUPABASE_SERVICE_KEY

```
Key:   SUPABASE_SERVICE_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Where to get this:**
1. In Supabase project
2. Settings → API
3. Under **"Project API keys"**
4. Copy the **"service_role"** key (the LONGER one)

⚠️ **IMPORTANT**: This is SECRET! Never expose in frontend!

**Starts with:** `eyJ...`  
**Length:** ~350+ characters

---

## 🎨 Visual Guide

### In Render Dashboard:

```
┌─────────────────────────────────────────────┐
│  Environment Variables                       │
├─────────────────────────────────────────────┤
│                                              │
│  [Add Environment Variable]                  │
│                                              │
│  ┌──────────────────────────────────────┐  │
│  │ Key:   SUPABASE_URL                   │  │
│  │ Value: https://abc123.supabase.co     │  │
│  └──────────────────────────────────────┘  │
│                                              │
│  ┌──────────────────────────────────────┐  │
│  │ Key:   SUPABASE_KEY                   │  │
│  │ Value: eyJhbGci...                    │  │
│  └──────────────────────────────────────┘  │
│                                              │
│  ┌──────────────────────────────────────┐  │
│  │ Key:   SUPABASE_SERVICE_KEY           │  │
│  │ Value: eyJhbGci... (longer)           │  │
│  └──────────────────────────────────────┘  │
│                                              │
│                            [Save Changes]    │
└─────────────────────────────────────────────┘
```

---

## 📸 Screenshot Guide

### Render Dashboard:

1. **Navigate to Service**
   ```
   Dashboard → Services → trendloom-3aux
   ```

2. **Go to Environment Tab**
   ```
   Left Sidebar → Environment
   ```

3. **Add Each Variable**
   - Click "Add Environment Variable"
   - Enter Key (exactly as shown above)
   - Paste Value from Supabase
   - Click outside or press Enter
   - Repeat for all 3 variables

4. **Save Changes**
   - Click "Save Changes" button at bottom
   - Wait for service to restart (1-2 minutes)
   - Check logs for confirmation

---

## 🧪 Verification

After adding variables and Render restarts:

### Test 1: Health Check
Visit: https://trendloom-3aux.onrender.com/health

**Expected Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "scheduler": "active",
  "environment": "production"
}
```

### Test 2: Get Trends
Visit: https://trendloom-3aux.onrender.com/api/trends/

**Expected Response:**
```json
[
  {
    "id": 1,
    "name": "Oversized Blazers",
    "category": "Outerwear",
    "status": "trending",
    ...
  },
  ...
]
```

### Test 3: Check Render Logs

In Render dashboard:
1. Click **"Logs"** tab
2. Look for:
   ```
   ✅ Database connection established
   ✅ TrendLoom API is ready!
   ```

---

## ❌ Common Issues

### Issue: "Database connection failed"

**Cause:** Environment variables not set or incorrect

**Fix:**
1. Check all 3 variables are added
2. Verify no extra spaces in values
3. Confirm keys are spelled exactly: `SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_SERVICE_KEY`
4. Click "Save Changes" after adding

### Issue: "Service not restarting"

**Cause:** Need to manually trigger restart

**Fix:**
1. Go to your service page
2. Click "Manual Deploy" → "Clear build cache & deploy"
3. Wait 2-3 minutes

### Issue: "Invalid API key"

**Cause:** Wrong key copied from Supabase

**Fix:**
1. Go back to Supabase → Settings → API
2. **Re-copy** the correct keys:
   - `SUPABASE_KEY` = anon/public key (shorter)
   - `SUPABASE_SERVICE_KEY` = service_role key (longer)
3. Update in Render

### Issue: "Database does not exist"

**Cause:** SQL schema not run in Supabase

**Fix:**
1. Go to Supabase → SQL Editor
2. Copy entire `backend/supabase_schema.sql` file
3. Paste and run in SQL Editor
4. Should create 7 tables

---

## 📋 Complete Checklist

Before adding to Render:

- [ ] Supabase project created
- [ ] SQL schema executed (`supabase_schema.sql`)
- [ ] 7 tables visible in Table Editor
- [ ] Project URL copied
- [ ] anon/public key copied
- [ ] service_role key copied

Adding to Render:

- [ ] Logged into Render dashboard
- [ ] Opened trendloom-3aux service
- [ ] Clicked Environment tab
- [ ] Added `SUPABASE_URL`
- [ ] Added `SUPABASE_KEY`
- [ ] Added `SUPABASE_SERVICE_KEY`
- [ ] Clicked "Save Changes"
- [ ] Waited for restart (check logs)

Verification:

- [ ] Health check shows "connected"
- [ ] /api/trends/ returns data
- [ ] No errors in Render logs
- [ ] Frontend dashboard loads data

---

## 🔐 Security Notes

**Safe to expose:**
- ✅ `SUPABASE_URL` (public URL)
- ✅ `SUPABASE_KEY` (anon/public key - has limited access)

**NEVER expose:**
- ❌ `SUPABASE_SERVICE_KEY` (full admin access)
- ❌ Database password
- ❌ Any SECRET keys

**Where they're used:**
- `SUPABASE_URL` → Both frontend and backend
- `SUPABASE_KEY` → Frontend read operations
- `SUPABASE_SERVICE_KEY` → Backend admin operations (Render only!)

---

## 📝 Copy-Paste Template

Use this template when adding to Render:

```
Key: SUPABASE_URL
Value: [PASTE YOUR PROJECT URL HERE]

Key: SUPABASE_KEY
Value: [PASTE YOUR ANON/PUBLIC KEY HERE]

Key: SUPABASE_SERVICE_KEY
Value: [PASTE YOUR SERVICE_ROLE KEY HERE]
```

---

## 🎯 What Happens After Adding

1. **Render detects changes**
   - Sees new environment variables
   - Triggers automatic restart

2. **Service restarts** (1-2 minutes)
   - Loads new configuration
   - Connects to Supabase
   - Initializes database connection

3. **Backend becomes fully functional**
   - All API endpoints work
   - Database queries succeed
   - Frontend can fetch data

4. **Your platform is LIVE! 🚀**
   - Complete end-to-end functionality
   - Real-time data flow
   - Production-ready

---

## 📞 Need Help?

### Render Support
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs
- Status: https://status.render.com

### Supabase Support
- Dashboard: https://app.supabase.com
- Docs: https://supabase.com/docs
- Community: https://supabase.com/community

### Your Project
- GitHub: https://github.com/eddardthehouesofstark-stack/trendloom-
- Backend API: https://trendloom-3aux.onrender.com/docs

---

## 🚀 Quick Action Steps

**Right now, do this:**

1. Open https://app.supabase.com
2. Get your 3 credentials (URL + 2 keys)
3. Open https://dashboard.render.com
4. Add the 3 environment variables
5. Click "Save Changes"
6. Wait 2 minutes
7. Test: https://trendloom-3aux.onrender.com/health

**Total time: 5 minutes** ⏱️

---

## ✅ Success!

Once you see this response:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

**You're done!** Your complete TrendLoom platform is 100% operational! 🎉

---

Last Updated: August 13, 2026  
Status: Ready for setup 🔧

