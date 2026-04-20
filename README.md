# Portfolio Optimization Engine

## dev/creator = tubakhxn

## About This Project
This project is a Python-based portfolio optimization engine that uses financial data to construct and analyze investment portfolios. It leverages the PyPortfolioOpt library to optimize asset allocation for maximum Sharpe ratio, minimum volatility, and to visualize the efficient frontier. The system also includes backtesting and comparison with an equal-weight portfolio, providing clear performance metrics and visualizations.

### Features
- Downloads historical price data for selected assets using yfinance
- Computes expected returns and covariance matrix
- Optimizes portfolio using PyPortfolioOpt (max Sharpe, min volatility)
- Generates and plots the efficient frontier
- Simulates and plots cumulative returns
- Compares optimized vs equal-weight portfolios

## How to Fork and Use
1. **Fork this repository** on GitHub to your own account.
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-username/portfolio-optimization-engine.git
   ```
3. **Install dependencies** (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the main script**:
   ```bash
   python -m portfolio_opt.main
   ```
5. **Modify tickers or parameters** in `main.py` as needed for your own analysis.

## Relevant Wikipedia Links
- [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)
- [Sharpe Ratio](https://en.wikipedia.org/wiki/Sharpe_ratio)
- [Efficient Frontier](https://en.wikipedia.org/wiki/Efficient_frontier)
- [Backtesting](https://en.wikipedia.org/wiki/Backtesting)
- [Portfolio Optimization](https://en.wikipedia.org/wiki/Portfolio_optimization)

---
For questions or contributions, please fork and submit a pull request.
