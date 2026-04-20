"""
backtest.py
Simulates and evaluates portfolio performance.
"""
import pandas as pd
import numpy as np
from typing import Dict, Tuple

def simulate_portfolio(prices: pd.DataFrame, weights: Dict[str, float]) -> pd.Series:
    """
    Simulate portfolio cumulative returns given asset weights.
    """
    returns = prices.pct_change().dropna()
    weights_arr = np.array([weights[t] for t in prices.columns])
    port_returns = returns.dot(weights_arr)
    cum_returns = (1 + port_returns).cumprod()
    return cum_returns

def compute_stats(cum_returns: pd.Series) -> Tuple[float, float, float]:
    """
    Compute cumulative return, annualized volatility, and Sharpe ratio.
    """
    total_return = cum_returns.iloc[-1] - 1
    daily_returns = cum_returns.pct_change().dropna()
    vol = daily_returns.std() * np.sqrt(252)
    sharpe = (daily_returns.mean() * 252) / vol if vol != 0 else np.nan
    return total_return, vol, sharpe
