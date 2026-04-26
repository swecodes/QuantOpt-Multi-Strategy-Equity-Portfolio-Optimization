import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol,start_date, end_date):
    stock_data = yf.download(symbol,start= start_date, end = end_date)
    return stock_data
# the symbol in the above code is a ticker like - "AAPL"

# combine data from multiple companies into one table
def collect_portfolio_data(portfolio_symbols, start_date, end_date):
    portfolio_data = pd.DataFrame()
    for symbol in portfolio_symbols:
        asset_data = yf.download(symbol, start=start_date, end=end_date)
        asset_data = asset_data[['Close']].rename(columns={'Close': symbol})
        asset_data['Date' + f'_{symbol}'] = asset_data.index.date

        if portfolio_data.empty:
            portfolio_data = asset_data
        else:
            portfolio_data = portfolio_data.merge(asset_data, left_index = True, right_index = True, how = 'outer', suffixes = ('',f'_{symbol}'))
            # outer = if one stock is traded on a day when another did not, we keep the data for both rather than deleting the row
    
    return portfolio_data
if __name__ == "__main__":
    portfolio_symbols = ["AAPL", "MSFT", "GOOGL", "TSLA"]  # Example portfolio with multiple assets
    start_date = "2016-01-01"
    end_date = "2025-12-31"

    portfolio_data = collect_portfolio_data(portfolio_symbols, start_date, end_date)
    portfolio_data.to_csv("data/portfolio_data.csv", index=False)