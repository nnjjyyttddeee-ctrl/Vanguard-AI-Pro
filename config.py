import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Owner
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Timeframes
TIMEFRAME = "M5"

# Symbols
SYMBOLS = [
    "XAUUSD"
]

# Risk Management
RISK_PERCENT = 1.0

# Signal Settings
MIN_RR = 2.0
MIN_CONFIDENCE = 80
