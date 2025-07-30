# 🚨 P2P Crypto Crisis Impact Analysis - Project Structure

## 📁 **Current Codebase Structure**

```doc
cryptoAnalysis/
├── 📊 config/
│   └── countries.yml                    # Target country profiles
├── 📈 data/                            # All CSV data storage
│   ├── raw/                            # Daily scraped data by platform
│   │   └── 2025-07-29/
│   │       └── binance_p2p_SD_2025-07-29.csv
│   ├── processed/                      # Analyzed and aggregated data
│   │   ├── daily_summaries/
│   │   ├── premium_calculations/
│   │   └── country_aggregates/
│   ├── exchange_rates/                 # Official fiat exchange rates
│   ├── analysis/                       # Crisis analysis data
│   │   ├── crisis_timeline.csv         # Master crisis events
│   │   ├── crisis_timeline_SD.csv      # Sudan events
│   │   ├── crisis_timeline_AF.csv      # Afghanistan events
│   │   ├── crisis_timeline_VE.csv      # Venezuela events
│   │   ├── crisis_timeline_NG.csv      # Nigeria events
│   │   ├── crisis_timeline_ZW.csv      # Zimbabwe events
│   │   └── crisis_timeline_AR.csv      # Argentina events
│   └── metadata/                       # Collection logs
│       └── collection_log.csv
├── 🔍 scrapers/                       # Data collection infrastructure
│   ├── binance_p2p.py                 # Binance P2P scraper (WORKING)
│   ├── data_orchestrator.py           # Master collection coordinator
│   └── platforms/                      # Platform-specific scrapers
│       ├── okx_p2p.py                  # OKX P2P scraper
│       └── paxful_historical.py       # Historical Paxful data
├── 🧪 utils/                          # Core utilities
│   ├── country_profiles.py            # Country profile loader (WORKING)
│   ├── csv_data_manager.py            # CSV storage manager (WORKING)
│   ├── exchange_rates.py              # Exchange rate collection
│   ├── data_viewer.py                 # Data exploration tool (WORKING)
│   └── test_country_profiles.py       # Test suite (WORKING)
├── 📊 analysis/                       # Crisis impact analysis
│   └── crisis_timeline.py             # Crisis event definitions (WORKING)
├── 📋 README.md                       # Project documentation
├── 📋 milestone_1_scoping.md          # Phase 1 documentation
└── 📋 requirements.txt                # Python dependencies
```

## 🎯 **Crisis Impact Analysis Framework**

### **Target Crisis Events (21 Total)**

#### 🔥 **HIGH PRIORITY (13 events)**

- **Sudan**: 4 major crises (2019 revolution → 2023 war)
- **Afghanistan**: 3 major crises (2021 Taliban takeover)  
- **Nigeria**: 2 major crises (2021 crypto ban, 2023 naira crisis)
- **Argentina**: 2 major crises (2019 peso crash, 2020 capital controls)
- **Zimbabwe**: 1 major crisis (2020 hyperinflation return)
- **Venezuela**: 1 major crisis (2019 political crisis)

#### 📅 **MEDIUM PRIORITY (8 events)**

- Various supporting events and policy changes

### **Data Collection Strategy**

#### **Phase 2A: Current Market Baseline** ✅ READY

- Collect current P2P data from all platforms
- Establish present-day market conditions
- Get current exchange rates for premium calculations

#### **Phase 2B: Crisis Period Historical Data** 🔜 NEXT

- Focus on 13 high-priority crisis events
- Collect P2P data around crisis dates (±3 months)
- Gather corresponding exchange rates

#### **Phase 2C: Trend Analysis** 🔜 PLANNED

- Calculate price premiums during crises
- Analyze liquidity changes
- Study payment method shifts
- Measure crypto adoption acceleration

## 🛠️ **Available Data Collection Tools**

### ✅ **READY TO USE**

1. **Binance P2P Scraper** - Live data collection working
2. **CSV Data Manager** - Complete storage system
3. **Country Profiles** - All 6 countries configured
4. **Crisis Timeline** - 21 events defined and prioritized
5. **Data Viewer** - Exploration and analysis tools

### 🧪 **TESTING REQUIRED**

1. **OKX P2P Scraper** - Built but needs testing
2. **Exchange Rate Collector** - Built but needs API keys
3. **Paxful Historical** - Built but relies on archived data
4. **Data Orchestrator** - Master coordination system

### 🎯 **ANALYSIS CAPABILITIES**

#### **Impact Metrics We Can Calculate**

- **Price Premiums**: Crypto price vs official exchange rate
- **Liquidity Changes**: Available volume before/during/after crises
- **Market Depth**: Number of active advertisers
- **Payment Method Evolution**: Shifts in preferred payment types
- **Geographic Patterns**: Country-specific adoption trends
- **Platform Comparison**: Which platforms served which crises

#### **Timeline Analysis**

- Pre-crisis baseline (6 months before)
- Crisis onset (event date ±2 weeks)
- Crisis period (during major instability)
- Post-crisis adaptation (6 months after)

## 📊 **Current Data Status**

### ✅ **Successfully Collected**

- **Sudan**: 106 current Binance P2P ads (6 buy, 100 sell)
- **Exchange Rate Example**: ~2,900 SDG per USDT vs ~600 official rate
- **Crisis Timeline**: All 21 events documented with sources

### 📈 **Ready for Analysis**

- Price premium calculation: **383% premium** in Sudan
- Payment methods: Bank of Khartoum, Faisal Islamic Bank dominance
- Market structure: Heavily sell-sided (people acquiring foreign currency)

## 🚀 **Next Steps (In Order)**

### **IMMEDIATE (Next Commands)**

1. **Test all scrapers**: Verify OKX and exchange rate collection
2. **Collect baseline data**: Run current snapshot for all 6 countries
3. **Set up exchange rates**: Get API keys and collect current rates

### **SHORT TERM (This Week)**

1. **Historical data collection**: Focus on top 5 crisis events
2. **Premium calculations**: Calculate crisis-period premiums
3. **Basic analysis**: Before/during/after crisis comparisons

### **MEDIUM TERM (Next Phase)**

1. **Comprehensive dataset**: All 21 crisis events analyzed
2. **Impact reporting**: Quantified stablecoin financial inclusion impact
3. **Visualization**: Charts showing crisis response patterns

---

## 💡 **Key Research Insights Already Emerging**

1. **Sudan Market Structure**: Heavily sell-sided, indicating people trying to exit SDG
2. **Price Premiums**: ~383% premium suggests severe currency stress
3. **Payment Methods**: Traditional banks still dominant despite crisis
4. **Platform Choice**: Binance appears to be primary platform for Sudan

This crisis-focused approach will clearly demonstrate how stablecoins provided financial lifelines during specific economic emergencies! 🎯
