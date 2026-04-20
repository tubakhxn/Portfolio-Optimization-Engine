"""
main.py
Main script to run the portfolio optimization workflow.
"""
import pandas as pd
from portfolio_opt import data, optimize, backtest, visualize

# 1. User parameters
tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "UNH", "PG", "DIS"
]
start = "2020-01-01"
end = "2024-01-01"

# 2. Data acquisition
prices = data.download_data(tickers, start, end)
mu, S = data.get_returns_and_cov(prices)

# 3. Optimization
opt_results = optimize.optimize_portfolio(prices)
weights_sharpe = opt_results["weights_sharpe"]
weights_minvol = opt_results["weights_minvol"]

# 4. Portfolio Output
visualize.display_allocation(weights_sharpe)

# 5. Backtesting
cum_returns = backtest.simulate_portfolio(prices, weights_sharpe)
cum_returns_eq = backtest.simulate_portfolio(prices, {t: 1/len(tickers) for t in tickers})

ret, vol, sharpe = backtest.compute_stats(cum_returns)
ret_eq, vol_eq, sharpe_eq = backtest.compute_stats(cum_returns_eq)

print(f"\nOptimized Portfolio: Return={ret:.2%}, Volatility={vol:.2%}, Sharpe={sharpe:.2f}")
print(f"Equal Weight Portfolio: Return={ret_eq:.2%}, Volatility={vol_eq:.2%}, Sharpe={sharpe_eq:.2f}")

# 6. Visualization (both graphs together)
visualize.plot_both(mu, S, weights_sharpe, weights_minvol, cum_returns, cum_returns_eq)
