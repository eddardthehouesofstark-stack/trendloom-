# TrendLoom - Fashion Intelligence Dashboard

A sophisticated **real-time** fashion intelligence platform that helps decision-makers turn market signals into confident production decisions with AI-powered global trend analysis.

## 🌟 Features

### Frontend (7 Pages)
- **Dashboard**: Executive overview with real-time KPIs, action board, and trending insights
- **Explore Trends**: Discover emerging fashion trends globally
- **Seasonal Intelligence**: Seasonal trend analysis and AI predictions
- **Regional Demand**: Localized design trends with country/state filtering (10+ regions)
- **Competitor Trends**: Track competitor movements and market positioning
- **Recommendations**: AI-powered production recommendations with ROI forecasting
- **Attribute Analyzer**: Deep dive into fashion attributes (colors, fabrics, patterns)

### Backend (FastAPI + Supabase)
- **Real-time API**: FastAPI REST endpoints for all features
- **Database**: Supabase PostgreSQL with 7 tables
- **Auto-scraping**: Scheduled jobs to fetch trend data every 6 hours
- **Analytics**: Momentum scoring, trend detection, forecasting
- **WebSocket**: Real-time updates (coming soon)

## 🏗️ Architecture

```
TrendLoom/
├── frontend/              # HTML/CSS/JavaScript
│   ├── *.html            # 7 dashboard pages
│   └── js/
│       ├── api.js        # API client
│       └── dashboard.js  # Real-time data binding
├── backend/              # Python FastAPI
│   ├── main.py          # API entry point
│   ├── app/
│   │   ├── routers/     # API endpoints
│   │   ├── services/    # Business logic
│   │   └── database.py  # Supabase integration
│   └── supabase_schema.sql
├── requirements.txt      # Python dependencies
└── SETUP_GUIDE.md       # Complete setup instructions
```

## 🚀 Quick Start

### 1. Clone & Setup Database

```bash
# Clone repository
git clone https://github.com/eddardthehouesofstark-stack/trendloom-.git
cd trendloom-

# Setup Supabase (see SETUP_GUIDE.md)
# Run backend/supabase_schema.sql in Supabase SQL Editor
```

### 2. Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Supabase credentials

# Run API
cd backend
python main.py
```

API will be at: http://localhost:8000

### 3. Frontend Setup

```bash
# Just open in browser!
cd frontend
open dashboard.html

# Or use Live Server in VS Code
```

**See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions**

## 🛠️ Tech Stack

### Frontend
- HTML5, CSS3, JavaScript (Vanilla)
- Tailwind CSS 3.x
- Google Fonts (Inter, Playfair Display)
- Material Symbols Icons

### Backend
- **Python 3.9+**
- **FastAPI** - Modern REST API framework
- **Supabase** - PostgreSQL database
- **BeautifulSoup** - Web scraping
- **APScheduler** - Background jobs
- **Uvicorn** - ASGI server

### Infrastructure
- **Frontend**: Vercel
- **Backend**: Render.com / Railway
- **Database**: Supabase
- **CI/CD**: GitHub Actions

## 📡 API Endpoints

### Trends
- `GET /api/trends/` - Get all trends
- `GET /api/trends/trending` - Currently trending items
- `GET /api/trends/kpis` - Dashboard KPIs
- `GET /api/trends/action-board` - Production recommendations

### Regional
- `GET /api/regional/countries` - Available countries
- `GET /api/regional/states?country=in` - States by country
- `GET /api/regional/trends?country=in&state=mh` - Regional trends

### Seasonal
- `GET /api/seasonal/current` - Current season
- `GET /api/seasonal/trends?season=Spring` - Seasonal trends
- `GET /api/seasonal/forecast?season=Fall` - Season forecast

### More
- Competitors, Recommendations, Attributes (see [API Docs](http://localhost:8000/docs))

## 📊 Database Schema

- `trends` - Fashion trends data
- `regional_trends` - Region-specific trends
- `seasonal_trends` - Seasonal fashion data
- `competitors` - Competitor information
- `recommendations` - AI recommendations
- `attributes` - Fashion attributes
- `recommendation_feedback` - User feedback

## 🎨 Design System

- **Primary Colors**: Navy (#0a192f), Teal (#0D9488), Cream (#F9F7F2)
- **Typography**: Playfair Display (headings), Inter (body)
- **Layout**: Consistent sidebar navigation across all pages
- **Components**: Glass-card styling with grain overlay effects
- **Responsive**: Mobile-first design with desktop optimizations

## 📱 Pages

1. `dashboard.html` - Main executive dashboard with real-time KPIs
2. `exploretrens.html` - Trend exploration interface
3. `seasonal.html` - Seasonal intelligence analysis
4. `regional.html` - Regional demand with country/state selectors
5. `comp.html` - Competitor trends tracking
6. `suggestion.html` - AI-powered recommendations
7. `attributes.html` - Attribute analyzer (colors, fabrics, patterns)

## 🌐 Live Demo

- **Frontend**: https://your-app.vercel.app (Update after deployment)
- **API Docs**: https://your-api.onrender.com/docs
- **GitHub**: https://github.com/eddardthehouesofstark-stack/trendloom-

## 🔒 Environment Variables

```env
# Backend (.env)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=your_anon_key
SUPABASE_SERVICE_KEY=your_service_key
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=production
```

## 🧪 Testing

```bash
# Test backend
curl http://localhost:8000/health
curl http://localhost:8000/api/trends/

# Test frontend
# Open browser console and run:
TrendLoomAPI.healthCheck().then(console.log)
```

## 📦 Deployment

### Backend (Render.com)
1. Connect GitHub repo
2. Set root directory to `backend`
3. Build: `pip install -r ../requirements.txt`
4. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables

### Frontend (Vercel) ✅
Already deployed! Just push to main branch.

**Detailed deployment guide**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)

## 🛣️ Roadmap

- [x] Frontend UI (7 pages)
- [x] Backend API (FastAPI)
- [x] Database (Supabase)
- [x] Real-time data integration
- [ ] Web scraping implementation
- [ ] AI/ML trend prediction
- [ ] User authentication
- [ ] Email alerts
- [ ] Mobile app

## 🐛 Issues & Support

Found a bug? [Open an issue](https://github.com/eddardthehouesofstark-stack/trendloom-/issues)

## 📄 License

MIT License - See LICENSE file

## 👥 Author

**Praga** - [GitHub](https://github.com/eddardthehouesofstark-stack)

---

Built with ❤️ for SRCAS Hackathon
