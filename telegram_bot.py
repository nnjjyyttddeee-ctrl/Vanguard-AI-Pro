from telegram import Bot
from config import BOT_TOKEN, OWNER_ID

bot = Bot(token=BOT_TOKEN)


async def send_message(text):

    try:
        await bot.send_message(
            chat_id=OWNER_ID,
            text=text,
            parse_mode="Markdown"
        )

    except Exception as e:
        print(f"Telegram Error: {e}")


async def send_signal(signal):

    message = (
        "🔥 *Vanguard AI Pro*\n\n"
        f"📈 Signal: {signal.get('side', 'N/A')}\n"
        f"💰 Entry: {signal.get('entry', 'N/A')}\n"
        f"🛑 Stop Loss: {signal.get('sl', 'N/A')}\n"
        f"🎯 Take Profit: {signal.get('tp', 'N/A')}\n"
        f"📊 Confidence: {signal.get('confidence', 'N/A')}%\n"
        f"⚖️ RR: {signal.get('rr', 'N/A')}"
    )

    await send_message(message)
