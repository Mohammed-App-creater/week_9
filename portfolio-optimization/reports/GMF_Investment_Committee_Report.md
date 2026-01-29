# GMF Investments — Portfolio Optimization & Strategy Report

**Prepared for:** Investment Committee  
**Project:** Portfolio Management Optimization (TSLA, BND, SPY)  
**Date:** January 2026  

---

## Execution Validation (Step 1)

- **Notebooks reviewed:** Task 1 (`task1_data_preprocessing_eda.ipynb`), Tasks 2–6 (`02_arima_sarima_modeling.ipynb` through `06_strategy_backtesting.ipynb`). Note: Task 1 uses the filename `task1_data_preprocessing_eda.ipynb`; the pipeline is equivalent to 01→06.
- **Execution status:** Tasks 2–6 contained executed outputs (plots, tables, metrics). Task 1 had no outputs initially; it was executed after a minimal code fix to handle yfinance’s MultiIndex column structure (Adj Close/Close extraction). All six notebooks have been executed end-to-end; plots and tables render.
- **Code change:** In Task 1, a single cell was updated to extract adjusted close (or close) prices when columns are a MultiIndex; no other refactoring was performed.

---

## 1. Executive Summary

This report synthesizes findings from a six-task quantitative pipeline: data preparation and exploratory analysis, ARIMA and LSTM modeling for Tesla (TSLA), multi-step forecasting, Modern Portfolio Theory (MPT) optimization, and out-of-sample backtesting. The objective was to evaluate whether a forecast-driven allocation could improve risk-adjusted outcomes versus a static 60% SPY / 40% BND benchmark.

**Main results:**

- **Data & risk profile:** TSLA showed the highest return and volatility (47.5% annualized return, 57.7% volatility); BND the lowest (2.0% return, 5.4% volatility); SPY was in between (14.3% return, 17.8% volatility). Diversification potential was confirmed by differing risk profiles and stationarity analysis.
- **Models:** ARIMA(0,1,0) was selected for TSLA prices (MAE $69.37, RMSE $82.80, MAPE 22.50%). The LSTM (two layers, 50 units, 60-day lookback) substantially outperformed on the test set (MAE $11.85, RMSE $15.15, MAPE 3.49%). **LSTM was chosen as the best-performing model** for forecasting and for feeding the optimizer.
- **Forecast & optimization:** The LSTM-based one-year TSLA forecast implied a **downward** trend (e.g. expected annual return about -70% in the optimization run), with uncertainty widening over the horizon. The MPT Max Sharpe portfolio allocated **0% to TSLA**, **55.7% to BND**, and **44.3% to SPY** (risk-free rate 0%), with expected return 7.46% and Sharpe 0.86.
- **Backtesting (Jan 2025 – Jan 2026):** The strategy (55.7% BND / 44.3% SPY, monthly rebalancing) delivered **lower total return** than the benchmark (13.11% vs 15.01%) but **better risk-adjusted performance**: Sharpe 1.33 vs 1.18 and max drawdown -8.22% vs -11.29%. So the strategy **did not outperform on raw return** but **did on risk-adjusted metrics and drawdown**.

**Conclusion for the Committee:** The process shows that incorporating a bearish TSLA forecast led the optimizer to exclude TSLA and tilt toward bonds. In the single out-of-sample year tested, this produced better Sharpe and smaller drawdown at the cost of lower total return. Results are suggestive, not conclusive; limitations (short backtest, no transaction costs, single period) and EMH considerations are noted in the body of the report.

---

## 2. Methodology Overview (Tasks 1–5)

### Task 1 — Data Preprocessing and EDA

- **Scope:** Historical adjusted close (or close) prices for TSLA, BND, and SPY from January 2015 to January 2026. Data was cleaned (forward fill for missing values), and features were engineered: daily returns and 20-day rolling annualized volatility.
- **Analysis:** Exploratory plots (prices, returns, rolling volatility), identification of extreme return days, Augmented Dickey-Fuller (ADF) stationarity tests on prices and returns, and risk metrics: 95% daily VaR and annualized Sharpe ratio (risk-free rate 0%).

### Task 2 — ARIMA/SARIMA Modeling

- **Scope:** TSLA price series. Training through 2024; test on 2025 onward.
- **Steps:** ADF/KPSS on levels and differenced series; first-order differencing (d=1) to achieve stationarity; Auto ARIMA for order selection; fit ARIMA(0,1,0); one-step-ahead forecasts on test; evaluation via MAE, RMSE, MAPE.

### Task 3 — LSTM Modeling

- **Scope:** Same TSLA data and train/test split as Task 2.
- **Steps:** MinMax scaling (fit on train only), 60-day lookback sequences, 2×LSTM(50) + Dropout(0.2) + Dense(1), MSE loss, Adam, EarlyStopping. Evaluation: MAE, RMSE, MAPE; comparison with ARIMA.

### Task 4 — Forecasting (Future Trends)

