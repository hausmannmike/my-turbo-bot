import pandas as pd
from datetime import datetime, timezone
from engine import get_daily_close_prices

start  = datetime(2023, 1, 1, tzinfo=timezone.utc)
end  = datetime(2024, 1, 1, tzinfo=timezone.utc)

aapl = get_daily_close_prices("AAPL", start, end)
msft = get_daily_close_prices("MSFT", start, end)

prices = pd.concat([aapl, msft], axis=1)
prices.columns = ["AAPL", "MSFT"]

# for each timestamp (day) we do: return_t = [price_t / price_(t-1)] - 1, this results in pecentage movements...
returns = prices.pct_change().dropna()

corr = returns["AAPL"].corr(returns["MSFT"])

# print(prices)
print(returns)
print()
print("Correltion between AAPL and MSFT: ", corr)
