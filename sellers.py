
import logging
import json
from typing import Final
import database
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,ConversationHandler,MessageHandler,filters,CallbackContext
from telegram import Bot, InputMediaPhoto


TOKEN: Final = '6007793381:AAG23oNb9zBsho7de-m_yzgdTumWB1N3bdI'
BOt_USERNAME : Final = '@beta_market_bot'
print('Starting up bot...')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

aNSWER, aNSWER2, aNSWER3, aNSWER4, aNSWER5,aNSWER6,aNSWER7,aNSWER8,aNSWER9 =range(9)

bot = Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 **Welcome to Addis Market!** 🎉\n\n"
                                    "እንኳን ወደ አዲስ ገበያ በደህና መጡ\n\n"
        "🛍️ This is the bot where you can buy products other people post.\n"
        "ይህ ሌሎች ሰዎች የሚለጥፉትን ምርቶችን የሚገዙበት ቦታ ነው.\n\n"
        "📦 If you are looking to buy products, go to @Addis_market_bot\n\n"
        "🔍 Add the type of product you want to sell.\nPlease make it general.\nFor example: phone, house, shoes, laptop, car.\n\n"
        "🔍 ለመግዛት የሚፈልጉት የምርት አይነት አስገቡ.\n"
        "ለምሳሌ ፡- ስልክ፣ ቤት ፣ ጫማ፣ ላፕቶፕ ፣ መኪና")
    return aNSWER
    
