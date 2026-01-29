# Portfolio Optimization for GMF Investments

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive quantitative financial analysis project implementing time series forecasting and portfolio optimization for GMF Investments.

---

## 📊 Business Context

**Client:** GMF Investments  
**Objective:** Optimize portfolio allocation across three distinct asset classes to maximize risk-adjusted returns

**Assets Under Analysis:**
- **TSLA (Tesla Inc.)** – High risk, high return equity
- **BND (Vanguard Total Bond Market ETF)** – Low risk fixed income
- **SPY (S&P 500 ETF)** – Moderate risk broad market equity

**Analysis Period:** January 1, 2015 to January 15, 2026 (11+ years)

---

## 🎯 Project Tasks

### Task 1: Data Preprocessing and Exploratory Analysis ✅
- Historical data extraction via `yfinance`
- Data cleaning and validation
- Feature engineering (returns, volatility)
- Comprehensive EDA with visualizations
- Stationarity analysis (ADF tests)
- Risk metrics (VaR, Sharpe Ratio)

**Deliverable:** `notebooks/01_data_preprocessing_and_eda.ipynb`

### Task 2: Time Series Forecasting 🔄
- ARIMA modeling for return forecasting
- GARCH modeling for volatility forecasting
- LSTM deep learning approach
- Model evaluation and comparison

**Deliverable:** `notebooks/02_time_series_forecasting.ipynb`

### Task 3: Portfolio Optimization 🔄
- Modern Portfolio Theory (Markowitz)
- Efficient frontier construction
- Optimal weight allocation
- Risk-return tradeoff analysis

**Deliverable:** `notebooks/03_portfolio_optimization.ipynb`

### Task 4: Backtesting and Validation 🔄
- Historical performance simulation
- Benchmark comparison
- Performance metrics calculation
- Strategy evaluation

**Deliverable:** `notebooks/04_backtesting.ipynb`

### Task 5: Final Reporting 🔄
- Executive dashboard
- Comprehensive results summary
- Investment recommendations
- Presentation-ready visualizations

**Deliverable:** `notebooks/05_final_reporting.ipynb`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git (for version control)
- 2GB+ free disk space (for data and models)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohammed-App-creater/portfolio-optimization.git
   cd portfolio-optimization
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

6. **Navigate to `notebooks/` and start with `01_data_preprocessing_and_eda.ipynb`**

---

## 📁 Repository Structure

```
portfolio-optimization/
├── .github/
│   └── workflows/
│       └── unittests.yml          # CI/CD pipeline for automated testing
├── .vscode/
│   └── settings.json              # VS Code configuration
├── data/
│   └── processed/                 # Cleaned, feature-engineered datasets
├── notebooks/
│   ├── 01_data_preprocessing_and_eda.ipynb    # Task 1 ✅
│   ├── 02_time_series_forecasting.ipynb       # Task 2 (planned)
│   ├── 03_portfolio_optimization.ipynb        # Task 3 (planned)
│   ├── 04_backtesting.ipynb                   # Task 4 (planned)
│   ├── 05_final_reporting.ipynb               # Task 5 (planned)
│   ├── __init__.py
│   └── README.md                  # Notebook documentation
├── src/
│   └── __init__.py                # Source code modules (future use)
├── scripts/
│   └── __init__.py                # Utility scripts (future use)
├── tests/
│   └── __init__.py                # Unit tests
├── .gitignore
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🛠️ Tech Stack

**Data Manipulation & Analysis:**
- `pandas` – Data wrangling
- `numpy` – Numerical computing

**Data Acquisition:**
- `yfinance` – Historical financial data

**Time Series Modeling:**
- `statsmodels` – ARIMA, statistical tests
- `pmdarima` – Auto-ARIMA
- `tensorflow` – LSTM deep learning

**Portfolio Optimization:**
- `pyportfolioopt` – Modern Portfolio Theory
- `scipy` – Optimization algorithms
- `scikit-learn` – Machine learning utilities

**Visualization:**
- `matplotlib` – Core plotting
- `seaborn` – Statistical visualizations

**Development:**
- `jupyter` – Interactive notebooks
- `pytest` – Unit testing (CI/CD)

---

## 📈 Key Features

✅ **Automated Data Pipeline** – Fetch and clean financial data with one command  
✅ **Stationarity Testing** – ADF tests for ARIMA readiness  
✅ **Rolling Volatility** – Time-varying risk measurement  
✅ **Value at Risk (VaR)** – Downside risk quantification  
✅ **Sharpe Ratio** – Risk-adjusted performance metrics  
✅ **Professional Visualizations** – Publication-ready plots  
✅ **Reproducible Research** – Fully documented Jupyter notebooks  
✅ **CI/CD Integration** – Automated testing with GitHub Actions  

---

## 📊 Preliminary Insights (Task 1)

**Asset Characteristics:**

| Asset | Annual Return | Annual Volatility | Sharpe Ratio | Risk Profile |
|-------|---------------|-------------------|--------------|--------------|
| TSLA  | High          | Very High (>80%)  | Variable     | Aggressive   |
| BND   | Low           | Very Low (<10%)   | Modest       | Conservative |
| SPY   | Moderate      | Moderate (20-40%) | Solid        | Balanced     |

**Stationarity:**
- ❌ Price series: Non-stationary (requires differencing)
- ✅ Return series: Stationary (ready for ARIMA)

**COVID-19 Impact:** All assets experienced heightened volatility (Feb-Apr 2020), with varying recovery trajectories.

---

## 🧪 Testing

Run unit tests using pytest:
```bash
pytest tests/ -v
```

Run tests with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

---

## 📝 Development Notes

**Code Style:**
- Follow PEP8 guidelines
- Use `black` for automatic formatting (88 character line length)
- Type hints recommended for functions

**Branching Strategy:**
- `main` – Production-ready code
- `develop` – Integration branch
- `feature/*` – Individual feature development

**Commit Messages:**
- Use conventional commits format (e.g., `feat:`, `fix:`, `docs:`)

---

## 🤝 Contributing

This is an academic project for GMF Investments. For questions or suggestions:

1. Open an issue describing the problem
2. Fork the repository
3. Create a feature branch (`git checkout -b feature/AmazingFeature`)
4. Commit your changes (`git commit -m 'feat: Add AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**Senior Quantitative Financial Analyst**  
10 Academy – Week 9 Portfolio Optimization Project

---

## 🙏 Acknowledgments

- **Data Source:** Yahoo Finance (via `yfinance`)
- **Inspiration:** Modern Portfolio Theory (Harry Markowitz, 1952)
- **Frameworks:** `pyportfolioopt` by Robert Andrew Martin
- **Educational Support:** 10 Academy Data Science Program

---

## 📚 References

1. Markowitz, H. (1952). "Portfolio Selection." *Journal of Finance*, 7(1), 77-91.
2. Black, F., & Litterman, R. (1992). "Global Portfolio Optimization." *Financial Analysts Journal*, 48(5), 28-43.
3. Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day.
4. Engle, R. F. (1982). "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation." *Econometrica*, 50(4), 987-1007.

---

**Project Status:** In Progress (Task 1 Complete ✅)  
**Last Updated:** January 28, 2026
