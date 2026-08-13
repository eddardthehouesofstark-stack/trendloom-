# TrendLoom GitHub Setup Script
# Run this after creating your GitHub repository

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "TrendLoom - GitHub Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Prompt for GitHub repository URL
Write-Host "Please enter your GitHub repository URL" -ForegroundColor Yellow
Write-Host "Example: https://github.com/praga/trendloom-dashboard.git" -ForegroundColor Gray
Write-Host ""
$repoUrl = Read-Host "Repository URL"

if ([string]::IsNullOrWhiteSpace($repoUrl)) {
    Write-Host "Error: Repository URL cannot be empty!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Setting up remote..." -ForegroundColor Green

# Remove existing origin if it exists
git remote remove origin 2>$null

# Add new remote
git remote add origin $repoUrl

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Remote added successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to add remote" -ForegroundColor Red
    exit 1
}

# Rename branch to main
Write-Host "Renaming branch to main..." -ForegroundColor Green
git branch -M main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Branch renamed to main" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to rename branch" -ForegroundColor Red
    exit 1
}

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Green
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ SUCCESS! Code pushed to GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next Step: Deploy to Vercel" -ForegroundColor Yellow
    Write-Host "1. Go to: https://vercel.com/new" -ForegroundColor Cyan
    Write-Host "2. Sign in with GitHub" -ForegroundColor Cyan
    Write-Host "3. Import your repository" -ForegroundColor Cyan
    Write-Host "4. Click Deploy" -ForegroundColor Cyan
    Write-Host ""
    
    # Ask if user wants to open Vercel
    $openVercel = Read-Host "Open Vercel deployment page? (y/n)"
    if ($openVercel -eq 'y' -or $openVercel -eq 'Y') {
        Start-Process "https://vercel.com/new"
        Write-Host "✓ Opening Vercel..." -ForegroundColor Green
    }
} else {
    Write-Host ""
    Write-Host "✗ Failed to push to GitHub" -ForegroundColor Red
    Write-Host "Please check your repository URL and try again" -ForegroundColor Yellow
    exit 1
}