- **Scope:** TSLA 6–12 month outlook using the Task 3 LSTM.
- **Steps:** Same architecture and lookback; iterative multi-step forecast (e.g. 252 trading days); RMSE-based heuristic uncertainty band (scaling with √time). Trend and opportunity/risk narrative.

### Task 5 — Portfolio Optimization (MPT)

- **Scope:** Three assets — TSLA, BND, SPY.
- **Inputs:** TSLA expected return from LSTM 1-year price forecast; BND and SPY from historical annualized means. Covariance from historical daily returns. PyPortfolioOpt for efficient frontier, Max Sharpe and Min Volatility portfolios (risk-free rate 0%).

### Task 6 — Backtesting

- **Scope:** Out-of-sample period January 2025 – January 2026 (no overlap with model training).
- **Strategy:** Max Sharpe weights from Task 5 (55.7% BND, 44.3% SPY, 0% TSLA) with **monthly rebalancing**.
- **Benchmark:** Static 60% SPY / 40% BND, buy-and-hold.
- **Metrics:** Total return, annualized return, annualized volatility, Sharpe ratio (rf=0), maximum drawdown.

---

## 3. Model Comparison & Selection

| Metric   | ARIMA(0,1,0) | LSTM (2×50, 60-day) |
|----------|----------------|----------------------|
| MAE      | $69.37        | $11.85               |
| RMSE     | $82.80        | $15.15               |
| MAPE     | 22.50%        | 3.49%                |

- **ARIMA:** Best Auto ARIMA order was (0,1,0)—random walk in differences. Simple and interpretable but large errors in dollar and percentage terms on the test set.
- **LSTM:** Same train/test split; 60-day lookback; two LSTM(50) layers + dropout. Much lower MAE, RMSE, and MAPE; captures non-linear structure that ARIMA does not.
- **Selection:** **LSTM was selected as the best-performing model** for TSLA forecasting and for feeding expected returns into the optimizer. ARIMA remains useful as a baseline and for short-term trend context.

---

## 4. Forecast Interpretation

- **Horizon:** 6–12 months (e.g. 252 trading days in the main runs).
- **Direction:** The LSTM-based TSLA forecast used in optimization implied a **downward** trend (e.g. current price ~$431, one-year forecast ~$130, implying roughly -70% annual return). The notebook’s narrative describes the forecast as a baseline trend indicator rather than a precise price target.
- **Uncertainty:** Confidence bands were constructed heuristically from test-set RMSE, scaling with √(time). Uncertainty **widens** over the horizon, consistent with multi-step iterative forecasting. The documentation states that real-world uncertainty is likely higher than these bands (e.g. regime changes, shocks).
- **Opportunities and risks:** Documented risks include model uncertainty (accuracy degrades with horizon), use of predictions as inputs (potential mean reversion in the path), and omission of fundamentals (rates, EV competition, earnings). The forecast is recommended as one input alongside fundamental and macro analysis.

---

## 5. Portfolio Recommendation

- **Expected return assumptions:**  
  - TSLA: from LSTM one-year price forecast (e.g. about -69.91% in the optimization run).  
  - BND and SPY: historical annualized mean returns (e.g. BND ~2.02%, SPY from historical data).
- **Covariance:** Sample covariance of daily returns. TSLA had by far the largest variance; BND the smallest; SPY in between. Correlation structure supported diversification (e.g. BND vs equities).
- **Efficient frontier:** The frontier was generated from these expected returns and covariance. The Max Sharpe (tangency) portfolio lay on this curve; the Min Volatility portfolio was more bond-heavy (e.g. ~94% BND, ~6% SPY).
- **Optimal weights (Max Sharpe, rf=0):**  
  - TSLA **0%**, BND **55.7%**, SPY **44.3%**.  
  Expected return ~7.46%, Sharpe 0.86.
- **Rationale:** The bearish TSLA forecast and high TSLA volatility led the optimizer to assign zero weight to TSLA. The tangency portfolio favored a BND/SPY mix that improved risk-adjusted return relative to the individual assets under the stated assumptions.

**Recommendation:** Use the **Max Sharpe portfolio (55.7% BND, 44.3% SPY, 0% TSLA)** for clients seeking the best risk-adjusted profile under these inputs. Rebalancing (e.g. monthly or quarterly) to these targets is appropriate; expected returns and covariance should be updated periodically (e.g. when new forecasts or data are available).

---

## 5a. Cross-Task Synthesis

