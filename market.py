import requests
import pandas as pd

class MarketData:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_candles(self, symbol="XAU/USD", interval="5min", outputsize=500):

        url = (
            f"https://api.twelvedata.com/time_series"
            f"?symbol={symbol}"
            f"&interval={interval}"
            f"&outputsize={outputsize}"
            f"&apikey={self.api_key}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        if "values" not in data:
            return None

        df = pd.DataFrame(data["values"])

        df = df.rename(columns={
            "datetime": "time"
        })

        df = df.iloc[::-1].reset_index(drop=True)

        numeric = ["open", "high", "low", "close"]

        for col in numeric:
            df[col] = df[col].astype(float)

        return df
