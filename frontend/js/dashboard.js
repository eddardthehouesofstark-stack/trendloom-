/**
 * Dashboard Real-Time Data Integration
 * Connects dashboard.html to the FastAPI backend
 */

document.addEventListener('DOMContentLoaded', async () => {
    console.log('📊 Loading dashboard data...');

    try {
        // Load KPIs
        await loadKPIs();

        // Load Action Board
        await loadActionBoard();

        // Load Trending Now
        await loadTrendingNow();

        console.log('✅ Dashboard data loaded successfully');
    } catch (error) {
        console.error('❌ Failed to load dashboard data:', error);
        showErrorNotification('Failed to load real-time data. Using cached data.');
    }
});

/**
 * Load KPI metrics
 */
async function loadKPIs() {
    try {
        const response = await api.getKPIs();
        
        if (response.success) {
            const data = response.data;

            // Update Market Coverage
            updateKPI('market-coverage', data.market_coverage, data.market_coverage_change);

            // Update Trend Accuracy
            updateKPI('trend-accuracy', data.trend_accuracy, data.trend_accuracy_change);

            // Update Signal Strength
            updateKPI('signal-strength', data.signal_strength);

            // Update Active Signals
            updateKPI('active-signals', data.active_signals);
        }
    } catch (error) {
        console.error('Error loading KPIs:', error);
    }
}

/**
 * Update KPI value in the DOM
 */
function updateKPI(kpiId, value, change = null) {
    const element = document.getElementById(kpiId);
    if (element) {
        element.textContent = typeof value === 'number' ? `${value}%` : value;
    }

    if (change !== null) {
        const changeElement = document.getElementById(`${kpiId}-change`);
        if (changeElement) {
            changeElement.textContent = `${change > 0 ? '+' : ''}${change}%`;
        }
    }
}

/**
 * Load Action Board recommendations
 */
async function loadActionBoard() {
    try {
        const response = await api.getActionBoard();
        
        if (response.success && response.data) {
            const actionBoardContainer = document.getElementById('action-board-container');
            
            if (!actionBoardContainer) return;

            actionBoardContainer.innerHTML = '';

            response.data.forEach(item => {
                const card = createActionCard(item);
                actionBoardContainer.appendChild(card);
            });
        }
    } catch (error) {
        console.error('Error loading action board:', error);
    }
}

/**
 * Create action board card element
 */
function createActionCard(item) {
    const card = document.createElement('div');
    card.className = `bg-surface/10 rounded-xl p-4 border border-surface/${item.category === 'PRODUCE NOW' ? '20' : '10'}`;

    const statusColors = {
        'PRODUCE NOW': 'brand-sage',
        'WAIT / MONITOR': 'yellow-500/20',
        'AVOID': 'brand-coral/20'
    };

    card.innerHTML = `
        <div class="flex items-center gap-2 mb-2">
            <span class="bg-${statusColors[item.category]} text-${item.color === 'green' ? 'brand-navy' : 'white'} font-bold text-[10px] px-2 py-1 rounded-sm tracking-wider">${item.category}</span>
            <span class="font-label-sm text-outline-variant">${item.certainty}% Certainty</span>
        </div>
        <h4 class="font-headline-md text-lg">${item.name}</h4>
        ${item.note ? `<p class="text-sm text-outline-variant mt-1">${item.note}</p>` : ''}
        <div class="mt-3 flex items-center justify-between text-sm text-outline-variant">
            <span>Momentum</span>
            <div class="w-1/2 bg-surface/20 h-1.5 rounded-full overflow-hidden">
                <div class="bg-${item.color === 'green' ? 'brand-sage' : item.color === 'yellow' ? 'yellow-400' : 'brand-coral'} h-full" style="width: ${item.momentum}%"></div>
            </div>
        </div>
    `;

    return card;
}

/**
 * Load trending items
 */
async function loadTrendingNow() {
    try {
        const response = await api.getTrendingNow(4);
        
        if (response.success && response.data) {
            const trendingContainer = document.getElementById('trending-container');
            
            if (!trendingContainer) return;

            // Update existing trend cards with real data
            const trendCards = trendingContainer.querySelectorAll('.trend-card');
            
            response.data.forEach((trend, index) => {
                if (trendCards[index]) {
                    updateTrendCard(trendCards[index], trend);
                }
            });
        }
    } catch (error) {
        console.error('Error loading trending items:', error);
    }
}

/**
 * Update trend card with real data
 */
function updateTrendCard(card, trend) {
    const titleElement = card.querySelector('.trend-title');
    const statusElement = card.querySelector('.trend-status');

    if (titleElement) {
        titleElement.textContent = trend.name;
    }

    if (statusElement && trend.status) {
        statusElement.textContent = trend.status.toUpperCase();
    }
}

/**
 * Show error notification
 */
function showErrorNotification(message) {
    // Create a simple notification
    const notification = document.createElement('div');
    notification.className = 'fixed top-4 right-4 bg-error-container text-on-error-container px-6 py-3 rounded-lg shadow-lg z-50';
    notification.textContent = message;

    document.body.appendChild(notification);

    // Remove after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

/**
 * Refresh dashboard data periodically
 */
function startAutoRefresh(intervalMinutes = 5) {
    setInterval(async () => {
        console.log('🔄 Refreshing dashboard data...');
        await loadKPIs();
        await loadTrendingNow();
    }, intervalMinutes * 60 * 1000);
}

// Start auto-refresh every 5 minutes
startAutoRefresh(5);
