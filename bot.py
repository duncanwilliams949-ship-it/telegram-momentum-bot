import os
from telegram.ext import Updater, CommandHandler

# Get your Telegram bot token from environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Bot is running ✅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add /start command
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
