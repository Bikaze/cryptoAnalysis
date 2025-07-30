"""
Premium Calculator for Current Data
===================================

Calculate cryptocurrency premiums vs official exchange rates
to demonstrate the immediate impact we can measure.

Author: Clement MUGISHA
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.csv_data_manager import CSVDataManager
from utils.exchange_rates import ExchangeRateCollector
import pandas as pd


def calculate_premiums():
    """Calculate premiums for all collected data."""

    print("💰 CRYPTOCURRENCY PREMIUM ANALYSIS")
    print("=" * 50)

    csv_manager = CSVDataManager()
    rate_collector = ExchangeRateCollector()

    # Load all P2P data
    all_data = csv_manager.load_raw_ads()

    if all_data.empty:
        print("❌ No P2P data found")
        return

    # Load current exchange rates
    rates_data = pd.read_csv("data/exchange_rates/rates_2025-07-30.csv")
    rates_dict = dict(zip(rates_data["fiat_currency"], rates_data["usd_rate"]))

    print(f"📊 Analyzing {len(all_data)} P2P advertisements")
    print(f"💱 Official rates available for: {list(rates_dict.keys())}")

    # Calculate premiums by country
    results = []

    for country_code in all_data["country_code"].unique():
        country_data = all_data[all_data["country_code"] == country_code]
        fiat = country_data["fiat"].iloc[0]

        if fiat not in rates_dict:
            print(f"⚠️  No exchange rate for {country_code} ({fiat})")
            continue

        official_rate = rates_dict[fiat]

        # Calculate average prices
        avg_price = country_data["price"].mean()
        median_price = country_data["price"].median()

        # Calculate premiums (assuming USDT = $1)
        premium_avg = rate_collector.calculate_premium(avg_price, official_rate, 1.0)
        premium_median = rate_collector.calculate_premium(
            median_price, official_rate, 1.0
        )

        # Market structure
        total_ads = len(country_data)
        buy_ads = len(country_data[country_data["trade_type"] == "BUY"])
        sell_ads = len(country_data[country_data["trade_type"] == "SELL"])

        result = {
            "country_code": country_code,
            "fiat": fiat,
            "total_ads": total_ads,
            "buy_ads": buy_ads,
            "sell_ads": sell_ads,
            "avg_price": avg_price,
            "median_price": median_price,
            "official_rate": official_rate,
            "premium_avg": premium_avg,
            "premium_median": premium_median,
        }
        results.append(result)

        print(f"\n🌍 {country_code} ({fiat}):")
        print(f"  📊 Market: {total_ads} ads ({buy_ads} buy, {sell_ads} sell)")
        print(f"  💰 Avg Price: {avg_price:,.2f} {fiat}")
        print(f"  💱 Official Rate: {official_rate:,.2f} {fiat}/USD")
        print(
            f"  🔥 Premium: {premium_avg:+.1f}% (avg), {premium_median:+.1f}% (median)"
        )

        # Market interpretation
        if sell_ads > buy_ads * 3:
            print(f"  📈 Market: Heavy sell pressure (people exiting {fiat})")
        elif buy_ads > sell_ads * 3:
            print(f"  📉 Market: Heavy buy pressure (people acquiring {fiat})")
        else:
            print(f"  ⚖️  Market: Balanced trading")

    # Summary
    print(f"\n🎯 IMPACT SUMMARY")
    print("=" * 30)

    if results:
        avg_premium = sum(r["premium_avg"] for r in results) / len(results)
        max_premium_country = max(results, key=lambda x: x["premium_avg"])
        min_premium_country = min(results, key=lambda x: x["premium_avg"])

        print(f"📊 Average premium across all countries: {avg_premium:+.1f}%")
        print(
            f"🔥 Highest premium: {max_premium_country['country_code']} ({max_premium_country['premium_avg']:+.1f}%)"
        )
        print(
            f"🔥 Lowest premium: {min_premium_country['country_code']} ({min_premium_country['premium_avg']:+.1f}%)"
        )

        total_ads = sum(r["total_ads"] for r in results)
        print(f"📈 Total market activity: {total_ads} advertisements")
        print(f"🌍 Countries with active P2P markets: {len(results)}/6")


if __name__ == "__main__":
    calculate_premiums()
