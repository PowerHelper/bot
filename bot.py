from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram.ext import CallbackContext

# تعريف المراحل
STEP1, STEP2, STEP3 = range(3)

# المتغيرات التي سيتم جمعها من المستخدم
user_data = {}

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("مرحبًا! أود مساعدتك في إنشاء بورتفوليو. من فضلك، أخبرني باسمك:")
    return STEP1

def step1(update: Update, context: CallbackContext) -> int:
    user_data['name'] = update.message.text
    update.message.reply_text(f"شكرًا {user_data['name']}! الآن، من فضلك، قدم لي سيرتك الذاتية:")
    return STEP2

def step2(update: Update, context: CallbackContext) -> int:
    user_data['cv'] = update.message.text
    update.message.reply_text("شكرًا! الآن، من فضلك، قدم لي رابطًا لمحفظة أعمالك (إن وجد):")
    return STEP3

def step3(update: Update, context: CallbackContext) -> int:
    user_data['portfolio'] = update.message.text
    update.message.reply_text(f"شكرًا! لقد تم جمع بياناتك بنجاح.\n"
                              f"الاسم: {user_data['name']}\n"
                              f"السيرة الذاتية: {user_data['cv']}\n"
                              f"رابط المحفظة: {user_data['portfolio']}\n\n"
                              "لإنشاء البورتفوليو، اضغط على الرابط أدناه.")
    # هنا يمكنك إنشاء رابط لتحميل الملف أو صفحة العرض
    # على سبيل المثال يمكن استخدام Flask لإنشاء صفحة HTML ديناميكية
    update.message.reply_text("رابط البورتفوليو: https://yourwebsite.com/portfolio")
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("تم إلغاء العملية.")
    return ConversationHandler.END

def main():
    updater = Updater("7854834366:AAGvtpoZNuAWveD8lZVjKCSdzsku4mtXVtk", use_context=True)
    dp = updater.dispatcher
    
    # إعداد المحادثة
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STEP1: [MessageHandler(Filters.text & ~Filters.command, step1)],
            STEP2: [MessageHandler(Filters.text & ~Filters.command, step2)],
            STEP3: [MessageHandler(Filters.text & ~Filters.command, step3)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dp.add_handler(conv_handler)

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
