"""
optimize.py
Performs portfolio optimization using PyPortfolioOpt.
"""
from pypfopt import EfficientFrontier, risk_models, expected_returns
import numpy as np
import pandas as pd
from typing import Tuple, Dict

def optimize_portfolio(prices: pd.DataFrame) -> Dict[str, np.ndarray]:
    """
    Optimize portfolio for max Sharpe, min volatility, and generate efficient frontier.
    Returns dict with optimal weights and frontier data.
    """
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)
    ef = EfficientFrontier(mu, S)
    weights_sharpe = ef.max_sharpe()
    cleaned_weights_sharpe = ef.clean_weights()
    ret_sharpe, vol_sharpe, sharpe_ratio = ef.portfolio_performance()

    ef = EfficientFrontier(mu, S)
    weights_minvol = ef.min_volatility()
    cleaned_weights_minvol = ef.clean_weights()
    ret_minvol, vol_minvol, sharpe_minvol = ef.portfolio_performance()

    return {
        "weights_sharpe": cleaned_weights_sharpe,
        "weights_minvol": cleaned_weights_minvol,
        "mu": mu,
        "S": S,
        "ret_sharpe": ret_sharpe,
        "vol_sharpe": vol_sharpe,
        "sharpe_ratio": sharpe_ratio,
        "ret_minvol": ret_minvol,
        "vol_minvol": vol_minvol,
        "sharpe_minvol": sharpe_minvol
    }
