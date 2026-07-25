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
import os
import time
import requests
from flask import Flask
from threading import Thread

TOKEN = "8801659495:AAHWnlrmzhV56VoSjZ2cmOwG3S2ov3iBkAo"
ADMIN_ID = 7390368263
URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask('')

@app.route('/')
def home():
    return "Vanguard AI Pro is Online!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def send_message(chat_id, text):
    try:
        requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": text}, timeout=10)
    except Exception:
        pass

def trading_signals_loop():
    while True:
        try:
            alert_text = "🚨 تنبيه إشارة جديدة 📊 السعر / التفاصيل واردة من المنصة بنجاح.\nالأصول: الذهب (XAUUSD) 🥇 | الناسداك (US100) 💻 | الداو جونز (US30) 🏭 | الإيثريوم (ETHUSD) 🌐"
            send_message(ADMIN_ID, alert_text)
        except Exception:
            pass
        time.sleep(900)

def bot_loop():
    offset = 0
    while True:
        try:
            response = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 30}, timeout=35)
            data = response.json()
            if data.get("ok"):
                for update in data.get("result", []):
                    offset = update["update_id"] + 1
                    message = update.get("message")
                    if message:
                        chat_id = message["chat"]["id"]
                        text = message.get("text", "")
                        if text == "/start":
                            send_message(chat_id, "🔥 Vanguard AI Pro\n\nالبوت يعمل بنجاح.\nبدأت مراقبة السوق وإرسال الإشارات على مدار 24 ساعة.")
        except Exception:
            time.sleep(5)
        time.sleep(1)

if __name__ == "__main__":
    t_web = Thread(target=run_web)
    t_web.daemon = True
    t_web.start()

    t_signals = Thread(target=trading_signals_loop)
    t_signals.daemon = True
    t_signals.start()

    bot_loop()
    
