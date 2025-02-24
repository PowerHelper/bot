import telebot

# توكن بوت تيليجرام
TOKEN = '7854834366:AAGvtpoZNuAWveD8lZVjKCSdzsku4mtXVtk'
bot = telebot.TeleBot(TOKEN)

# روابط صفحات الهبوط لكل خدمة
LANDING_PAGES = {
    "netflix": "https://handswork.shop/",
    "spotify": "https://your-landing-page.com/spotify",
    "iptv": "https://your-landing-page.com/iptv"
}

# إرسال قائمة الخدمات عند الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "🎉 مرحبًا بك في بوت بيع الاشتراكات!\n"
        "اختر الخدمة التي تريدها بالنقر على أحد الأزرار أدناه:",
        reply_markup=get_main_menu()
    )

# إنشاء لوحة أزرار للخدمات
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    markup = InlineKeyboardMarkup()
    for service, url in LANDING_PAGES.items():
        markup.add(InlineKeyboardButton(text=f"اشتراك {service.capitalize()}", url=url))
    return markup

# تشغيل البوت
bot.polling()
