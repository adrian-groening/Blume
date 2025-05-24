from polygon import RESTClient
from pprint import pprint
import csv


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

def get_aggs(from_date, to_date, date_expansion):

    aggs = []
    for a in client.get_aggs(ticker=ticker, multiplier=1, timespan="minute", from_=from_date, to=date_expansion, limit=None):
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

    #omit results before from_date
    from_date = from_date.replace("-", "")
    to_date = to_date.replace("-", "")
    aggs = [agg for agg in aggs if from_date <= agg.timestamp.strftime('%Y%m%d') <= to_date]
    #omit results after to_date
    aggs = [agg for agg in aggs if agg.timestamp.strftime('%Y%m%d') <= to_date]

    return aggs


# List Aggregates (Bars)
aggs = []


# save to CSV
def save_aggs_to_csv(aggs, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Open', 'Close', 'High', 'Low', 'Volume', 'VWAP', 'Timestamp', 'Transactions', 'OTC'])
        for agg in aggs:
            writer.writerow([
                agg.open, agg.close, agg.high, agg.low, agg.volume,
                agg.vwap, agg.timestamp.isoformat(), agg.transactions, agg.otc
            ])

day = "2025-05-20"
d1 = get_aggs(day, day, "2025-05-21")
save_aggs_to_csv(d1, f'{day}_aggs.csv')





