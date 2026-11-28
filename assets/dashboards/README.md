# Pandemic Dashboard Integration

This directory contains the pandemic dashboard implementation for the Econ-ARK Central Bank Journey page.

## Overview

The pandemic dashboard integration provides interactive economic modeling based on Carroll et al. (2020) "Modeling the Consumption Response to the CARES Act". It leverages Mridul Seth's WASM implementation using Voici for the main dashboard, with a Chart.js fallback for broader compatibility.

## Implementation Strategy

### Primary Implementation: WASM/Voici
- **Source**: https://mriduls.github.io/pandemic-voici/voici/render/dashboard.html
- **Technology**: Voici (JupyterLite + WASM)
- **Advantages**: Full interactive notebook experience, no server required
- **Loading**: May take 10-30 seconds on first load due to WASM dependencies

### Fallback Implementation: Chart.js
- **Location**: `/assets/js/pandemic-fallback.js`
- **Technology**: Chart.js (same as existing dashboards)
- **Advantages**: Fast loading, consistent with site technology stack
- **Limitations**: Simplified model with fewer parameters

## Integration Points

### 1. Central Bank Journey Page
- **Location**: `pages/journeys/central-bank.html`
- **Integration**: Third tab in existing dashboard component
- **User Experience**: Seamless integration with existing HANK dashboards

### 2. Tab Structure
```
- Impulse Response (existing)
- Wealth Distribution (existing)  
- Pandemic Policy Response (new)
```

### 3. JavaScript Integration
- Added `initPandemicModeling()` to dashboard initialization
- Progressive loading with error handling
- Fallback activation if WASM fails

## Technical Implementation

### Key Features
1. **Progressive Enhancement**: WASM when supported, Chart.js when not
2. **Loading States**: Visual feedback during WASM initialization
3. **Error Handling**: Graceful degradation with helpful messages
4. **Brand Consistency**: Matches Econ-ARK design system

### File Structure
```
econ-ark.org/
├── assets/
│   ├── dashboards/
│   │   ├── embedded/          # Future: Custom embedded versions
│   │   ├── standalone/        # Future: Self-hosted full dashboards
│   │   └── README.md         # This file
│   └── js/
│       └── pandemic-fallback.js  # Chart.js fallback implementation
└── pages/journeys/
    └── central-bank.html      # Main integration point
```

## Future Enhancements

### Phase 2: Custom Embedded Version
- Brand-styled notebook using Voici templates
- Reduced parameter set for embedding
- Custom CSS injection for seamless integration

### Phase 3: Build Pipeline
- Automated dashboard generation from source notebooks
- GitHub Actions for continuous deployment
- Version management for dashboard updates

## Testing

### Local Development
1. Start Jekyll: `docker-compose up`
2. Navigate to: http://localhost:4000/pages/journeys/central-bank.html
3. Click "Pandemic Policy Response" tab
4. Test both WASM and fallback implementations

### Fallback Testing
To test the Chart.js fallback:
1. Block the WASM dashboard URL in browser dev tools
2. Reload the page
3. The fallback should activate automatically

## Parameters

### WASM Dashboard (Full)
Based on `param_desc.yaml` from the Pandemic repository:
- Unavoidable spending reduction (`uPfac_L`)
- Lockdown duration (`Lspell_real`, `Lspell_pcvd`)
- Deep unemployment severity (`Deep0`, `DeepD`, `DeepH`, `DeepC`)
- Stimulus parameters (`StimMax`, `StimCut0`, `StimCut1`)
- Unemployment benefits (`BonusUnemp`, `BonusDeep`)
- And many more...

### Fallback Dashboard (Simplified)
- Unavoidable Spending Reduction (0.8-1.0)
- Maximum Stimulus ($200-$2200)  
- Unemployment Benefits Bonus (3.0-7.0)
- Lockdown Duration (1.0-5.0 quarters)

## Dependencies

### Primary (WASM)
- Voici dashboard (external, hosted by Mridul)
- Modern browser with WASM support

### Fallback
- Chart.js (already loaded on page)
- ES6+ JavaScript support

## References

1. [Pandemic Paper](http://econ-ark.github.io/Pandemic) - Carroll et al. (2020)
2. [Mridul's WASM Dashboard](https://mriduls.github.io/pandemic-voici/voici/render/dashboard.html)
3. [Voici Documentation](https://voici.readthedocs.io/)
4. [Original Repository](https://github.com/econ-ark/Pandemic) 