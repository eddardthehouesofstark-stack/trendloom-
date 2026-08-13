-- TrendLoom Supabase Database Schema
-- Run this in your Supabase SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Trends table
CREATE TABLE IF NOT EXISTS trends (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    momentum_score DECIMAL(5,2) DEFAULT 0,
    status VARCHAR(50) DEFAULT 'active',
    description TEXT,
    image_url TEXT,
    source VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Regional trends table
CREATE TABLE IF NOT EXISTS regional_trends (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_code VARCHAR(10) NOT NULL,
    state_code VARCHAR(10),
    momentum_score DECIMAL(5,2) DEFAULT 0,
    image_url TEXT,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Seasonal trends table
CREATE TABLE IF NOT EXISTS seasonal_trends (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    season VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    category VARCHAR(100),
    momentum_score DECIMAL(5,2) DEFAULT 0,
    forecast_confidence DECIMAL(5,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Competitor data table
CREATE TABLE IF NOT EXISTS competitors (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    market_share DECIMAL(5,2),
    trend_score INTEGER,
    pricing_strategy VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Recommendations table
CREATE TABLE IF NOT EXISTS recommendations (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    priority VARCHAR(50),
    confidence INTEGER,
    reasoning TEXT,
    suggested_action TEXT,
    expected_roi VARCHAR(50),
    time_horizon VARCHAR(100),
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Attributes table
CREATE TABLE IF NOT EXISTS attributes (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    momentum_score DECIMAL(5,2) DEFAULT 0,
    trend VARCHAR(50),
    prevalence VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Feedback table (for recommendation outcomes)
CREATE TABLE IF NOT EXISTS recommendation_feedback (
    id BIGSERIAL PRIMARY KEY,
    recommendation_id BIGINT REFERENCES recommendations(id),
    action_taken VARCHAR(255),
    outcome TEXT,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better query performance
CREATE INDEX idx_trends_category ON trends(category);
CREATE INDEX idx_trends_status ON trends(status);
CREATE INDEX idx_trends_momentum ON trends(momentum_score DESC);
CREATE INDEX idx_regional_country ON regional_trends(country_code);
CREATE INDEX idx_regional_state ON regional_trends(state_code);
CREATE INDEX idx_seasonal_season_year ON seasonal_trends(season, year);
CREATE INDEX idx_attributes_category ON attributes(category);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply updated_at triggers to all tables
CREATE TRIGGER update_trends_updated_at BEFORE UPDATE ON trends
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_regional_trends_updated_at BEFORE UPDATE ON regional_trends
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_seasonal_trends_updated_at BEFORE UPDATE ON seasonal_trends
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_competitors_updated_at BEFORE UPDATE ON competitors
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_recommendations_updated_at BEFORE UPDATE ON recommendations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_attributes_updated_at BEFORE UPDATE ON attributes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert sample data
INSERT INTO trends (name, category, momentum_score, status, description) VALUES
('Oversized Blazers', 'Tailoring', 92, 'trending', 'Classic tailoring with contemporary oversized fit'),
('Sheer Layers', 'Textiles', 85, 'trending', 'Delicate sheer fabrics for layering'),
('Wide-Leg Trousers', 'Tailoring', 90, 'trending', 'Comfortable wide-leg silhouettes gaining momentum'),
('Sustainable Denim', 'Denim', 88, 'trending', 'Eco-friendly denim production methods'),
('Chunky Knits', 'Knitwear', 83, 'stable', 'Oversized knitwear pieces');

INSERT INTO regional_trends (name, country_code, state_code, momentum_score) VALUES
('Bandra Streetstyle', 'in', 'mh', 95),
('Delhi Contemporary', 'in', 'dl', 88),
('Parisian Chic', 'fr', NULL, 92),
('Tokyo Minimalist', 'jp', NULL, 89),
('Dubai Luxury', 'ae', NULL, 87);

INSERT INTO attributes (name, category, momentum_score, trend, prevalence) VALUES
('Sage Green', 'colors', 94, 'rising', '18%'),
('Butter Yellow', 'colors', 88, 'rising', '15%'),
('Linen Blends', 'fabrics', 91, 'rising', '24%'),
('Oversized', 'silhouettes', 93, 'rising', '34%'),
('Wide-Leg', 'silhouettes', 90, 'rising', '28%');

-- Enable Row Level Security (RLS)
ALTER TABLE trends ENABLE ROW LEVEL SECURITY;
ALTER TABLE regional_trends ENABLE ROW LEVEL SECURITY;
ALTER TABLE seasonal_trends ENABLE ROW LEVEL SECURITY;
ALTER TABLE competitors ENABLE ROW LEVEL SECURITY;
ALTER TABLE recommendations ENABLE ROW LEVEL SECURITY;
ALTER TABLE attributes ENABLE ROW LEVEL SECURITY;

-- Create policies (allow all for now - restrict in production)
CREATE POLICY "Allow all operations" ON trends FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON regional_trends FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON seasonal_trends FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON competitors FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON recommendations FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON attributes FOR ALL USING (true);
CREATE POLICY "Allow all operations" ON recommendation_feedback FOR ALL USING (true);
