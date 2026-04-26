# QuantOpt-Multi-Strategy-Equity-Portfolio-Optimization
![Efficient Frontier](efficient_frontier.png)
This project demonstrates a rigorous end-to-end quantitative finance pipeline, moving from raw market data acquisition to the deployment of modern portfolio optimization strategies. Unlike basic financial scripts, this repository implements a dual-strategy approach comparing Mean-Variance Optimization (Sharpe-Max) against Risk Parity, accounting for real-world constraints such as capital allocation limits and non-finite data handling.

Portfolio Optimization and Quantitative Analysis
Project Overview
The objective of this project is to construct an optimal investment portfolio using high-growth technology assets: AAPL, MSFT, GOOGL, and TSLA. The analysis bridges the gap between raw historical data and actionable investment intelligence through statistical modeling and numerical optimization.

Core Methodologies
Exploratory Data Analysis (EDA): Comprehensive analysis of historical trends, daily returns distribution (clipped at ±20% to manage outliers), and 50-day rolling statistics to assess stationarity and volatility clusters.

Modern Portfolio Theory (MPT): Implementation of the Efficient Frontier using Monte Carlo simulations (1,000 iterations) to visualize the risk-return spectrum.

Sharpe-Max Optimization: A predictive model designed to maximize the risk-adjusted return by solving for the highest possible Sharpe Ratio using the SLSQP (Sequential Least Squares Programming) algorithm.

Risk Parity (Novel Method): A risk-centric approach that equalizes the marginal risk contribution of each asset, ensuring the portfolio is not overly dependent on a single high-volatility stock like Tesla.

Key Performance Results
The optimization yielded two distinct investment profiles based on the analysis of 1,000 trading days:

Metric	Sharpe-Max (Profit Focused)	Risk Parity (Stability Focused)
Annualized Return	36.48%	26.68%
Annualized Volatility	41.47%	32.56%
Sharpe Ratio	0.81	0.73
Primary Allocation	TSLA (42.6%), AAPL (32.2%)	Balanced (~25-28% each)
Analysis of Results: The Sharpe-Max strategy identified Apple and Tesla as the primary drivers of growth, whereas the Risk Parity strategy reintroduced a significant position in Google (28%) to act as a volatility buffer, reducing total portfolio risk by nearly 9% absolute.

Technical Implementation
Data Engineering: Automated fetching via yfinance with a robust preprocessing layer to handle log-normal returns and filter non-finite values.

Optimization Engine: Utilizes scipy.optimize with budget constraints (∑w=1) and asset bounds (0≤w≤1).

Visualization: High-fidelity plotting of the Efficient Frontier, including the Capital Allocation Line (CAL) and comparison markers for key strategies.

Repository Structure
scripts/data_collection.py: Modular logic for API interaction and data persistence.

scripts/data_preprocessing.py: Statistical cleaning and feature engineering.

scripts/optimization.py: Numerical solvers for Sharpe and Risk Parity models.

portfolio_optimization.ipynb: Executive workflow and visualization of results.

This project serves as a template for applying modern quantitative techniques to standard equity portfolios, providing a framework for objective decision-making in capital allocation.
