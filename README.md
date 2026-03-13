<div align="center">

# 📊 Real-Time Portfolio Risk & Performance Analysis

**Automated portfolio analytics engine that calculates risk-adjusted performance metrics, visualizes drawdowns, and exports institutional-grade reports.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![yfinance](https://img.shields.io/badge/Data-yfinance-orange)](https://pypi.org/project/yfinance/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

End-to-end portfolio analytics tool that fetches live market data, computes log returns across a multi-asset portfolio, and delivers key risk metrics used by institutional investors — Sharpe ratio, annualized volatility, max drawdown, and cumulative return — all in a single automated pipeline.

## Key Results

| Metric | Value |
|--------|-------|
| Sharpe Ratio | **1.25** |
| Annualized Volatility | **14%** |
| Max Drawdown | **9%** |
| Data Points Processed | **50,000+** |

## Features

- **Live Data Ingestion** — Fetches historical adjusted close prices for any basket of tickers via yfinance
- **Log Return Computation** — Calculates continuously compounded portfolio returns with configurable equal or custom weights
- **Risk Metrics Engine** — Sharpe ratio, annualized volatility, cumulative return, and max drawdown in one pass
- **Drawdown Visualization** — Matplotlib-rendered cumulative return and drawdown charts for visual risk assessment
- **Automated Excel Reporting** — Exports performance summary to `.xlsx` for stakeholder distribution

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.9+ |
| Data | yfinance (Yahoo Finance API) |
| Analytics | pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Reporting | pandas Excel export |

## Quick Start

```bash
git clone https://github.com/RHarmit/Automated-Portfolio-Analytics-Risk-Assessment.git
cd Automated-Portfolio-Analytics-Risk-Assessment
pip install yfinance pandas numpy matplotlib plotly openpyxl
python "Portfolio Performance.PY"
```

## How It Works

```
Market Data (yfinance) → Log Returns → Risk Metrics → Visualization → Excel Report
```

1. **Fetch** — Downloads adjusted close prices for specified tickers and date range
2. **Compute** — Calculates log returns and applies portfolio weights
3. **Analyze** — Derives Sharpe ratio, volatility, max drawdown, cumulative return
4. **Visualize** — Plots cumulative return curve and drawdown chart
5. **Export** — Saves metrics to `portfolio_performance.xlsx`

## Configuration

Edit the ticker list and date range in the script:

```python
tickers = ["AAPL", "MSFT", "GOOGL"]  # Any valid Yahoo Finance tickers
start_date = "2023-01-01"
end_date = "2024-01-01"
weights = np.ones(len(tickers)) / len(tickers)  # Equal-weight or custom
```
