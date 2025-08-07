from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo bro! Selamat datang di toko kami.\nKetik /order untuk mulai order.")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kamu belum menyebutkan nama barang. Contoh: /order sepatu")
        return
    item = " ".join(context.args)
    await update.message.reply_text(f"✅ Order kamu untuk *{item}* sudah kami terima!", parse_mode="Markdown")

if __name__ == '__main__':
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order))

    print("Bot berjadlan...")
    app.run_polling()
