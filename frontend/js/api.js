/**
 * TrendLoom API Client
 * Connects frontend to FastAPI backend
 */

// API Configuration
const API_CONFIG = {
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://your-backend-api.render.com', // Update with your deployed API URL
    timeout: 10000
};

/**
 * API Client Class
 */
class TrendLoomAPI {
    constructor(baseURL = API_CONFIG.baseURL) {
        this.baseURL = baseURL;
    }

    /**
     * Make API request
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers,
                },
            });

            if (!response.ok) {
                throw new Error(`API Error: ${response.status} ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Request failed:', error);
            throw error;
        }
    }

    // ============ TRENDS API ============
    
    async getTrends(limit = 100) {
        return this.request(`/api/trends/?limit=${limit}`);
    }

    async getTrendingNow(limit = 10) {
        return this.request(`/api/trends/trending?limit=${limit}`);
    }

    async getKPIs() {
        return this.request('/api/trends/kpis');
    }

    async getActionBoard() {
        return this.request('/api/trends/action-board');
    }

    async getCategories() {
        return this.request('/api/trends/categories');
    }

    // ============ REGIONAL API ============
    
    async getCountries() {
        return this.request('/api/regional/countries');
    }

    async getStates(countryCode) {
        return this.request(`/api/regional/states?country=${countryCode}`);
    }

    async getRegionalTrends(countryCode, stateCode = null, limit = 10) {
        let url = `/api/regional/trends?country=${countryCode}&limit=${limit}`;
        if (stateCode) url += `&state=${stateCode}`;
        return this.request(url);
    }

    async getRegionalGrowth(countryCode, stateCode = null) {
        let url = `/api/regional/growth?country=${countryCode}`;
        if (stateCode) url += `&state=${stateCode}`;
        return this.request(url);
    }

    // ============ SEASONAL API ============
    
    async getCurrentSeason() {
        return this.request('/api/seasonal/current');
    }

    async getSeasonalTrends(season, year, limit = 20) {
        return this.request(`/api/seasonal/trends?season=${season}&year=${year}&limit=${limit}`);
    }

    async getSeasonalForecast(season, year) {
        return this.request(`/api/seasonal/forecast?season=${season}&year=${year}`);
    }

    // ============ COMPETITORS API ============
    
    async getCompetitors(limit = 10) {
        return this.request(`/api/competitors/?limit=${limit}`);
    }

    async getCompetitorDetail(competitorId) {
        return this.request(`/api/competitors/${competitorId}`);
    }

    async compareTrends(competitorIds) {
        return this.request(`/api/competitors/trends/comparison?competitors=${competitorIds.join(',')}`);
    }

    // ============ RECOMMENDATIONS API ============
    
    async getRecommendations(category = null, limit = 10) {
        let url = `/api/recommendations/?limit=${limit}`;
        if (category) url += `&category=${category}`;
        return this.request(url);
    }

    async getRecommendationDetail(recommendationId) {
        return this.request(`/api/recommendations/${recommendationId}`);
    }

    async submitFeedback(recommendationId, actionTaken, outcome = null) {
        return this.request('/api/recommendations/feedback', {
            method: 'POST',
            body: JSON.stringify({
                recommendation_id: recommendationId,
                action_taken: actionTaken,
                outcome: outcome
            })
        });
    }

    // ============ ATTRIBUTES API ============
    
    async getAttributeCategories() {
        return this.request('/api/attributes/categories');
    }

    async analyzeAttributes(category, timeRange = '30d') {
        return this.request(`/api/attributes/analyze?category=${category}&time_range=${timeRange}`);
    }

    async getAttributeCorrelations(attribute) {
        return this.request(`/api/attributes/correlations?attribute=${encodeURIComponent(attribute)}`);
    }

    async getEmergingAttributes(limit = 10) {
        return this.request(`/api/attributes/emerging?limit=${limit}`);
    }

    // ============ HEALTH CHECK ============
    
    async healthCheck() {
        return this.request('/health');
    }
}

// Create global API instance
const api = new TrendLoomAPI();

// Export for use in HTML files
window.TrendLoomAPI = api;

console.log('🔌 TrendLoom API Client loaded');
