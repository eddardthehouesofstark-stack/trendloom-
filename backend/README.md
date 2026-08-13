# TrendLoom Backend API

FastAPI + Supabase backend for real-time fashion intelligence platform.

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Supabase account ([supabase.com](https://supabase.com))
- pip or poetry

### 1. Setup Supabase

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Go to SQL Editor and run `supabase_schema.sql`
3. Get your credentials from Settings > API:
   - `SUPABASE_URL` (Project URL)
   - `SUPABASE_KEY` (anon/public key)
   - `SUPABASE_SERVICE_KEY` (service_role key)

### 2. Install Dependencies

```bash
cd backend
pip install -r ../requirements.txt
```

### 3. Configure Environment

```bash
# Copy example env file
cp ../.env.example ../.env

# Edit .env and add your Supabase credentials
```

Your `.env` should look like:
```env
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
SUPABASE_KEY=your_anon_key_here
SUPABASE_SERVICE_KEY=your_service_role_key_here

API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=development

FRONTEND_URL=http://localhost:5500
VERCEL_URL=https://your-app.vercel.app
```

### 4. Run the API

```bash
# Development mode with auto-reload
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

## 📁 Project Structure

```
backend/
├── main.py                    # FastAPI application entry point
├── app/
│   ├── config.py             # Configuration settings
│   ├── database.py           # Supabase connection & operations
│   ├── routers/              # API endpoints
│   │   ├── trends.py        # Trends endpoints
│   │   ├── regional.py      # Regional trends
│   │   ├── seasonal.py      # Seasonal intelligence
│   │   ├── competitors.py   # Competitor analysis
│   │   ├── recommendations.py  # AI recommendations
│   │   └── attributes.py    # Attribute analyzer
│   └── services/
│       ├── scheduler.py     # Background jobs
│       └── scraper.py       # Web scraping service
└── supabase_schema.sql      # Database schema
```

## 🔌 API Endpoints

### Health & Status
- `GET /` - API health check
- `GET /health` - Detailed health status

### Trends
- `GET /api/trends/` - Get all trends
- `GET /api/trends/trending` - Get currently trending items
- `GET /api/trends/kpis` - Get dashboard KPIs
- `GET /api/trends/action-board` - Get production recommendations
- `GET /api/trends/categories` - Get trend categories

### Regional
- `GET /api/regional/countries` - Get available countries
- `GET /api/regional/states?country=in` - Get states for country
- `GET /api/regional/trends?country=in&state=mh` - Get regional trends
- `GET /api/regional/growth?country=in&state=mh` - Get growth metrics

### Seasonal
- `GET /api/seasonal/current` - Get current season
- `GET /api/seasonal/trends?season=Spring&year=2025` - Get seasonal trends
- `GET /api/seasonal/forecast?season=Fall` - Get seasonal forecast

### Competitors
- `GET /api/competitors/` - Get competitor list
- `GET /api/competitors/{id}` - Get competitor details
- `GET /api/competitors/trends/comparison` - Compare trends

### Recommendations
- `GET /api/recommendations/` - Get AI recommendations
- `GET /api/recommendations/{id}` - Get recommendation details
- `POST /api/recommendations/feedback` - Submit feedback

### Attributes
- `GET /api/attributes/categories` - Get attribute categories
- `GET /api/attributes/analyze?category=colors` - Analyze attributes
- `GET /api/attributes/correlations?attribute=Sage Green` - Get correlations
- `GET /api/attributes/emerging` - Get emerging attributes

## 🗄️ Database Schema

Tables:
- `trends` - Fashion trends data
- `regional_trends` - Region-specific trends
- `seasonal_trends` - Seasonal fashion data
- `competitors` - Competitor information
- `recommendations` - AI-generated recommendations
- `attributes` - Fashion attributes (colors, fabrics, etc.)
- `recommendation_feedback` - User feedback on recommendations

See `supabase_schema.sql` for complete schema.

## 🔄 Background Jobs

The API runs scheduled jobs:
- **Trend Scraping**: Every 6 hours (scrapes fashion websites)
- **Analytics Update**: Every hour (calculates momentum scores)

Configure in `app/services/scheduler.py`

## 🌐 CORS Configuration

The API accepts requests from:
- `http://localhost:3000`
- `http://localhost:5500`
- Your Vercel deployment URL

Update CORS origins in `main.py` for production.

## 🚀 Deploy to Production

### Option 1: Render.com (Recommended)

1. Create account at [render.com](https://render.com)
2. New Web Service > Connect your GitHub repo
3. Select `backend` directory
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables from `.env`

### Option 2: Railway.app

1. Create account at [railway.app](https://railway.app)
2. New Project > Deploy from GitHub
3. Add environment variables
4. Railway will auto-detect Python and deploy

### Option 3: Fly.io

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Deploy
cd backend
fly launch
fly deploy
```

## 📊 Monitoring

- View logs: Check your hosting platform dashboard
- Database: Monitor in Supabase dashboard
- API health: `GET /health` endpoint

## 🔐 Security Notes

- Store API keys in `.env`, never commit them
- Use `SUPABASE_SERVICE_KEY` only server-side
- Implement rate limiting for production
- Restrict CORS origins in production
- Enable Supabase RLS policies for production

## 🛠️ Development Tips

```bash
# Install dev dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest

# Format code
black app/

# Type checking
mypy app/
```

## 📝 Next Steps

1. ✅ Setup Supabase database
2. ✅ Configure environment variables
3. ✅ Run API locally
4. 🔄 Implement real web scraping
5. 🔄 Add authentication
6. 🔄 Deploy to production
7. 🔄 Connect frontend to API

## 🐛 Troubleshooting

**Import errors:**
```bash
pip install -r requirements.txt
```

**Supabase connection fails:**
- Check your credentials in `.env`
- Verify Supabase project is active
- Check if tables exist (run `supabase_schema.sql`)

**CORS errors:**
- Add your frontend URL to `allow_origins` in `main.py`

**Port already in use:**
```bash
# Change port in .env or run:
uvicorn main:app --port 8001
```

## 📞 Support

For issues, check:
- FastAPI docs: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- Supabase docs: [supabase.com/docs](https://supabase.com/docs)

## 📄 License

MIT License - See LICENSE file
