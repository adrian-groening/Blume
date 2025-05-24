from polygon import RESTClient
from pprint import pprint


client = RESTClient(api_key="XjabqthVtsWoU6Yen5gkeoG_dijvyceK")

ticker = "X:BTCUSD"

class Aggregate:
    def __init__(self, open, close, high, low, volume, vwap, timestamp, transactions, otc):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.vwap = vwap
        self.timestamp = timestamp
        self.transactions = transactions
        self.otc = otc
    def __repr__(self):
        return f"Aggregate(open={self.open}, close={self.close}, high={self.high}, low={self.low}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}, otc={self.otc})"

def convert_timestamp(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(timestamp / 1000)


# List Aggregates (Bars)
aggs = []

for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2025-05-20", to="2025-05-23", limit=50000):
    aggs.append(Aggregate(
        open=a.open,
        close=a.close,
        high=a.high,
        low=a.low,
        volume=a.volume,
        vwap=a.vwap,
        timestamp=convert_timestamp(a.timestamp),
        transactions=a.transactions,
        otc=a.otc
    ))
    
pprint(aggs)

# 1: Set up database
# 2: Feed polygon data into database
# 3: 
# 4: 







