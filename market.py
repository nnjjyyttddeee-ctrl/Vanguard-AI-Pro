import requests
import pandas as pd
from config import TWELVE_API_KEY


class MarketData:

    BASE_URL = "https://api.twelvedata.com/time_series"

    def __init__(self, api_key=TWELVE_API_KEY):
        self.api_key = api_key

    def get_candles(self, symbol="XAU/USD", interval="5min", outputsize=500):

        params = {
            "symbol": symbol,
            "interval": interval,
            "outputsize": outputsize,
            "apikey": self.api_key,
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=15)
            response.raise_for_status()

            data = response.json()

            if "values" not in data:
                print("API Error:", data)
                return None

            df = pd.DataFrame(data["values"])

            df = df.rename(columns={"datetime": "time"})
            df = df.iloc[::-1].reset_index(drop=True)

            numeric = ["open", "high", "low", "close"]

            for col in numeric:
                df[col] = pd.to_numeric(df[col], errors="coerce")

            if "volume" in df.columns:
                df["volume"] = pd.to_numeric(df["volume"], errors="coerce")

            df = df.dropna()

            return df

        except Exception as e:
            print(f"Market Error: {e}")
            return None
