import pandas as pd
from datetime import datetime, timezone
from engine import get_daily_close_prices

start  = datetime(2023, 1, 1, tzinfo=timezone.utc)
end  = datetime(2024, 1, 1, tzinfo=timezone.utc)

aapl = get_daily_close_prices("AAPL", start, end)
msft = get_daily_close_prices("MSFT", start, end)

prices = pd.concat([aapl, msft], axis=1)
prices.columns = ["AAPL", "MSFT"]

# print(prices)
print(prices)
print()
