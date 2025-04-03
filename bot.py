import telebot
from gtts import gTTS
import os

# Telegram bot token
BOT_TOKEN = "7224882890:AAHLe_G7vHnBLcL60cfThYAoKTOb0Xb5IIw"

# Bot initialize
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "मुझे कोई भी text भेजो, मैं उसे आवाज़ में बदल दूँगा!")

@bot.message_handler(func=lambda message: True)
def text_to_speech(message):
    try:
        text = message.text
        lang = "hi" if any("\u0900" <= char <= "\u097F" for char in text) else "en"
        
        # Text ko speech me convert karna
        tts = gTTS(text=text, lang=lang)
        filename = f"{message.chat.id}.mp3"
        tts.save(filename)

        # Audio send karna
        with open(filename, "rb") as voice:
            bot.send_audio(message.chat.id, voice)
        
        # File delete karna
        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, "कुछ गलती हो गई 😕\nError: " + str(e))

# Bot ko run karna
print("Bot is running...")
bot.polling()
