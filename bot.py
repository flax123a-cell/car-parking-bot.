import telebot

TOKEN = "9214094119:AAEz6c5GtG0_gwJkm-VcEfDDl3y-hoINomY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا بطل في بوت Car Parking Multiplayer! البوت يعمل بنجاح 24/7.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أهلاً بك! لقد استلمت رسالتك: {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
