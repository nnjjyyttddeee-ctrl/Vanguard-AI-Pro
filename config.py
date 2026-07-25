import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Twelve Data API
TWELVE_API_KEY = os.getenv("TWELVE_API_KEY")

# Trading
SYMBOL = "XAU/USD"
TIMEFRAME = "5min"
CANDLES = 500

# Risk Management
RISK_PERCENT = 1.0
MIN_RR = 2.0
MIN_CONFIDENCE = 80
