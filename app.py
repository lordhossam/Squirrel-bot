from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # الحصول على اسم المستخدم
    user = update.effective_user
    user_first_name = user.first_name
    
    # إرسال الصورة مع الوصف
    photo_url = "D:\Game Squirrel Coins\photo\Gift Christmas.PNG"  # استبدل برابط الصورة الفعلي
    description = f"Welcome to Squirrel Coins, {user_first_name}! 🎉\n\n" \
                  "You are now ready to enter the game and start collecting coins. \n\n" \
                  "Choose one of the options below to get started:"

    keyboard = [
        [InlineKeyboardButton("Enter The Squirrel Coins", web_app=dict(url="https://squirrelcoins.whf.bz/"))],
        [InlineKeyboardButton("Join Channel", url="https://t.me/TradingGenius10")],
        [InlineKeyboardButton("Follow X", url="https://twitter.com/your-twitter")],
        [InlineKeyboardButton("Invite a Friend", callback_data='invite_friend')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=description, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    if query.data == 'invite_friend':
        user_id = query.from_user.id
        invite_link = f"https://t.me/Squirrel_Coins10_bot?start=ref_{user_id}"
        
        message = f"Invite your friends and get bonuses for each invited friend! 🎁\n\nYour referral link: {invite_link}"
        
        await query.answer()
        await query.edit_message_text(text=message)

def main() -> None:
    application = ApplicationBuilder().token("7086693986:AAGhA8Nm5ai2C69lrAm8Bg8rY79CJPWbnVM").build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == '__main__':
    main()
