![OPIM 3510 — Business Data Analytics I · Dr. Dave Wanik](opim3510_banner.svg)

# OPIM 3510 — Business Data Analytics I · Notebooks

> 📦 **Archive: the Spring 2024 version of the course.** The rebuilt course (Spring 2027) lives at **[drdave-teaching/OPIM3510-BDA1](https://github.com/drdave-teaching/OPIM3510-BDA1)**. This repo stays up because Module 3 is still linked from there until it is rebuilt.

Student-facing Google Colab notebooks for **OPIM 3510 (BDA1)**, the hands-on
companions to the [course companion book](https://drdave-teaching.github.io/opim3510-textbook/).

| Folder | Topic | Book chapter |
|---|---|---|
| `Module1_EDA/` | Python basics, tables & wrangling, EDA/charts, queries & joins | Ch 1, 3 |
| `Module2_TimeSeriesForecasting/` | Time-series data, moving averages & momentum trading, exponential smoothing | Ch 5–6 |
| `Module3_Stats_Geospatial/` | Distributions & for loops, sampling/CLT/CIs, geospatial & maps | Ch 1–2, 4 |
| `Assignments/` | Individual assignment templates + course projects | — |
| `data/` | Course datasets, read straight from GitHub by the notebooks (no Drive or downloads needed) | — |

### Module 2 starts here
Module 2 is built around one forecasting problem: **Connecticut's daily electricity demand**.
Start with `Module2_TimeSeriesForecasting/1_TimeSeriesData/1_CT_Electricity_Demand.ipynb` (Week 6: the data),
then `Module2_TimeSeriesForecasting/2_MovingAverageModel/1_CT_Baselines_and_Moving_Averages.ipynb` (Week 7: baselines, moving averages, leakage, train/test by time).
Every Module 2 notebook scores forecasts with the same `evaluate()` scorecard
(`Module2_TimeSeriesForecasting/forecast_helpers.py`), using **error = predicted − actual**.

### Data
| File | What it is |
|---|---|
| `ct_demand_weather_hourly_2011_2021.csv` | Hourly CT electricity demand (MWh) + Bradley Airport weather, 2011–2021 (raw, with its real-world problems left in) |
| `ct_daily_demand_2011_2021.csv` | The cleaned daily version built in the Week 6 notebook (GWh/day, avg + max temperature) |
| `ct_heating_oil_weekly_2019_2023.csv` | Weekly CT retail heating oil prices, Oct 2019 – Oct 2023 |
| `GLD.csv` | Daily prices for the GLD gold ETF, Nov 2004 – Oct 23, 2026 (saved from Yahoo Finance) |
| `AAPL.csv` | Daily AAPL stock prices, 1980–2020 |
| `BDL_Jan2019.csv` | Raw 5-minute Bradley Airport weather observations, January 2019 |

— Dr. Dave Wanik · University of Connecticut
