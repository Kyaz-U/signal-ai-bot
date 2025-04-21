import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from predict_model import predict_next_value

ADMIN_ID = 92058415
user_stats = {}

menu = ReplyKeyboardMarkup(
    keyboard=[
        ["🔮 Signal olish"],
        ["📊 Statistika"],
        ["⚙️ Sozlamalar"]
    ],
    resize_keyboard=True
)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Wersal AI botga xush kelibsiz.\nKerakli bo'limni tanlang:",
        reply_markup=menu
    )

# Xabarlar uchun handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == "🔮 Signal olish":
        data = [1.53, 2.44, 1.57, 5.11, 9.56, 2.02, 1.68, 1.13, 1.09, 4.19]
        model_path = "models/aviator_1win.pkl"
        result = predict_next_value(model_path, data)
        await update.message.reply_text(f"Aviator uchun signal: {result}")
        
        # Statistika hisoblash
        user_stats[user_id] = user_stats.get(user_id, 0) + 1

    elif text == "📊 Statistika":
        count = user_stats.get(user_id, 0)
        await update.message.reply_text(f"Foydalanuvchi statistikasi:\nID: {user_id} — {count} ta signal")

    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("Sozlamalar tez orada yangilanadi.")

    else:
        await update.message.reply_text("Iltimos, menyudan tugmalardan birini tanlang.")

# Botni ishga tushirish
if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
