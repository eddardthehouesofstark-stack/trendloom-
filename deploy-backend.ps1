# TrendLoom Backend Deployment Helper Script
# Run this to get deployment URLs and instructions

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TrendLoom Backend Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📦 Your backend is ready to deploy!" -ForegroundColor Green
Write-Host ""

Write-Host "🌐 DEPLOYMENT OPTIONS:" -ForegroundColor Yellow
Write-Host ""

Write-Host "1️⃣  RENDER.COM (Recommended - Easiest)" -ForegroundColor Cyan
Write-Host "   ✅ Free tier available" 
Write-Host "   ✅ Auto-deploys from GitHub"
Write-Host "   ✅ No credit card needed"
Write-Host ""
Write-Host "   👉 Go to: https://render.com" -ForegroundColor Green
Write-Host "   📖 Full guide: BACKEND_DEPLOYMENT.md" -ForegroundColor Gray
Write-Host ""

Write-Host "2️⃣  RAILWAY.APP (Alternative)" -ForegroundColor Cyan
Write-Host "   ✅ $5 free credit/month"
Write-Host "   ✅ Simple setup"
Write-Host ""
Write-Host "   👉 Go to: https://railway.app" -ForegroundColor Green
Write-Host ""

Write-Host "3️⃣  FLY.IO (For Advanced Users)" -ForegroundColor Cyan
Write-Host "   ✅ Always-on free tier"
Write-Host "   ✅ Global edge network"
Write-Host ""
Write-Host "   👉 Install: irm https://fly.io/install.ps1 | iex" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 QUICK SETUP (5 MINUTES):" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Click one of the links above" -ForegroundColor White
Write-Host "2. Sign up with GitHub" -ForegroundColor White  
Write-Host "3. Connect this repository: trendloom-" -ForegroundColor White
Write-Host "4. Set these config values:" -ForegroundColor White
Write-Host ""
Write-Host "   Root Directory:  backend" -ForegroundColor Gray
Write-Host "   Build Command:   pip install -r ../requirements.txt" -ForegroundColor Gray
Write-Host "   Start Command:   uvicorn main:app --host 0.0.0.0 --port `$PORT" -ForegroundColor Gray
Write-Host ""
Write-Host "5. Add environment variables (from Supabase):" -ForegroundColor White
Write-Host "   - SUPABASE_URL" -ForegroundColor Gray
Write-Host "   - SUPABASE_KEY" -ForegroundColor Gray
Write-Host "   - SUPABASE_SERVICE_KEY" -ForegroundColor Gray
Write-Host ""
Write-Host "6. Click Deploy! 🚀" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📚 NEED HELP?" -ForegroundColor Yellow
Write-Host "   Read: BACKEND_DEPLOYMENT.md (step-by-step guide)" -ForegroundColor White
Write-Host ""

Write-Host "🎯 CURRENT STATUS:" -ForegroundColor Yellow
Write-Host ""

# Check if backend is running locally
$backendRunning = $false
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -TimeoutSec 2
    if ($response.StatusCode -eq 200) {
        $backendRunning = $true
    }
} catch {
    $backendRunning = $false
}

if ($backendRunning) {
    Write-Host "   ✅ Backend running locally" -ForegroundColor Green
    Write-Host "   👉 http://localhost:8000/docs" -ForegroundColor Gray
} else {
    Write-Host "   ⚠️  Backend not running locally" -ForegroundColor Yellow
    Write-Host "   Run: cd backend ; python main.py" -ForegroundColor Gray
}
Write-Host ""

# Check if Supabase is configured
if (Test-Path ".env") {
    $envContent = Get-Content ".env" -Raw
    if ($envContent -match "SUPABASE_URL") {
        Write-Host "   ✅ Supabase configured" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  Supabase not configured" -ForegroundColor Yellow
        Write-Host "   Setup: Follow SETUP_GUIDE.md" -ForegroundColor Gray
    }
} else {
    Write-Host "   ⚠️  .env file not found" -ForegroundColor Yellow
    Write-Host "   Copy: .env.example to .env" -ForegroundColor Gray
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Ready to deploy? Choose an option above! 🚀" -ForegroundColor Green
Write-Host ""

# Pause
Read-Host "Press Enter to exit"
