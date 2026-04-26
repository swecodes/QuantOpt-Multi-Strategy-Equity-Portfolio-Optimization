import pandas as pd
import numpy as np

def calculate_portfolio_metrics(data):
    # 1. Identify only the specific columns we want to analyze
    # Try to find "Log Returns" first; if not, use the raw tickers
    returns_columns = [col for col in data.columns if "Log Returns" in col]
    if not returns_columns:
        returns_columns = [col for col in data.columns if "Date_" not in col]
    
    # 2. Select ONLY those columns and convert to numeric
    # This prevents the "Date_" columns from being in our math slice
    asset_data = data[returns_columns].apply(pd.to_numeric, errors='coerce')

    # 3. Drop rows ONLY if they are missing values in OUR selected columns
    asset_data = asset_data.dropna()

    # DEBUG: Check if we have data left
    if asset_data.empty:
        raise ValueError("The dataset is empty after dropping missing values. Check your date ranges!")

    num_assets = len(asset_data.columns)
    weights = np.array([1 / num_assets] * num_assets)

    # 4. Math (Now it won't be empty!)
    mean_returns = asset_data.mean()
    portfolio_return = np.sum(weights * mean_returns)
    cov_matrix = asset_data.cov()
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    return {
        "Portfolio Return": portfolio_return,
        "Portfolio Risk": portfolio_risk,
        "Mean Returns": mean_returns,
        "Weights": weights,
    }
    
    #return portfolio_metrics