import os
from dotenv import load_dotenv

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

load_dotenv()


# function that, given: a ticker, start date and end date, fetches its daily close prices in that time interval.
def get_daily_close_prices(ticker, start_date, end_date):
    api_key = os.getenv("ALPACA_API_KEY")
    secret_key = os.getenv("ALPACA_SECRET_KEY")

    client = StockHistoricalDataClient(api_key, secret_key)
        
    request = StockBarsRequest(
        symbol_or_symbols=[ticker], 
        start=start_date,
        end=end_date,
        timeframe=TimeFrame.Day    
    )

    bars = client.get_stock_bars(request)
    closes = bars.df["close"]
    closes = closes.droplevel("symbol")
    return closes.head()



