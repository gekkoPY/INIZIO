Welcome to my personal collection of financial analysis tools aimed at extracting insights from market data using Python. This repository documents my journey from basic plotting to advanced portfolio optimization algorithms.




🚀 Projects Overview
1. 🦄 The Portfolio Optimiser (best_allocation.py) [NEW 🔥]
My most advanced project yet. A full-scale Monte Carlo Simulation engine designed to find the mathematically optimal portfolio.

Mission: Fires 50,000+ simulations to find the exact asset allocation that maximizes returns relative to risk (Max Sharpe Ratio).

Tech Stack: NumPy (Heavy Math), Pandas, Matplotlib (Dual-Window Dashboard).

Key Features:

Efficient Frontier Visualization: A scatter plot visualizing the risk-return trade-off and highlighting the optimal strategy.

Wealth Simulator: Tracks how a $10k investment transforms over 10 years (finding +2,000% returns strategies).

Smart Auto-Adjust: Automatically handles dividends and stock splits using auto_adjust=True.




2. 🎯 Portfolio Sniper (portfolio_sniper.py)
A precision tool for deep-dive risk analysis of a basket of assets.

Focus: Instead of optimizing weights, it analyzes the quality of individual assets and their relationships.

Key Features:

Correlation Heatmap: A professional, dark-themed correlation matrix to spot diversification opportunities (or dangerous overlaps).

Risk Metrics: Calculates Sharpe Ratio AND Sortino Ratio (which only penalizes downside volatility) for every single asset.




3. 🆚 Asset Comparator (Asset comparator.py)
A powerful tool that compares two user-selected assets (e.g., AAPL vs. TSLA) and challenges them against the S&P 500 market benchmark.

Tech Stack: yfinance, Pandas, Plotly.

Key Features:

Cumulative return calculation (Normalizing assets to 0%).

Interactive chart opened directly in your browser.




4. 📊 Interactive Stock Graph (interactive stock graph.py)
A detailed visualization tool for single-stock analysis.

Includes interactive line charts and technical indicators.

Designed for deep-dives into historical price actions.




5. 📉 Static Stock Graph (static stock graph.py)
My very first financial data visualization project using Matplotlib.

Focuses on clean, static price trend analysis over a 2-year period.

Useful for quick snapshots and generating reports.




🛠️ How to use
Clone this repository:
git clone https://github.com/gekkoPY/financial-tools.git



Install dependencies:
pip install pandas yfinance plotly matplotlib numpy seaborn



Run a tool (e.g., The Optimiser):
python best_allocation.py


Created by gekkoPY - Powered by Python, Financial Data, and a lot of coffee ☕
