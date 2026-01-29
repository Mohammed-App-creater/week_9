# Quick Start Guide

Welcome to the Portfolio Optimization project! This guide will get you up and running in 5 minutes.

## ⚡ Quick Setup (3 steps)

### 1. Run the setup script:
```bash
python setup.py
```

This will:
- Check your Python version
- Create a virtual environment
- Install all dependencies

### 2. Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Launch Jupyter:
```bash
jupyter notebook
```

## 📊 Running Task 1

1. In Jupyter, navigate to: `notebooks/01_data_preprocessing_and_eda.ipynb`
2. Click **"Restart & Run All"** from the menu
3. Wait ~30-60 seconds for data download and processing
4. Review the outputs and visualizations

## 📁 Project Structure at a Glance

```
portfolio-optimization/
├── notebooks/          ← Jupyter notebooks (start here!)
│   └── 01_data_preprocessing_and_eda.ipynb
├── data/
│   └── processed/      ← Output CSVs (created by notebooks)
├── src/                ← Python modules (future)
├── tests/              ← Unit tests
├── requirements.txt    ← Dependencies
└── README.md           ← Full documentation
```

## 🔧 Dependencies

All dependencies are in `requirements.txt`:
- Data: `pandas`, `numpy`, `yfinance`
- Modeling: `statsmodels`, `pmdarima`, `tensorflow`, `sklearn`
- Optimization: `pyportfolioopt`, `scipy`
- Visualization: `matplotlib`, `seaborn`
- Development: `jupyter`, `notebook`

## 🚀 Common Commands

```bash
# Install new package
pip install <package-name>

# Update requirements.txt
pip freeze > requirements.txt

# Run tests
pytest tests/ -v

# Deactivate virtual environment
deactivate
```

## 📚 Task Roadmap

- [x] **Task 1:** Data Preprocessing & EDA ✅
- [ ] **Task 2:** Time Series Forecasting (ARIMA, GARCH, LSTM)
- [ ] **Task 3:** Portfolio Optimization
- [ ] **Task 4:** Backtesting
- [ ] **Task 5:** Final Reporting

## 🆘 Troubleshooting

### Issue: "Module not found"
**Solution:** Ensure virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Issue: "Jupyter not found"
**Solution:** Install Jupyter in the virtual environment:
```bash
pip install jupyter notebook
```

### Issue: yfinance download fails
**Solution:** Check internet connection and try again. Yahoo Finance API is sometimes rate-limited.

## 📖 Full Documentation

See [README.md](README.md) for comprehensive project documentation.

---

**Need help?** Open an issue or refer to the main README.
