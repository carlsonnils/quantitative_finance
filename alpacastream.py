import os
from alpaca_trade_api.common import URL
from alpaca_trade_api.stream import Stream

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(os.environ['APCA_API_KEY_ID'],
                os.environ['APCA_API_SECRET_KEY'],
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to 'sip' if you have PRO subscription

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
# stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()