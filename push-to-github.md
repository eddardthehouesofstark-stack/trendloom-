# Push TrendLoom to GitHub - Step by Step Guide

## Step 1: Create GitHub Repository

1. **Open this link**: https://github.com/new
2. **Repository name**: `trendloom-dashboard` (or any name you prefer)
3. **Description**: "Fashion Intelligence Dashboard - Real-time global trend analysis platform"
4. **Visibility**: Public (or Private if you prefer)
5. **IMPORTANT**: Do NOT check any of these boxes:
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
6. Click **"Create repository"**

## Step 2: Copy Your Repository URL

After creating the repository, GitHub will show you a page with setup instructions.

Copy the repository URL that looks like:
```
https://github.com/YOUR_USERNAME/trendloom-dashboard.git
```

## Step 3: Run These Commands

Open PowerShell in this folder and run:

```powershell
# Add your GitHub repository as remote (replace URL with yours)
git remote add origin https://github.com/YOUR_USERNAME/trendloom-dashboard.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME/trendloom-dashboard.git` with your actual repository URL!**

## Step 4: Deploy to Vercel

### Option A: Vercel Dashboard (Easiest - Recommended)

1. Go to: https://vercel.com/new
2. Sign in with your GitHub account
3. Click "Import" next to your `trendloom-dashboard` repository
4. Vercel will detect the `vercel.json` configuration automatically
5. Click "Deploy"
6. Wait 30-60 seconds
7. Your site will be live! 🎉

Vercel will give you a URL like: `https://trendloom-dashboard.vercel.app`

### Option B: Vercel CLI (Alternative)

```powershell
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

---

## Quick Command Summary

After creating the GitHub repo, copy your repo URL and run:

```powershell
git remote add origin YOUR_GITHUB_REPO_URL
git branch -M main
git push -u origin main
```

Then go to https://vercel.com/new to deploy!

---

## Troubleshooting

**If you get "remote origin already exists":**
```powershell
git remote remove origin
git remote add origin YOUR_GITHUB_REPO_URL
```

**If push is rejected:**
```powershell
git pull origin main --rebase
git push -u origin main
```

---

## Your Project Structure
```
srcas hackathon/
├── frontend/
│   ├── dashboard.html        (Homepage)
│   ├── seasonal.html
│   ├── exploretrens.html
│   ├── regional.html         (NEW: Country/State selectors)
│   ├── comp.html
│   ├── suggestion.html
│   └── attributes.html       (NEW: Attribute analyzer)
├── vercel.json               (Deployment config)
├── README.md                 (Project documentation)
└── .git/                     (Git repository)
```

✅ Everything is ready to push!
