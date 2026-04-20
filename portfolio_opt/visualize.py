"""
visualize.py
Handles plotting for portfolio optimization results.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Dict

from pypfopt import EfficientFrontier

def plot_efficient_frontier(mu, S, weights_sharpe, weights_minvol):
    from pypfopt import EfficientFrontier
    from pypfopt import EfficientFrontier
    # Find min and max volatility
    ef_min = EfficientFrontier(mu, S)
    ef_min.min_volatility()
def plot_both(mu, S, weights_sharpe, weights_minvol, cum_returns, cum_returns_eq):
    ef_min = EfficientFrontier(mu, S)
    ef_min.min_volatility()
    _, min_vol, _ = ef_min.portfolio_performance()
    ef_max = EfficientFrontier(mu, S)
    ef_max.max_sharpe()
    _, max_vol, _ = ef_max.portfolio_performance()
    risks = []
    rets = []
    for target_vol in np.linspace(min_vol, max_vol, 50):
        ef = EfficientFrontier(mu, S)
        try:
            ef.efficient_risk(target_vol)
            perf = ef.portfolio_performance()
            rets.append(perf[0])
            risks.append(perf[1])
        except ValueError:
            continue
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    # Efficient Frontier
    axs[0].plot(risks, rets, label="Efficient Frontier")
    ef.set_weights(weights_sharpe)
    ret_sharpe, vol_sharpe, _ = ef.portfolio_performance()
    axs[0].scatter([vol_sharpe], [ret_sharpe], marker="*", color="r", s=200, label="Max Sharpe")
    ef.set_weights(weights_minvol)
    ret_minvol, vol_minvol, _ = ef.portfolio_performance()
    axs[0].scatter([vol_minvol], [ret_minvol], marker="o", color="g", s=100, label="Min Volatility")
    axs[0].set_xlabel("Volatility (Std Dev)")
    axs[0].set_ylabel("Expected Return")
    axs[0].set_title("Efficient Frontier")
    axs[0].legend()
    # Cumulative Returns
    axs[1].plot(cum_returns.index, cum_returns.values, label="Optimized Portfolio")
    axs[1].plot(cum_returns_eq.index, cum_returns_eq.values, label="Equal Weight Portfolio", linestyle="--")
    axs[1].set_xlabel("Date")
    axs[1].set_ylabel("Cumulative Return")
    axs[1].set_title("Portfolio Cumulative Returns")
    axs[1].legend()
    plt.tight_layout()
    plt.show()
    plt.show()

def display_allocation(weights: Dict[str, float]):
    print("\nPortfolio Allocation:")
    for asset, weight in weights.items():
        print(f"{asset}: {weight:.2%}")
