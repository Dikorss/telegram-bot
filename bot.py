import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔑 ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ BOTFATHER
TOKEN = "8738791326:AAEPwG1yHAsHzXGP3KmyTnfWK8Q5UeeeNOg"

def is_tiktok(url):
    return "tiktok.com" in url

def download_video(url):
    try:
        api = f"https://tikwm.com/api/?url={url}"
        r = requests.get(api, timeout=10).json()
        return r["data"]["play"]
    except:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Отправь TikTok ссылку 📥")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if is_tiktok(text):
        await update.message.reply_text("⏳ Скачиваю видео...")

        video = download_video(text)

        if video:
            await update.message.reply_video(video)
        else:
            await update.message.reply_text("❌ Не удалось скачать видео")
    else:
        await update.message.reply_text("📌 Пришли TikTok ссылку")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

print("🤖 Бот запущен...")
app.run_polling()
