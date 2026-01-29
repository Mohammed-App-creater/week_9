# Notebooks Directory

This directory contains all Jupyter notebooks for the portfolio optimization project, organized sequentially by task.

## Naming Convention

Notebooks follow the format: `XX_descriptive_name.ipynb` where:
- `XX` = two-digit number (01, 02, 03, etc.) indicating execution order
- `descriptive_name` = brief description of the notebook's purpose

## Notebook Descriptions

### 01_data_preprocessing_and_eda.ipynb
**Task 1: Data Preprocessing and Exploratory Analysis**
- Fetch historical price data for TSLA, BND, SPY (2015-2026)
- Data cleaning and validation
- Feature engineering (daily returns, rolling volatility)
- Exploratory data analysis with professional visualizations
- Stationarity analysis (ADF tests)
- Risk metrics calculation (VaR, Sharpe Ratio)

### 02_arima_sarima_modeling.ipynb
**Task 2: Time Series Forecasting (Traditional)**
- ARIMA/SARIMA modeling for price forecasting
- Stationarity checks and differencing
- Parameter optimization (Grid Search/AutoARIMA)
- Model evaluation (MAE, RMSE, MAPE)

### 03_lstm_modeling.ipynb
**Task 3: Deep Learning Forecasting**
- Data normalization and sequence creation
- LSTM Neural Network architecture
- Model training with Early Stopping
- Forecasting and inverse transformation
- Comparison with classical models

### 04_forecast_future_trends.ipynb
**Task 4: Future Forecasts & Trend Analysis**
- Future price forecasting (6-12 months horizon)
- Trend analysis using best-performing model (LSTM)
- Visualization of historical data vs. forecasts
- Market opportunities and risk assessment

---

## How to Run

1. Ensure you're in the virtual environment:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Start Jupyter:
   ```bash
   jupyter notebook
   ```

3. Execute notebooks in sequential order (01 → 02 → 03 → 04 → 05)

---

## Best Practices

- **Always run notebooks in order** – later notebooks may depend on earlier outputs
- **Restart kernel before final run** – ensures reproducibility
- **Save outputs** – processed data should be exported to `../data/processed/`
- **Document changes** – add markdown cells explaining modifications
- **Keep code clean** – follow PEP8 and modular design principles