- **How forecasting influenced portfolio construction:** The LSTM forecast for TSLA implied a large negative one-year return (e.g. ~-70%). That input drove the MPT optimizer to assign **0% to TSLA** and to favor BND and SPY. Without that bearish TSLA forecast, the optimizer could have allocated nonzero weight to TSLA; the forecast was therefore decisive for the chosen allocation.
- **Higher model complexity and portfolio outcomes:** LSTM (more complex) clearly beat ARIMA (simpler) on MAE, RMSE, and MAPE for TSLA. In the backtest, the resulting portfolio (no TSLA) delivered **better Sharpe and smaller drawdown** than the 60/40 benchmark but **lower total return**. So higher complexity led to a different, more conservative allocation and better risk-adjusted outcomes in this single period, not to higher raw return.
- **Role of diversification:** TSLA (high return, high volatility), BND (low return, low volatility), and SPY (moderate on both) offered clear diversification. The optimal Max Sharpe portfolio used only BND and SPY; excluding TSLA reduced volatility and drawdown. BND acted as a stabilizer; SPY provided equity exposure. Diversification was central to the risk–return improvement in the backtest.
- **Alignment with Efficient Market Hypothesis (EMH):**  
  - **Strengths:** The pipeline is consistent with using available information (historical data, forecasts) to form expectations. The optimizer and backtest are transparent and reproducible. The fact that the strategy did not beat the benchmark on raw return is consistent with markets being hard to beat.  
  - **Practical limitations:** EMH suggests that simple forecast-based rules may not generate persistent alpha. The backtest is one short period; improved Sharpe and drawdown could be luck or regime-specific. The LSTM forecast is based on past prices only and may not reflect future information. The report does not claim that the strategy will outperform in other periods or after costs.

---

## 6. Backtesting Results

- **Period:** January 2025 – January 2026 (~268 trading days).
- **Strategy:** 55.7% BND, 44.3% SPY, 0% TSLA; monthly rebalancing to these weights.
- **Benchmark:** 60% SPY / 40% BND, buy-and-hold.

| Metric                   | Strategy | Benchmark |
|--------------------------|----------|-----------|
| Total return             | 13.11%   | 15.01%    |
| Annualized return        | 12.28%   | 14.06%    |
| Annualized volatility    | 9.00%    | 11.72%    |
| Sharpe ratio (rf=0)      | 1.33     | 1.18      |
| Max drawdown             | -8.22%   | -11.29%   |

- **Did the strategy outperform?**  
  - **On total return:** No. The benchmark had higher total and annualized return.  
  - **On risk-adjusted performance:** Yes. The strategy had a higher Sharpe (1.33 vs 1.18) and a smaller (less negative) max drawdown (-8.22% vs -11.29%), with lower volatility (9.00% vs 11.72%).  

So the forecast-driven allocation **gave up some raw return in exchange for better risk-adjusted outcomes and drawdown control** in this single out-of-sample year. The tilt toward bonds (vs the 60/40 benchmark) reduced volatility and drawdown; whether this persists in other periods or with costs included is not tested here.

---

## 7. Limitations & Risk Disclosure

- **Execution and data:** Task 1 required a small code change to support current yfinance MultiIndex output (Adj Close/Close extraction). All six notebooks were executed; Task 1 is named `task1_data_preprocessing_eda.ipynb` (equivalent to “01” in the pipeline).
- **Backtest:** One year of out-of-sample data; results can be period-specific. No transaction costs, taxes, or slippage; rebalancing would reduce net returns in practice. No look-ahead bias in the described setup (weights from Task 5 use only pre-2025 data).
- **Models:** ARIMA and LSTM are based on historical prices (and returns). They do not incorporate fundamentals, macro, or news. LSTM is a black box; interpretability is limited. Multi-step LSTM forecasts are known to drift and underestimate uncertainty.
- **Optimization:** MPT is sensitive to expected return and covariance inputs. The extreme negative TSLA forecast drove 0% TSLA; different forecasts would change weights. Covariance is historical and may not reflect future regimes.
- **EMH:** If markets are efficient, sustained alpha from a simple forecast-based rule may be limited. The backtest is a single realization; improved Sharpe and drawdown could be partly luck. The report does not claim that the strategy will outperform in the future.

---

## 8. Final Conclusion for GMF Investment Committee

The project delivered a full chain from data and EDA through modeling, forecasting, MPT optimization, and backtesting. **LSTM was clearly better than ARIMA for TSLA in-sample and was used for the TSLA forecast.** That forecast was bearish and led the optimizer to recommend **no TSLA** and a **55.7% BND / 44.3% SPY** Max Sharpe portfolio.

In the only out-of-sample year tested (Jan 2025 – Jan 2026), this strategy **underperformed the 60/40 benchmark in total return** but **outperformed on Sharpe ratio and maximum drawdown**. So the work shows that forecast-driven allocation can change the risk–return profile meaningfully, but it does not demonstrate that the strategy will beat the benchmark on return in other periods or after costs.

**Suggested use:** Treat the Max Sharpe weights as a **candidate** allocation for risk-aware mandates, to be updated as new forecasts and data become available. Do not rely on this single backtest for strategic commitment; consider robustness checks (other periods, costs, alternative forecasts) and maintain appropriate disclosure of limitations and model risk in client materials.

---

*This report is based solely on outputs and results present in the project notebooks. No results have been invented. Where a metric or interpretation was not explicitly stated in the notebooks, it is either omitted or clearly flagged.*
