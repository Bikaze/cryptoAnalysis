# 🌎 Target Countries and Profiles: Milestone Documentation

## 📊 Objective

To define the rationale behind selecting specific countries for P2P crypto data collection and create a structured, programmatically usable profile for each region. These profiles will be used across scraping, exchange rate fetching, analytics, and reporting scripts.

---

## ✉️ Selection Criteria

Countries are chosen based on one or more of the following:

* 💸 Severe currency instability or hyperinflation
* 🌏 Lack of access to international financial systems (sanctions, blacklisting)
* ❌ Collapsed or dysfunctional local banking systems
* 🧵 Evidence or reports of informal P2P crypto usage
* 🔄 Capital controls or high remittance dependency

---

## 🌐 Countries & Rationales

### 🇸🇩 Sudan (SD)

* **Reason**: War, international sanctions, inaccessible global banking
* **Traits**: MTN and Zain mobile money dominate
* **Crypto use**: Informal trading and P2P remittances

### 🇦🇫 Afghanistan (AF)

* **Reason**: Taliban regime, frozen assets, banned banking systems
* **Traits**: Few traditional payment methods; often rely on cash in Kabul
* **Crypto use**: Critical for aid and USD access

### 🇻🇪 Venezuela (VE)

* **Reason**: Hyperinflation, Bolivar collapse, huge demand for USD
* **Traits**: Pago Móvil and domestic banks dominate P2P methods
* **Crypto use**: Extremely high

### 🇳🇬 Nigeria (NG)

* **Reason**: Crypto bans, unstable Naira, remittance demand
* **Traits**: Bank transfers and mobile payments like Opay
* **Crypto use**: Highest in Africa

### 🇵🇼 Zimbabwe (ZW)

* **Reason**: Recurring inflation crises, USD black market
* **Traits**: Local Ecocash mobile wallet and cash usage
* **Crypto use**: Growing

### 🇦🇷 Argentina (AR)

* **Reason**: Capital controls, peso instability, crypto savings
* **Traits**: Bank transfers, Mercado Pago
* **Crypto use**: Increasing institutional and informal usage

---

## 🔄 Standardized Profile Structure

Each country will have a structured profile stored in a reusable format, as defined in [`config/countries.yml`](config/countries.yml):

```yaml
- country_code: "SD"
  name: "Sudan"
  fiat: "SDG"
  stablecoins: ["USDT"]
  expected_payment_methods: ["MTN", "Zain"]
  exchange_rate_sources: ["https://xe.com"]
  p2p_platforms: ["binance", "okx", "paxful"]
  start_date: "2019-01-01"
```

---

## 📦 Data Profile Usage

These profiles will be used by:

* ✅ Scrapers to determine country codes, fiat filters, and payment methods
* ✅ Exchange rate comparators to locate sources for official rates
* ✅ Analytics pipelines to infer location and group by geography
* ✅ Dashboards and reports for narrative context and filtering

---

## 🔧 Format Options Comparison

| Format          | Pros                     | Cons                     | Use Case                   |
| --------------- | ------------------------ | ------------------------ | -------------------------- |
| **YAML**        | Human-readable, flexible | Needs parser (PyYAML)    | Configs, editable metadata |
| **JSON**        | Fast, portable           | Harder to read/edit      | APIs, JS integrations      |
| **Python dict** | Native for scripts       | Less reusable externally | Fast prototyping           |
| **SQLite**      | Queryable, efficient     | Setup overhead           | Dashboards, analytics      |
| **MongoDB**     | Schema-flexible          | Complex infra            | Scalable queries, web apps |

---

## ✅ Next Steps

1. Implement [`config/countries.yml`](config/countries.yml) with all 6 profiles.
2. Build the Python loader utility, [`utils/country_profiles.py`](utils/country_profiles.py), to import profiles by country code.
3. Use the profile in the Binance scraper for dynamic parameter injection.

---

This milestone provides the essential geographic and economic context needed to power accurate, scalable, and ethically sound crypto research scraping infrastructure.
