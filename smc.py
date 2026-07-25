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

    def detect_choch(self):

        trend = self.detect_trend()
        bos = self.detect_bos()

        if trend == "BULLISH" and bos == "BEARISH_BOS":
            return "BEARISH_CHOCH"

        if trend == "BEARISH" and bos == "BULLISH_BOS":
            return "BULLISH_CHOCH"

        return None

    def detect_fvg(self):

        gaps = []

        for i in range(2, len(self.df)):

            high1 = self.df["high"].iloc[i - 2]
            low3 = self.df["low"].iloc[i]

            low1 = self.df["low"].iloc[i - 2]
            high3 = self.df["high"].iloc[i]

            if low3 > high1:
                gaps.append({
                    "type": "BULLISH",
                    "index": i,
                    "top": low3,
                    "bottom": high1
                })

            elif high3 < low1:
                gaps.append({
                    "type": "BEARISH",
                    "index": i,
                    "top": low1,
                    "bottom": high3
                })

        return gaps

    def detect_liquidity(self, tolerance=0.10):

        highs, lows = self.detect_swings()

        equal_highs = []
        equal_lows = []

        for i in range(1, len(highs)):
            h1 = self.df["high"].iloc[highs[i - 1]]
            h2 = self.df["high"].iloc[highs[i]]

            if abs(h1 - h2) <= tolerance:
                equal_highs.append(highs[i])

        for i in range(1, len(lows)):
            l1 = self.df["low"].iloc[lows[i - 1]]
            l2 = self.df["low"].iloc[lows[i]]

            if abs(l1 - l2) <= tolerance:
                equal_lows.append(lows[i])

        return equal_highs, equal_lows
