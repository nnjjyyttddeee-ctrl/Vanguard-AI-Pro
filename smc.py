import pandas as pd


class SMCAnalyzer:

    def __init__(self, df):
        self.df = df

    def trend(self):

        if len(self.df) < 200:
            return "UNKNOWN"

        ema50 = self.df["close"].rolling(50).mean().iloc[-1]
        ema200 = self.df["close"].rolling(200).mean().iloc[-1]

        if ema50 > ema200:
            return "BULLISH"

        if ema50 < ema200:
            return "BEARISH"

        return "RANGE"

    def swing_high(self):

        return self.df["high"].max()

    def swing_low(self):

        return self.df["low"].min()
