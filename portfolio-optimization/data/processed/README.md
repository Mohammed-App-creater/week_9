# Processed Data Directory

This directory stores cleaned and feature-engineered datasets exported from notebooks.

## Expected Files

- `cleaned_price_data.csv` – Clean adjusted close prices (Task 1)
- `daily_returns.csv` – Calculated daily returns (Task 1)
- `rolling_volatility.csv` – 20-day rolling volatility (Task 1)
- `arima_forecasts.csv` – ARIMA model predictions (Task 2)
- `garch_volatility_forecasts.csv` – GARCH volatility predictions (Task 2)
- `optimal_portfolio_weights.csv` – Optimized allocations (Task 3)
- `backtest_results.csv` – Historical performance (Task 4)

## Usage

Notebooks should export processed DataFrames to this directory for:
1. **Reproducibility** – Avoid re-running expensive computations
2. **Modularity** – Separate data processing from modeling
3. **Collaboration** – Share intermediate results

## Format Guidelines

- Use CSV format for compatibility
- Include proper headers
- Use ISO date format (YYYY-MM-DD) for time series
- Document any transformations in notebook markdown

---

*Note: Raw data files are automatically downloaded from yfinance and not stored in Git.*
