#!/usr/bin/env python3
"""
Phase 3 Data Collection Coordinator
Author: Clement MUGISHA
Purpose: Methodical and coordinated data collection for crisis analysis

This script implements our systematic approach to collecting historical and current
cryptocurrency data for correlation with crisis events. Every data point collected
has a clear purpose in answering our research questions.
"""

import os
import sys
from datetime import datetime, timedelta
import pandas as pd

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

class Phase3DataCoordinator:
    """
    Coordinates methodical data collection for crisis correlation analysis.
    
    Purpose: Systematic data collection with clear objectives:
    1. Historical crypto prices for crisis correlation
    2. Current P2P premiums for validation
    3. Crisis timeline correlation analysis
    """
    
    def __init__(self):
        self.base_dir = project_root
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.today = datetime.now().strftime('%Y-%m-%d')
        
        # Ensure data directories exist
        self._ensure_data_structure()
        
        # Crisis events we want to analyze (from our documented timeline)
        self.crisis_events = [
            # Sudan crises
            {'country': 'SD', 'date': '2021-10-25', 'event': 'Military coup', 'severity': 'HIGH'},
            {'country': 'SD', 'date': '2019-04-11', 'event': 'Omar al-Bashir ousted', 'severity': 'HIGH'},
            
            # Venezuela crises
            {'country': 'VE', 'date': '2018-08-20', 'event': 'Currency redenomination', 'severity': 'HIGH'},
            {'country': 'VE', 'date': '2019-01-23', 'event': 'Juan Guaidó declares presidency', 'severity': 'MEDIUM'},
            
            # Argentina economic events
            {'country': 'AR', 'date': '2019-08-11', 'event': 'Peso devaluation after primary elections', 'severity': 'MEDIUM'},
            {'country': 'AR', 'date': '2020-04-22', 'event': 'Debt default announcement', 'severity': 'MEDIUM'},
            
            # Afghanistan crisis
            {'country': 'AF', 'date': '2021-08-15', 'event': 'Taliban takeover of Kabul', 'severity': 'HIGH'},
            
            # Nigeria events
            {'country': 'NG', 'date': '2020-10-20', 'event': 'Central bank restricts crypto', 'severity': 'MEDIUM'},
            
            # Zimbabwe events
            {'country': 'ZW', 'date': '2019-02-20', 'event': 'Currency crisis escalation', 'severity': 'HIGH'},
        ]
        
        print(f"🎯 Phase 3 Data Coordinator initialized")
        print(f"📊 Target crisis events: {len(self.crisis_events)}")
        print(f"📁 Data directory: {self.data_dir}")
    
    def _ensure_data_structure(self):
        """Create organized data directory structure."""
        directories = [
            'data/raw',
            'data/processed',
            'data/analysis',
            'data/historical',
            'data/historical/yahoo_finance',
            'data/historical/cryptocompare',
            'data/analysis/crisis_correlations',
            'data/analysis/reports'
        ]
        
        for directory in directories:
            path = os.path.join(self.base_dir, directory)
            os.makedirs(path, exist_ok=True)
    
    def collect_historical_baseline(self):
        """
        Step 1: Collect historical crypto price data for crisis correlation.
        
        Purpose: Get 10+ years of Bitcoin/crypto prices to correlate with our
        documented crisis events. This establishes the baseline for measuring
        crisis impact.
        """
        print("\n🔍 STEP 1: Historical Baseline Collection")
        print("Purpose: Establish crypto price baseline for crisis correlation")
        
        try:
            # Import yfinance for historical data
            import yfinance as yf
            
            # Target cryptocurrencies for analysis
            crypto_symbols = {
                'BTC-USD': 'Bitcoin',
                'ETH-USD': 'Ethereum', 
                'USDT-USD': 'Tether'
            }
            
            historical_data = {}
            
            for symbol, name in crypto_symbols.items():
                print(f"\n📈 Collecting {name} ({symbol}) historical data...")
                
                try:
                    # Get maximum available historical data
                    ticker = yf.Ticker(symbol)
                    history = ticker.history(period="max")
                    
                    if not history.empty:
                        start_date = history.index[0].strftime('%Y-%m-%d')
                        end_date = history.index[-1].strftime('%Y-%m-%d')
                        days = len(history)
                        
                        print(f"✅ {name}: {days} days ({start_date} to {end_date})")
                        
                        # Save historical data
                        filename = f"{symbol.replace('-', '_')}_historical.csv"
                        filepath = os.path.join(self.data_dir, 'historical', 'yahoo_finance', filename)
                        history.to_csv(filepath)
                        
                        historical_data[symbol] = {
                            'data': history,
                            'days': days,
                            'start_date': start_date,
                            'end_date': end_date,
                            'filepath': filepath
                        }
                        
                    else:
                        print(f"❌ {name}: No data available")
                        
                except Exception as e:
                    print(f"❌ Error collecting {name}: {e}")
            
            print(f"\n✅ Historical baseline collection complete")
            print(f"📊 Collected data for {len(historical_data)} cryptocurrencies")
            
            return historical_data
            
        except ImportError:
            print("❌ yfinance not installed. Installing...")
            os.system("python -m pip install --user yfinance")
            print("✅ Please run the script again after installation")
            return None
        except Exception as e:
            print(f"❌ Error in historical collection: {e}")
            return None
    
    def analyze_crisis_correlations(self, historical_data):
        """
        Step 2: Correlate historical crypto prices with our crisis events.
        
        Purpose: Quantify how crypto prices moved during each documented crisis.
        This provides the core evidence for our research questions.
        """
        if not historical_data:
            print("❌ No historical data available for crisis analysis")
            return None
            
        print("\n🔍 STEP 2: Crisis Correlation Analysis")
        print("Purpose: Quantify crypto price movements during documented crises")
        
        crisis_analysis = []
        
        for crisis in self.crisis_events:
            print(f"\n📊 Analyzing: {crisis['event']} ({crisis['country']}, {crisis['date']})")
            
            try:
                crisis_date = pd.to_datetime(crisis['date'])
                
                # Analyze Bitcoin correlation (most complete historical data)
                if 'BTC-USD' in historical_data:
                    btc_data = historical_data['BTC-USD']['data']
                    
                    # Get 30 days before and after crisis
                    start_window = crisis_date - timedelta(days=30)
                    end_window = crisis_date + timedelta(days=30)
                    
                    # Filter data to crisis window
                    window_data = btc_data[
                        (btc_data.index >= start_window) & 
                        (btc_data.index <= end_window)
                    ]
                    
                    if len(window_data) > 10:  # Ensure sufficient data
                        # Calculate pre/post crisis averages
                        pre_crisis = window_data[window_data.index < crisis_date]
                        post_crisis = window_data[window_data.index >= crisis_date]
                        
                        if len(pre_crisis) > 0 and len(post_crisis) > 0:
                            pre_avg = pre_crisis['Close'].mean()
                            post_avg = post_crisis['Close'].mean()
                            change_pct = ((post_avg - pre_avg) / pre_avg) * 100
                            
                            # Calculate volatility (standard deviation)
                            pre_vol = pre_crisis['Close'].std()
                            post_vol = post_crisis['Close'].std()
                            vol_change = ((post_vol - pre_vol) / pre_vol) * 100 if pre_vol > 0 else 0
                            
                            crisis_result = {
                                'country': crisis['country'],
                                'date': crisis['date'],
                                'event': crisis['event'],
                                'severity': crisis['severity'],
                                'pre_crisis_price': pre_avg,
                                'post_crisis_price': post_avg,
                                'price_change_pct': change_pct,
                                'pre_volatility': pre_vol,
                                'post_volatility': post_vol,
                                'volatility_change_pct': vol_change,
                                'data_points': len(window_data)
                            }
                            
                            crisis_analysis.append(crisis_result)
                            
                            print(f"   ✅ Price change: {change_pct:+.2f}%")
                            print(f"   📊 Volatility change: {vol_change:+.2f}%")
                            print(f"   📈 Data points: {len(window_data)}")
                        else:
                            print(f"   ⚠️  Insufficient data around crisis date")
                    else:
                        print(f"   ❌ No data available for crisis period")
                        
            except Exception as e:
                print(f"   ❌ Error analyzing crisis: {e}")
        
        if crisis_analysis:
            # Save crisis correlation analysis
            df = pd.DataFrame(crisis_analysis)
            filepath = os.path.join(self.data_dir, 'analysis', 'crisis_correlations', 
                                   f'bitcoin_crisis_correlation_{self.today}.csv')
            df.to_csv(filepath, index=False)
            
            print(f"\n✅ Crisis correlation analysis complete")
            print(f"📊 Analyzed {len(crisis_analysis)} crisis events")
            print(f"💾 Results saved to: {filepath}")
            
            # Show summary statistics
            print(f"\n📈 CRISIS IMPACT SUMMARY:")
            avg_price_change = df['price_change_pct'].mean()
            avg_vol_change = df['volatility_change_pct'].mean()
            print(f"   Average price change: {avg_price_change:+.2f}%")
            print(f"   Average volatility change: {avg_vol_change:+.2f}%")
            
            # Identify strongest correlations
            strongest_impact = df.loc[df['price_change_pct'].abs().idxmax()]
            print(f"\n🔥 Strongest crisis impact:")
            print(f"   {strongest_impact['event']} ({strongest_impact['country']})")
            print(f"   Price change: {strongest_impact['price_change_pct']:+.2f}%")
            
            return crisis_analysis
        
        return None
    
    def collect_current_validation_data(self):
        """
        Step 3: Collect current P2P data to validate historical findings.
        
        Purpose: Use our proven Binance P2P scraper to collect current premium
        data that validates the historical crisis correlation patterns.
        """
        print("\n🔍 STEP 3: Current Data Validation")
        print("Purpose: Validate historical findings with current P2P premium data")
        
        try:
            # Import our proven Binance scraper
            from scrapers.binance_p2p import BinanceP2PScraper
            from utils.exchange_rates import ExchangeRateManager
            
            scraper = BinanceP2PScraper()
            rate_manager = ExchangeRateManager()
            
            # Target countries with known crisis patterns
            target_countries = ['SD', 'VE', 'AR', 'AF']  # Start with proven working countries
            
            validation_results = []
            
            # Get current exchange rates
            print("📊 Fetching current exchange rates...")
            current_rates = rate_manager.get_current_rates()
            
            for country in target_countries:
                print(f"\n💱 Collecting {country} P2P data...")
                
                try:
                    # Get country info for currency mapping
                    from utils.country_profiles import get_country_info
                    country_info = get_country_info(country)
                    
                    if country_info and 'fiat_currency' in country_info:
                        fiat = country_info['fiat_currency']
                        
                        # Collect USDT sell orders (people selling crypto for fiat)
                        sell_ads = scraper.get_ads(asset='USDT', fiat=fiat, trade_type='SELL')
                        
                        if sell_ads:
                            # Calculate current premium
                            avg_price = sum(float(ad.get('price', 0)) for ad in sell_ads) / len(sell_ads)
                            official_rate = current_rates.get(fiat, 1.0)
                            
                            # Premium calculation (how much above official rate)
                            expected_price = 1.0 * official_rate  # USDT should be ~$1
                            premium_pct = ((avg_price - expected_price) / expected_price) * 100
                            
                            result = {
                                'country': country,
                                'fiat_currency': fiat,
                                'avg_p2p_price': avg_price,
                                'official_rate': official_rate,
                                'premium_pct': premium_pct,
                                'ad_count': len(sell_ads),
                                'collection_date': self.today
                            }
                            
                            validation_results.append(result)
                            
                            print(f"   ✅ {country}: {premium_pct:+.1f}% premium ({len(sell_ads)} ads)")
                        else:
                            print(f"   ⚠️  {country}: No ads available")
                    else:
                        print(f"   ❌ {country}: Currency info not available")
                        
                except Exception as e:
                    print(f"   ❌ Error collecting {country}: {e}")
            
            if validation_results:
                # Save validation data
                df = pd.DataFrame(validation_results)
                filepath = os.path.join(self.data_dir, 'raw', f'p2p_validation_{self.today}.csv')
                df.to_csv(filepath, index=False)
                
                print(f"\n✅ Current validation data collection complete")
                print(f"📊 Collected data from {len(validation_results)} countries")
                print(f"💾 Results saved to: {filepath}")
                
                return validation_results
            
        except Exception as e:
            print(f"❌ Error in validation data collection: {e}")
            
        return None
    
    def generate_research_summary(self, historical_data, crisis_analysis, validation_data):
        """
        Step 4: Generate comprehensive research summary.
        
        Purpose: Create actionable research insights from our systematic data collection.
        """
        print("\n🔍 STEP 4: Research Summary Generation")
        print("Purpose: Generate actionable insights from systematic data collection")
        
        summary = {
            'collection_date': self.today,
            'historical_data_sources': len(historical_data) if historical_data else 0,
            'crisis_events_analyzed': len(crisis_analysis) if crisis_analysis else 0,
            'current_countries_validated': len(validation_data) if validation_data else 0,
        }
        
        print(f"\n📊 RESEARCH CAPABILITY SUMMARY:")
        print(f"   Historical crypto data: {summary['historical_data_sources']} sources")
        print(f"   Crisis events analyzed: {summary['crisis_events_analyzed']} events")
        print(f"   Current validation data: {summary['current_countries_validated']} countries")
        
        if crisis_analysis:
            # Calculate key research metrics
            df = pd.DataFrame(crisis_analysis)
            
            # High-impact crises (>5% price change)
            high_impact = df[df['price_change_pct'].abs() > 5]
            summary['high_impact_crises'] = len(high_impact)
            
            print(f"   High-impact crises (>5% price change): {len(high_impact)}")
            
            if len(high_impact) > 0:
                print(f"\n🔥 SIGNIFICANT CRISIS CORRELATIONS:")
                for _, crisis in high_impact.iterrows():
                    print(f"   {crisis['event']} ({crisis['country']}): {crisis['price_change_pct']:+.1f}%")
        
        if validation_data:
            # Current crisis indicators
            df_val = pd.DataFrame(validation_data)
            high_premium = df_val[df_val['premium_pct'] > 10]  # >10% premium indicates stress
            
            summary['current_crisis_indicators'] = len(high_premium)
            print(f"   Current crisis indicators (>10% premium): {len(high_premium)}")
            
            if len(high_premium) > 0:
                print(f"\n⚠️  CURRENT CRISIS SIGNALS:")
                for _, country in high_premium.iterrows():
                    print(f"   {country['country']}: {country['premium_pct']:+.1f}% premium")
        
        # Save research summary
        summary_path = os.path.join(self.data_dir, 'analysis', f'research_summary_{self.today}.json')
        import json
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n✅ Research summary complete")
        print(f"💾 Summary saved to: {summary_path}")
        
        print(f"\n🎯 NEXT STEPS:")
        print(f"   1. Review crisis correlation results in data/analysis/crisis_correlations/")
        print(f"   2. Analyze current validation data in data/raw/")
        print(f"   3. Prepare academic publication using systematic findings")
        print(f"   4. Implement daily monitoring for ongoing research")
        
        return summary

def main():
    """
    Execute Phase 3 methodical data collection with clear objectives.
    """
    print("🚀 PHASE 3: METHODICAL DATA COLLECTION")
    print("="*60)
    print("Research Objective: Quantify cryptocurrency crisis correlation")
    print("Method: Systematic historical and current data analysis")
    print("Expected Outcome: Academic-quality crisis impact evidence")
    print("="*60)
    
    # Initialize coordinator
    coordinator = Phase3DataCoordinator()
    
    # Step 1: Historical baseline
    historical_data = coordinator.collect_historical_baseline()
    
    # Step 2: Crisis correlation analysis
    crisis_analysis = coordinator.analyze_crisis_correlations(historical_data)
    
    # Step 3: Current validation data
    validation_data = coordinator.collect_current_validation_data()
    
    # Step 4: Research summary
    summary = coordinator.generate_research_summary(historical_data, crisis_analysis, validation_data)
    
    print(f"\n🎉 PHASE 3 COLLECTION COMPLETE!")
    print(f"📊 Systematic data collection with clear research objectives achieved")
    print(f"🎯 Ready for academic analysis and publication preparation")

if __name__ == "__main__":
    main()
