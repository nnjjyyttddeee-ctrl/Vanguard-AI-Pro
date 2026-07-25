from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Vanguard AI Pro\n\n"
        "البوت اشتغل بنجاح.\n"
        "حالياً جاري تجهيز نظام التحليل المؤسسي..."
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Vanguard AI Pro Started")

    app.run_polling()

if __name__ == "__main__":
    main()