async def ANSWER(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    product_type = update.message.text.lower()
    if product_type =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        context.user_data['product_type'] = product_type
        await update.message.reply_text(f'💰Add the price of your product in birrs.\nExample: 450, 2000, 1000000.\nMake sure you input only a number and do not include "birr".\n\n💰የምርትዎን ዋጋ በብር ይጨምሩ።\nለምሳሌ ፡- 450, 2000, 1000000።\nቁጥር ብቻ ማስገባትዎን ያረጋግጡ እና "ብር" አያካትቱ።')
    return aNSWER2

async def ANSWER2(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    if update.message.text.lower() == '/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        try:
            price = float(update.message.text)
            context.user_data['price'] = price
        except ValueError:
            await update.message.reply_text(f'⚠️Invalid response. Please enter a number.\n💰Add the price of your product in birrs.\n⚠️Example: 450, 2000, 1000000.\nMake sure you input only a number and do not include "birr".\n\nልክ ያልሆነ ምላሽ ነው ይስገቡት እባክዎን ቁጥር ይስገባ።\n💰የምርትዎን ዋጋ በብር ይጨምር።\nለምሳሌ ፡- 450, 2000, 1000000።\nቁጥር ብቻ ማስገባትዎን ያረጋግጡ እና "ብር" አያካትቱ።')
            return aNSWER2
        username = update.message.from_user.username
    await update.message.reply_text(f"📞 Would you like to be contacted at @{username}?\nIf so, please reply with ‘yes’.\n\nIf not, please provide the Telegram username account you would like to be contacted by.\nExample:- @abebe, @1234_abebe\n\n📞በ @{username} ገዢዎች እንዲያገኑት ይፈልጋሉ።\nከሆነ 'አዎ' ብለው ይመልሱ።\n\nይህ ካልሆነ ሊገኑ የሚፈልጉትን የቴሌግራም ስም ያጨምር።\nለምሳሌ፡- @abebe, @1234_abebe")
    return aNSWER3

async def ANSWER3(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    user_name = update.message.text.lower()
    if user_name =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        if user_name !='yes':
            context.user_data['user_name'] = user_name
        else:
            context.user_data['user_name'] = update.message.from_user.username
        
        await update.message.reply_text(f'📞Add your phone number so potential buyers can contact you.\nExample:- 0911111111, 251911111111\n\n📞ገዥዎች እርስዎን ማግኘት እንዲችሉ ስልክ ቁጥርዎን ያክሉ።\nለምሳሌ፡- 0911111111፣ 251911111111')
    return aNSWER4

async def ANSWER4(update: Update,context: ContextTypes.DEFAULT_TYPE)-> int:
    if update.message.text.lower() == '/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        try:
            phone_number = int(update.message.text)
            context.user_data['phone_number'] = phone_number
        except ValueError:
            await update.message.reply_text(f'⚠️Invalid response.Please enter a number.\n📞Add your phone number so potential buyers can contact you.\nExample:- 0911111111, 251911111111\n\n⚠️ልክ ያልሆነ ምላሽ ነው። ይስገቡት እባክዎን ቁጥር ይስገባ።\n📞ገዥዎች እርስዎን ማግኘት እንዲችሉ ስልክ ቁጥርዎን ያክሉ።\nለምሳሌ፡- 0911111111፣ 251911111111')
            return aNSWER4
    await update.message.reply_text(f'🔵Please input one of the following states for your product:\nStates: Brand New, Slightly Used, Used\n\n'
                                    f'🔵ለምርትዎ ከ3ቱ ይዘቶች ውስጥ አንዱን ብቻ ያስገቡ።\nይዘቶች- አዲስ፣ ትንሽ ጥቅም ላይ የዋለ፣ ጥቅም ላይ የዋለ')  
    return aNSWER5
    
async def ANSWER5(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    status = update.message.text.lower()
    if status =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        context.user_data['status'] = status
        await update.message.reply_text(f'📝 Please add a description of the product.\n This can include the specific model of the product.\nExample:- iphone 8 , nike ,adidas.\n\n'
                                        f'📝የምርቱን መግለጫ ያክሉ።\nይህ የምርቱን ልዩ ሞዴል ሊያካትት ይችላል።\nለምሳሌ፡- iphone 8፣ nike ፣ adidas።\n\n'
                                        f'if it’s your first time, we highly recommend checking out https://t.me/Addis_Market_channel/3\n\n'
                                        f'ጥሩ መግለጫ እንዴት እንደሚጽፉ የበለጠ መረጃ ክፊለጉ https://t.me/Addis_Market_channel/3 ን ይመልከቱ')
    
    return aNSWER6
async def ANSWER6(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    description = update.message.text.lower()
    if description =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        context.user_data['description'] = description
        await update.message.reply_text(f'📸 Please add the first of three photos of your product.\nYou can also add another photo,once you have added this one.\n\n'
                                        f'📸የምርትዎን ከሶስት ፎቶዎች ውስጥ የመጀመሪያዎን ያስገቡ።\nይህንን ፎቶ አንዴ ካከሉ በኋላ ሌላ ፎቶ ማስገባት ይችላሉ።')
    return aNSWER7

async def ANSWER7(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    """Stores the photo metadata"""
    photo1 = update.message.from_user
    photo_file1 = await update.message.photo[-1].get_file()
    # Save the JSON format of the incoming photo in a variable
    photo_json1 = photo_file1.to_dict()
    photo_json1_string = json.dumps(photo_json1)
    context.user_data['photo_json1_string'] = photo_json1_string
    context.user_data['photo_file1']= photo_file1
    
    await update.message.reply_text(f'📸 Please add a second photo of your product\n\n'
                                    f'📸 እባክዎ የምርትዎን ሁለተኛ ፎቶ ያክሉ')

    return aNSWER8
async def ANSWER8(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    photo2= update.message.from_user
    photo_file2= await update.message.photo[-1].get_file()
    
    photo_json2 = photo_file2.to_dict()
    photo_json2_string = json.dumps(photo_json2)
    context.user_data['photo_json2_string'] = photo_json2_string
    context.user_data['photo_file2']= photo_file2
    
    await update.message.reply_text(f'📸 Please add the last photo of your product\n\n'
                                    f'📸 እባክዎ የምርትዎን የመጨረሻ ፎቶ ያክሉ')
    return aNSWER9

async def ANSWER9(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    photo3 = update.message.from_user
    photo_file3 = await update.message.photo[-1].get_file()
    
    photo_json3 = photo_file3.to_dict()
    photo_json3_string = json.dumps(photo_json3)
    context.user_data['photo_json3_string'] = photo_json3_string
    
    product_type = context.user_data['product_type']
    price = context.user_data['price']
    user_name = context.user_data['user_name']
    phone_number = context.user_data['phone_number']
    status = context.user_data['status']
    description = context.user_data['description']
    photo1 = context.user_data['photo_json1_string']
    photo2 = context.user_data['photo_json2_string']
    photo3 = context.user_data['photo_json3_string']
    photo_file1 =context.user_data['photo_file1']
    photo_file2 =context.user_data['photo_file2']
    
    
    database.insert(product_type, price, user_name, phone_number, status, description,photo1,photo2,photo3)
    
    message_text = f'Product Type: {product_type}\nPrice: {price}\nSeller: {user_name}\nPhone Number: {phone_number}\nStatus: {status}\nDescription: {description}'
    photos = [InputMediaPhoto(photo.file_id) for photo in [photo_file1, photo_file2, photo_file3]]

    await bot.send_message(chat_id='@Addis_Market_channel', text=message_text)
    await bot.send_media_group(chat_id='@Addis_Market_channel', media=photos)
    await update.message.reply_text(f'Your product has successfully been add to our database.\nYou can share the link of your product by going to https://t.me/Addis_Market_channel and coping the post link')
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    await update.message.reply_text('Conversation cancelled')
    return ConversationHandler.END

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

#product_idd = database.get_last_row_id()
#product_url = f"https://t.me/beta_market_bot/{product_id}"
def main()-> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    #application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    conv_handler_1 = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        aNSWER: [MessageHandler(filters.TEXT, ANSWER)],
        aNSWER2: [MessageHandler(filters.TEXT, ANSWER2)],
        aNSWER3: [MessageHandler(filters.TEXT, ANSWER3)],
        aNSWER4: [MessageHandler(filters.TEXT, ANSWER4)],
        aNSWER5: [MessageHandler(filters.TEXT, ANSWER5)],
        aNSWER6: [MessageHandler(filters.TEXT, ANSWER6)],
        aNSWER7: [MessageHandler(filters.PHOTO, ANSWER7)],
        aNSWER8: [MessageHandler(filters.PHOTO, ANSWER8)],
        aNSWER9: [MessageHandler(filters.PHOTO, ANSWER9)],
        
    },
    fallbacks=[CommandHandler('cancel', cancel)],

)
    application.add_handler(conv_handler_1)
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

    #app.run_polling(poll_interval=5)
