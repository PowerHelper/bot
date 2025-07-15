import os
os.system("pip install pyTelegramBotAPI")
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت
TOKEN = '7898491089:AAH4_KwLOlrLj_tDrtaVub9WaSS9TKNbuGE'
bot = telebot.TeleBot(TOKEN)

# رابط موقع أدوات الذكاء الاصطناعي
AI_TOOLS_URL = "https://powerhelper.github.io/bot/index.html"

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "👛 مرحبًا بك في محفظتك الإلكترونية!\n"
        "🔗 اضغط على الزر أدناه لعرض الرصيد والتفاصيل.",
        reply_markup=get_wallet_button()
    )

# زر الدخول إلى المحفظة
def get_wallet_button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="👀 عرض المحفظة", url=WALLET_PAGE_URL))
    return markup

# تشغيل البوت
bot.polling()
