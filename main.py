import pandas as pd
from datetime import datetime, timezone
from engine import get_daily_close_prices

start  = datetime(2023, 1, 1, tzinfo=timezone.utc)
end  = datetime(2024, 1, 1, tzinfo=timezone.utc)

tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "META", "XOM", "GLD"]

prices = pd.DataFrame()

for ticker in tickers:
    closes = get_daily_close_prices(ticker, start, end)
    closes.name = ticker
    prices = pd.concat([prices, closes], axis=1)

# for each timestamp (day) we do: return_t = [price_t / price_(t-1)] - 1, this results in pecentage movements...
returns = prices.pct_change().dropna()

corr = returns.corr()

# print(prices)
print(returns)
print()
print("Correltion Matrix:")
print(corr)