import telebot


API_TOKEN = '8161959414:AAGpMJGaXgoy3jmrXgXsq1Vq5BdjzS314wc'

bot = telebot.TeleBot("8161959414:AAGpMJGaXgoy3jmrXgXsq1Vq5BdjzS314wc")

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm your bot. Type /help to see what I can do.")

# /help command handler
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Available commands:\n" \
                "/start - Welcome message\n" \
                "/help - Show help\n" \
                "/echo <text> - Repeat what you say"
    bot.reply_to(message, help_text)

# /echo command handler
@bot.message_handler(commands=['echo'])
def echo_message(message):
    args = message.text.split()[1:]
    if args:
        bot.reply_to(message, ' '.join(args))
    else:
        bot.reply_to(message, "Please provide text to echo. Example: /echo Hello World!")

# Default text handler (optional)
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "I didn't recognize that command. Use /help to see available commands.")

# Start polling (listening for messages)
print("Bot is running...")
bot.infinity_polling()
