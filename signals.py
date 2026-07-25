from market import MarketData
from smc import analyze_smc
from telegram_bot import send_signal


async def scan_market():
    market = MarketData()

    df = market.get_candles()

    if df is None or len(df) < 100:
        print("No market data.")
        return

    signal = analyze_smc(df)

    if signal is None:
        print("No valid signal.")
        return

    await send_signal(signal)
