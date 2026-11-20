/**
 * Pandemic Dashboard Fallback Implementation
 * Uses Chart.js to provide a simplified version of the pandemic response model
 * when WASM/Voici is not available or fails to load
 */

class PandemicDashboardFallback {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.parameters = {
            uPfac: 0.89,
            stimulus: 1.2,
            bonusUnemp: 5.2,
            lspell: 2.0
        };
        
        if (this.container) {
            this.init();
        }
    }
    
    init() {
        this.createFallbackUI();
        this.initializeCharts();
        this.setupControls();
    }
    
    createFallbackUI() {
        this.container.innerHTML = `
            <div class="grid grid-cols-2 gap-8">
                <div class="space-y-6">
                    <canvas id="unemployment-fallback-chart" width="400" height="300"></canvas>
                    <canvas id="consumption-fallback-chart" width="400" height="300"></canvas>
                </div>
                <div class="space-y-6">
                    <div class="space-y-4 controls">
                        <div>
                            <label class="block text-sm font-medium mb-2">Unavoidable Spending Reduction</label>
                            <input type="range" class="slider w-full" 
                                   min="0.8" max="1.0" step="0.01" value="0.89"
                                   id="uPfac-slider">
                            <div class="text-xs text-gray-500 mt-1">Current: <span id="uPfac-value">0.89</span></div>
                        </div>
                        <div>
                            <label class="block text-sm font-medium mb-2">Maximum Stimulus ($1000s)</label>
                            <input type="range" class="slider w-full" 
                                   min="0.2" max="2.2" step="0.1" value="1.2"
                                   id="stimulus-slider">
                            <div class="text-xs text-gray-500 mt-1">Current: <span id="stimulus-value">1.2</span></div>
                        </div>
                        <div>
                            <label class="block text-sm font-medium mb-2">Unemployment Benefits Bonus</label>
                            <input type="range" class="slider w-full" 
                                   min="3.0" max="7.0" step="0.2" value="5.2"
                                   id="bonus-slider">
                            <div class="text-xs text-gray-500 mt-1">Current: <span id="bonus-value">5.2</span></div>
                        </div>
                        <div>
                            <label class="block text-sm font-medium mb-2">Lockdown Duration (Quarters)</label>
                            <input type="range" class="slider w-full" 
                                   min="1.0" max="5.0" step="0.2" value="2.0"
                                   id="lockdown-slider">
                            <div class="text-xs text-gray-500 mt-1">Current: <span id="lockdown-value">2.0</span></div>
                        </div>
                    </div>
                    
                    <div class="p-4 border rounded-lg" style="border-color: var(--econ-ark-red);">
                        <h4 class="font-bold mb-2" style="color: var(--econ-ark-red);">Key Results</h4>
                        <p class="text-sm">Peak Unemployment: <span id="peak-unemployment" class="font-bold">-</span>%</p>
                        <p class="text-sm">Consumption Drop: <span id="consumption-drop" class="font-bold">-</span>%</p>
                    </div>
                    
                    <div class="p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                        <p class="text-xs text-yellow-800">
                            <strong>Note:</strong> This is a simplified fallback version. 
                            <a href="https://mriduls.github.io/pandemic-voici/voici/render/dashboard.html" 
                               target="_blank" class="underline">
                                Open the full interactive dashboard
                            </a> for the complete experience.
                        </p>
                    </div>
                </div>
            </div>
        `;
    }
    
    initializeCharts() {
        // Unemployment Rate Chart
        const unempCtx = document.getElementById('unemployment-fallback-chart').getContext('2d');
        this.unemploymentChart = new Chart(unempCtx, {
            type: 'line',
            data: {
                labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'],
                datasets: [
                    {
                        label: 'Baseline',
                        data: [],
                        borderColor: '#6b7280',
                        backgroundColor: '#6b7280',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 2
                    },
                    {
                        label: 'Pandemic Response',
                        data: [],
                        borderColor: '#dc2626',
                        backgroundColor: '#dc2626',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 2
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 25,
                        title: {
                            display: true,
                            text: 'Unemployment Rate (%)'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Unemployment Rate Response',
                        font: { size: 14, weight: 'bold' }
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
        
        // Consumption Chart
        const consCtx = document.getElementById('consumption-fallback-chart').getContext('2d');
        this.consumptionChart = new Chart(consCtx, {
            type: 'line',
            data: {
                labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'],
                datasets: [
                    {
                        label: 'Baseline',
                        data: [],
                        borderColor: '#6b7280',
                        backgroundColor: '#6b7280',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 2
                    },
                    {
                        label: 'No Policy',
                        data: [],
                        borderColor: '#dc2626',
                        backgroundColor: '#dc2626',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 2,
                        borderDash: [5, 5]
                    },
                    {
                        label: 'With CARES Act',
                        data: [],
                        borderColor: '#2563eb',
                        backgroundColor: '#2563eb',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 2
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'Aggregate Consumption (Billion $)'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Aggregate Consumption Response',
                        font: { size: 14, weight: 'bold' }
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }
    
    setupControls() {
        const sliders = ['uPfac', 'stimulus', 'bonus', 'lockdown'];
        
        sliders.forEach(param => {
            const slider = document.getElementById(`${param}-slider`);
            const valueSpan = document.getElementById(`${param}-value`);
            
            if (slider && valueSpan) {
                slider.addEventListener('input', (e) => {
                    const value = parseFloat(e.target.value);
                    valueSpan.textContent = value.toFixed(2);
                    
                    // Map slider to parameter
                    if (param === 'uPfac') this.parameters.uPfac = value;
                    else if (param === 'stimulus') this.parameters.stimulus = value;
                    else if (param === 'bonus') this.parameters.bonusUnemp = value;
                    else if (param === 'lockdown') this.parameters.lspell = value;
                    
                    this.updateCharts();
                });
            }
        });
        
        // Initial update
        this.updateCharts();
    }
    
    updateCharts() {
        // Simplified pandemic response calculations
        const quarters = 8;
        const baselineUnemp = Array(quarters).fill(4.5); // Normal unemployment
        const baselineConsumption = Array(quarters).fill(2800); // Baseline consumption
        
        // Unemployment response
        const unempResponse = this.calculateUnemploymentResponse();
        const consumptionResponse = this.calculateConsumptionResponse();
        
        // Update unemployment chart
        this.unemploymentChart.data.datasets[0].data = baselineUnemp;
        this.unemploymentChart.data.datasets[1].data = unempResponse;
        this.unemploymentChart.update();
        
        // Update consumption chart
        this.consumptionChart.data.datasets[0].data = baselineConsumption;
        this.consumptionChart.data.datasets[1].data = consumptionResponse.noPolicy;
        this.consumptionChart.data.datasets[2].data = consumptionResponse.withPolicy;
        this.consumptionChart.update();
        
        // Update key results
        const peakUnemp = Math.max(...unempResponse);
        const minConsumption = Math.min(...consumptionResponse.withPolicy);
        const consumptionDrop = ((2800 - minConsumption) / 2800 * 100);
        
        document.getElementById('peak-unemployment').textContent = peakUnemp.toFixed(1);
        document.getElementById('consumption-drop').textContent = consumptionDrop.toFixed(1);
    }
    
    calculateUnemploymentResponse() {
        const { lspell, uPfac } = this.parameters;
        const impact = (1 - uPfac) * 40; // Scale impact
        
        return [
            4.5, // Q1: Pre-pandemic
            4.5 + impact * 0.8, // Q2: Peak impact
            4.5 + impact * Math.pow(0.7, lspell - 1), // Q3: Recovery begins
            4.5 + impact * Math.pow(0.5, lspell),
            4.5 + impact * Math.pow(0.3, lspell),
            4.5 + impact * Math.pow(0.2, lspell),
            4.5 + impact * Math.pow(0.1, lspell),
            4.5 + impact * Math.pow(0.05, lspell)
        ];
    }
    
    calculateConsumptionResponse() {
        const { uPfac, stimulus, bonusUnemp } = this.parameters;
        const baseline = 2800;
        const impactMultiplier = (1 - uPfac) * 0.3;
        
        // No policy response
        const noPolicy = [
            baseline,
            baseline * (1 - impactMultiplier * 0.8),
            baseline * (1 - impactMultiplier * 0.9),
            baseline * (1 - impactMultiplier * 0.7),
            baseline * (1 - impactMultiplier * 0.5),
            baseline * (1 - impactMultiplier * 0.3),
            baseline * (1 - impactMultiplier * 0.2),
            baseline * (1 - impactMultiplier * 0.1)
        ];
        
        // With policy response
        const policyBoost = (stimulus + bonusUnemp) * 0.1;
        const withPolicy = noPolicy.map((value, index) => {
            if (index >= 1 && index <= 4) { // Policy active Q2-Q5
                return value + policyBoost * baseline * Math.pow(0.8, index - 1);
            }
            return value;
        });
        
        return { noPolicy, withPolicy };
    }
}

// Export for use in main application
window.PandemicDashboardFallback = PandemicDashboardFallback; 