# 🗄️ Supabase Database Setup (5 Minutes)

## Step 1: Create Supabase Account & Project

1. **Go to Supabase**: https://supabase.com
2. Click **"Start your project"** or **"Sign In"**
3. Sign up with **GitHub** (easiest option)
4. Click **"New Project"**

**Fill in these details:**
```
Organization: (Create new or use existing)
Name: trendloom
Database Password: (create a strong password - SAVE THIS!)
Region: Choose closest to you (e.g., US East, Europe West)
Pricing Plan: Free
```

5. Click **"Create new project"**
6. ⏱️ Wait 2-3 minutes for project creation

---

## Step 2: Run Database Schema

Once your project is created:

1. In Supabase dashboard, click **"SQL Editor"** (left sidebar)
2. Click **"New Query"**
3. Copy the SQL schema from `backend/supabase_schema.sql`
4. Paste it into the SQL Editor
5. Click **"Run"** button (or press Ctrl+Enter)
6. ✅ Should see: "Success. No rows returned" (this is normal!)

**What this creates:**
- ✅ 7 database tables
- ✅ Indexes for performance
- ✅ Sample fashion trend data
- ✅ Row-level security policies

---

## Step 3: Get API Credentials

1. Click **Settings** (gear icon, bottom left)
2. Click **API** section
3. You'll see:

### Project URL
```
https://xxxxxxxxxxxxx.supabase.co
```
**Copy this** → You'll need it as `SUPABASE_URL`

### API Keys

**anon / public key** (starts with `eyJ...`)
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
**Copy this** → You'll need it as `SUPABASE_KEY`

**service_role key** (starts with `eyJ...`, longer)
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
**Copy this** → You'll need it as `SUPABASE_SERVICE_KEY`

⚠️ **IMPORTANT**: The service_role key is SECRET - never expose it in frontend code!

---

## Step 4: Add Credentials to Render

Now connect your database to the backend:

1. Go to **Render Dashboard**: https://dashboard.render.com
2. Click on your **trendloom-api** service
3. Go to **"Environment"** tab (left sidebar)
4. Click **"Add Environment Variable"**

Add these **one by one**:

### Variable 1:
```
Key:   SUPABASE_URL
Value: (paste your Project URL here)
```

### Variable 2:
```
Key:   SUPABASE_KEY
Value: (paste your anon/public key here)
```

### Variable 3:
```
Key:   SUPABASE_SERVICE_KEY
Value: (paste your service_role key here)
```

5. Click **"Save Changes"**
6. ⏱️ Render will automatically restart your service (takes 1-2 minutes)

---

## Step 5: Verify Database Connection

Once Render finishes restarting:

1. Visit: https://trendloom-3aux.onrender.com/health
2. Should see:
   ```json
   {
     "status": "healthy",
     "database": "connected",
     "scheduler": "active",
     "environment": "production"
   }
   ```

3. Test data retrieval: https://trendloom-3aux.onrender.com/api/trends/
4. Should see JSON array of fashion trends!

---

## 📋 Quick Checklist

- [ ] Supabase project created
- [ ] SQL schema executed (7 tables created)
- [ ] Project URL copied
- [ ] anon key copied
- [ ] service_role key copied
- [ ] All 3 variables added to Render
- [ ] Render service restarted
- [ ] /health endpoint shows "connected"
- [ ] /api/trends/ returns data

---

## 🗂️ Database Tables Created

Your database now has:

1. **trends** - Main fashion trends
2. **regional_trends** - Location-specific trends
3. **seasonal_trends** - Seasonal fashion data
4. **competitors** - Competitor information
5. **recommendations** - AI recommendations
6. **attributes** - Fashion attributes (colors, fabrics, etc.)
7. **recommendation_feedback** - User feedback tracking

Each table has:
- Auto-incrementing ID
- Timestamps (created_at, updated_at)
- Indexes for fast queries
- Sample data for testing

---

## 📊 View Your Data

In Supabase dashboard:

1. Click **"Table Editor"** (left sidebar)
2. Click any table name
3. See the data in a spreadsheet view
4. You can add/edit/delete rows here

Try clicking on **"trends"** table - you should see 5 sample trends!

---

## 🧪 Test Queries

In Supabase SQL Editor, try these queries:

### Get all trends:
```sql
SELECT * FROM trends;
```

### Get trending items:
```sql
SELECT * FROM trends WHERE status = 'trending' ORDER BY momentum_score DESC;
```

### Get regional trends for India:
```sql
SELECT * FROM regional_trends WHERE country_code = 'in';
```

---

## 🔒 Security Notes

**What's Safe:**
- ✅ `SUPABASE_URL` - Can be public
- ✅ `SUPABASE_KEY` (anon key) - Can be in frontend
- ❌ `SUPABASE_SERVICE_KEY` - NEVER expose! Backend only!

**Row Level Security (RLS):**
- Already configured with basic policies
- Allows all operations for now (development)
- Tighten security before production launch

---

## 🐛 Troubleshooting

### "Error creating project"
- Check your email for verification
- Try a different project name
- Wait a few minutes and retry

### "SQL execution failed"
- Make sure you copied the ENTIRE schema file
- Check for any syntax errors
- Try running sections one at a time

### "Database connection failed" in Render
- Double-check all 3 environment variables are set
- Verify no extra spaces in the values
- Make sure Render service restarted after adding variables

### "No data returned" from API
- Check SQL schema was run successfully
- Verify sample data was inserted
- Check Supabase Table Editor to see if tables exist

---

## 💡 Next Steps After Setup

### Immediate:
1. Test all API endpoints
2. Check frontend loads data
3. Explore Supabase dashboard

### Soon:
1. Add more sample data
2. Customize trends for your use case
3. Enable real-time subscriptions

### Later:
1. Implement user authentication
2. Add row-level security rules
3. Set up database backups
4. Monitor usage and scale

---

## 📞 Help & Resources

- **Supabase Docs**: https://supabase.com/docs
- **SQL Editor**: https://supabase.com/dashboard/project/_/sql
- **Table Editor**: https://supabase.com/dashboard/project/_/editor
- **API Docs**: https://supabase.com/dashboard/project/_/api

---

## 🎯 Success Criteria

You'll know it's working when:

✅ Supabase project shows "Active"
✅ 7 tables visible in Table Editor  
✅ Sample data visible in tables
✅ Render health check shows "database: connected"
✅ API endpoints return real data
✅ Frontend dashboard loads trends

---

**Ready to set up? Follow the steps above!** 🚀

Total time: ~5 minutes
Cost: $0 (Free tier: 500MB database, 2GB bandwidth)
