# TrendLoom Backend API Tester
# Tests all endpoints and shows results

Write-Host "`n" -NoNewline
Write-Host "="*70 -ForegroundColor Cyan
Write-Host "  TRENDLOOM BACKEND API TESTER" -ForegroundColor Cyan
Write-Host "="*70 -ForegroundColor Cyan
Write-Host ""

$baseUrl = "https://trendloom-3aux.onrender.com"

# Test 1: Root endpoint
Write-Host "[1/5] Testing Root Endpoint..." -ForegroundColor Yellow
Write-Host "      URL: $baseUrl/" -ForegroundColor Gray
try {
    $response = Invoke-WebRequest -Uri "$baseUrl/" -Method Get -TimeoutSec 30
    $data = $response.Content | ConvertFrom-Json
    Write-Host "      ✅ SUCCESS" -ForegroundColor Green
    Write-Host "         Status: $($data.status)" -ForegroundColor Green
    Write-Host "         Service: $($data.service)" -ForegroundColor Green
    Write-Host "         Version: $($data.version)" -ForegroundColor Green
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Message -like "*404*") {
        Write-Host "         → Backend might not be deployed or sleeping" -ForegroundColor Yellow
    }
}
Write-Host ""

# Test 2: Health endpoint
Write-Host "[2/5] Testing Health Endpoint..." -ForegroundColor Yellow
Write-Host "      URL: $baseUrl/health" -ForegroundColor Gray
try {
    $response = Invoke-WebRequest -Uri "$baseUrl/health" -Method Get -TimeoutSec 30
    $data = $response.Content | ConvertFrom-Json
    Write-Host "      ✅ SUCCESS" -ForegroundColor Green
    Write-Host "         Status: $($data.status)" -ForegroundColor Green
    Write-Host "         Database: $($data.database)" -ForegroundColor Green
    Write-Host "         Environment: $($data.environment)" -ForegroundColor Green
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Test 3: Trends endpoint
Write-Host "[3/5] Testing Trends Endpoint..." -ForegroundColor Yellow
Write-Host "      URL: $baseUrl/api/trends/" -ForegroundColor Gray
try {
    $response = Invoke-WebRequest -Uri "$baseUrl/api/trends/" -Method Get -TimeoutSec 30
    $data = $response.Content | ConvertFrom-Json
    $count = $data.Count
    Write-Host "      ✅ SUCCESS" -ForegroundColor Green
    Write-Host "         Trends Found: $count" -ForegroundColor Green
    if ($count -gt 0) {
        Write-Host "         First 3 trends:" -ForegroundColor Green
        foreach ($trend in $data | Select-Object -First 3) {
            Write-Host "           - $($trend.name) (Score: $($trend.momentum_score), Cat: $($trend.category))" -ForegroundColor Cyan
        }
    }
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Test 4: Regional Countries endpoint
Write-Host "[4/5] Testing Regional Countries..." -ForegroundColor Yellow
Write-Host "      URL: $baseUrl/api/regional/countries" -ForegroundColor Gray
try {
    $response = Invoke-WebRequest -Uri "$baseUrl/api/regional/countries" -Method Get -TimeoutSec 30
    $data = $response.Content | ConvertFrom-Json
    Write-Host "      ✅ SUCCESS" -ForegroundColor Green
    Write-Host "         Countries: $($data -join ', ')" -ForegroundColor Green
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Test 5: Regional Trends (India)
Write-Host "[5/5] Testing Regional Trends (Tamil Nadu)..." -ForegroundColor Yellow
Write-Host "      URL: $baseUrl/api/regional/trends" -ForegroundColor Gray
try {
    $response = Invoke-WebRequest -Uri "$baseUrl/api/regional/trends?country_code=in&state=Tamil Nadu" -Method Get -TimeoutSec 30
    $data = $response.Content | ConvertFrom-Json
    $count = $data.Count
    Write-Host "      ✅ SUCCESS" -ForegroundColor Green
    Write-Host "         Tamil Nadu Trends: $count" -ForegroundColor Green
    if ($count -gt 0) {
        Write-Host "         First 3 trends:" -ForegroundColor Green
        foreach ($trend in $data | Select-Object -First 3) {
            Write-Host "           - $($trend.name) (Score: $($trend.momentum_score))" -ForegroundColor Cyan
        }
    }
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Summary
Write-Host "="*70 -ForegroundColor Cyan
Write-Host "  TEST COMPLETE" -ForegroundColor Cyan
Write-Host "="*70 -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. If all tests ✅ passed: Your backend is working!" -ForegroundColor Green
Write-Host "  2. If tests ❌ failed: Check VERIFY_DATA.md for troubleshooting" -ForegroundColor Yellow
Write-Host "  3. Open your Vercel URL and check frontend" -ForegroundColor Yellow
Write-Host ""
Write-Host "Troubleshooting Commands:" -ForegroundColor Yellow
Write-Host "  - Check Render logs: https://dashboard.render.com" -ForegroundColor Gray
Write-Host "  - View guide: cat VERIFY_DATA.md" -ForegroundColor Gray
Write-Host "  - Manual deploy: Go to Render → Manual Deploy" -ForegroundColor Gray
Write-Host ""
