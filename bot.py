import os
os.system("pip install pyTelegramBotAPI")
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن بوت تيليجرام
TOKEN = '7898491089:AAH4_KwLOlrLj_tDrtaVub9WaSS9TKNbuGE'
bot = telebot.TeleBot(TOKEN)

# رابط موقع أدوات الذكاء الاصطناعي
AI_TOOLS_URL = "https://powerhelper.github.io/bot/index.html"

# إرسال رسالة الترحيب عند الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "🤖 مرحبًا بك في موقع أدوات الذكاء الاصطناعي الخاص بنا!\n"
        "🔗 اضغط على الزر أدناه للاستفادة من أحدث أدوات الذكاء الاصطناعي.",
        reply_markup=get_tools_button()
    )

# إنشاء زر لزيارة الموقع
def get_tools_button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🔍 زيارة موقع الأدوات", url=AI_TOOLS_URL))
    return markup

# تشغيل البوت
bot.polling()
