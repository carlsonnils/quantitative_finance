from datetime import datetime
from polygon import RESTClient

client = RESTClient()

ticker = "AAPL"

aggs = client.get_aggs(
    ticker,
    1,
    "day",
    datetime(2023, 5, 22),
    datetime.today(),
)

print(len(aggs))