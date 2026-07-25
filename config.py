import os

# ==========================
# Telegram Configuration
# ==========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# ==========================
# Market Data API
# ==========================
TWELVE_API_KEY = os.getenv("TWELVE_API_KEY")

# ==========================
# Trading Settings
# ==========================
SYMBOL = "XAU/USD"

# Main timeframe
TIMEFRAME = "5min"

# Higher timeframe confirmations
HTF_1 = "15min"
HTF_2 = "1h"

# Number of candles to download
CANDLES = 500

# Scan interval (seconds)
SCAN_INTERVAL = 60

# ==========================
# Risk Management
# ==========================
RISK_PERCENT = 1.0
MIN_RR = 2.0
MIN_CONFIDENCE = 80

# ==========================
# Signal Filters
# ==========================
USE_TREND_FILTER = True
USE_FVG = True
USE_ORDER_BLOCK = True
USE_LIQUIDITY = True
USE_CHOCH = True
USE_BOS = True
USE_VOLUME_FILTER = True
