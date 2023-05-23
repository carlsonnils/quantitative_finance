import os
from alpaca.trading.client import TradingClient
from alpaca.data.live.stock import StockDataStream
from alpaca.data.live.crypto import CryptoDataStream
# from alpaca.data import CryptoDataStream
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime


API_KEY = os.environ['API_KEY_ID']
SECRET_KEY = os.environ['SECRET_KEY']


###########
#
# Trading
#
# ###########
# trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# account = trading_client.get_account()
# print(account)
# for property_name, value in account:
#   print(f"\"{property_name}\": {value}")


###########
#
# Market Data
#
###########
# wss_client = CryptoDataStream(API_KEY, SECRET_KEY)

# async def quote_data_handler(data):
#     print(data)
#     print("in async func")
#     return data

# wss_client.subscribe_quotes(quote_data_handler, "SPY")
# print('subscribed')
# wss_client.run()
# print('ran')



# # keys required for stock historical data client
# client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

# # multi symbol request - single symbol is similar
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

# gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price

# print(gld_latest_ask_price)

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=[
                            "BTC/USD", 
                            "ETH/USD"
                        ],
                        timeframe=TimeFrame.Day,
                        start=datetime(2015, 1, 1),
                        end=datetime(2023, 5, 21)
                 )

bars = client.get_crypto_bars(request_params)

# convert to dataframe
bars.df.to_parquet('test_data.parquet')
bars.df.to_csv('test_data.csv')

# access bars as list - important to note that you must access by symbol key
# even for a single symbol request - models are agnostic to number of symbols
bars["BTC/USD"]
print(bars.df)