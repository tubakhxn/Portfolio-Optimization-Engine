"""
data.py
Handles data acquisition and preprocessing for portfolio optimization.
"""
import yfinance as yf
import pandas as pd
from typing import List, Tuple

def download_data(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Download daily close prices for given tickers from Yahoo Finance.
    Returns a DataFrame with tickers as columns and dates as index.
    """
    data = yf.download(tickers, start=start, end=end)
    # Extract 'Close' prices for all tickers
    close = data.xs('Close', axis=1, level=0)
    return close.dropna()

def get_returns_and_cov(prices: pd.DataFrame) -> Tuple[pd.Series, pd.DataFrame]:
    """
    Compute expected returns and sample covariance matrix of asset returns.
    """
    returns = prices.pct_change().dropna()
    mu = returns.mean() * 252  # annualized
    cov = returns.cov() * 252  # annualized
    return mu, cov
