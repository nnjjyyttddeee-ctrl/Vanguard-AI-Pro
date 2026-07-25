import pandas as pd


class SMCAnalyzer:

    def __init__(self, df):
        self.df = df.copy()

    def detect_swings(self, left=3, right=3):

        highs = []
        lows = []

        for i in range(left, len(self.df) - right):

            high = self.df["high"].iloc[i]

            if high == max(self.df["high"].iloc[i-left:i+right+1]):
                highs.append(i)

            low = self.df["low"].iloc[i]

            if low == min(self.df["low"].iloc[i-left:i+right+1]):
                lows.append(i)

        return highs, lows

    def detect_trend(self):

        ema50 = self.df["close"].rolling(50).mean()
        ema200 = self.df["close"].rolling(200).mean()

        if ema50.iloc[-1] > ema200.iloc[-1]:
            return "BULLISH"

        elif ema50.iloc[-1] < ema200.iloc[-1]:
            return "BEARISH"

        return "RANGE"

    def detect_bos(self):

        highs, lows = self.detect_swings()

        if len(highs) < 2 or len(lows) < 2:
            return None

        last_high = self.df["high"].iloc[highs[-1]]
        prev_high = self.df["high"].iloc[highs[-2]]

        last_low = self.df["low"].iloc[lows[-1]]
        prev_low = self.df["low"].iloc[lows[-2]]

        if last_high > prev_high:
            return "BULLISH_BOS"

        if last_low < prev_low:
            return "BEARISH_BOS"

        return None
