import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN, SCAN_INTERVAL
from signals import scan_market


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Vanguard AI Pro\n\n"
        "البوت يعمل بنجاح.\n"
        "بدأت مراقبة السوق وإرسال الإشارات."
    )


async def market_loop():
    while True:
        try:
            await scan_market()
        except Exception as e:
            print(f"Market Error: {e}")

        await asyncio.sleep(SCAN_INTERVAL)


async def on_start(app):
    asyncio.create_task(market_loop())


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(on_start).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Vanguard AI Pro Started")

    app.run_polling()


if __name__ == "__main__":
    main()
