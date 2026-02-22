import pandas as pd
from datetime import datetime, timezone
from engine import get_daily_close_prices

start  = datetime(2016, 1, 1, tzinfo=timezone.utc)
end  = datetime(2026, 1, 1, tzinfo=timezone.utc)

tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "META", "XOM", "GLD"]

closes = get_daily_close_prices(tickers, start, end)

# for each timestamp (day) we do: return_t = [price_t / price_(t-1)] - 1, this results in pecentage movements...
returns = closes.pct_change().dropna()

corr = returns.corr()

# 1. Turn correlation matrix into list of pairs
# 2. Remove diagonal elements
# 3. Remove duplicate symmetric pairs.
corr_unstacked = corr.unstack() #1
corr_unstacked = corr_unstacked[corr_unstacked.index.get_level_values(0) != corr_unstacked.index.get_level_values(1)] #2
corr_unstacked = corr_unstacked[corr_unstacked.index.get_level_values(0) < corr_unstacked.index.get_level_values(1)] #3

# print()
# print(corr_unstacked)

most_negative_pair = corr_unstacked.idxmin()
most_negative_value = corr_unstacked.min()

print("Most negative pair:", most_negative_pair)
print("Correlation:", most_negative_value)
