#install requests
import io
from datetime import datetime
import logging
import json
import requests
from telegram import Bot,InputFile
from typing import Final
import database
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,ConversationHandler,MessageHandler,filters,CallbackContext

TOKEN: Final = '6342676141:AAGP1LeG5aLkFaXTHOwPFaFtLtf1wCk4ZaQ'
BOt_USERNAME : Final = '@Addis_market_bot'
bot = Bot(TOKEN)
print('Starting up bot...')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



aNSWER_1, aNSWER_2, aNSWER_3, aNSWER_4, aNSWER_5= range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "🎉 **Welcome to Addis Market!** 🎉\n"
    "እንኳን ወደ አዲስ ገበያ በደህና መጡ\n\n"
    "🛍️ This is the bot where you can buy products other people post.\n"
    "ይህ ሌሎች ሰዎች የሚለጥፉትን ምርቶችን የሚገዙበት ቦታ ነው.\n\n"
    "📦 If you are looking to sell products, go to @beta_market_bot\n"
    "📦 ምርቶችን ለመሸጥ ከፈለጉ, @beta_market_bot ይጎብኙ\n\n\n"
    "🔍 Add the type of product you want to buy.\nFor example: phone, house, shoes, laptop, car.\n\n"
    "🔍 ለመግዛት የሚፈልጉት የምርት አይነት አስገቡ.\n"
    "ለምሳሌ ፡- ስልክ፣ ቤት ፣ ጫማ፣ ላፕቶፕ ፣ መኪና"
)    
    return aNSWER_1

async def ANSWER_1(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    product_type_supply = update.message.text.lower()
    if product_type_supply =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        context.user_data['product_type_supply'] = product_type_supply
        await update.message.reply_text(f'💰 Add the maximum price for your product in birrs.\nExample:- 550, 2000, 1000000.\n please make sure you input only a number do not include birr\n\n '
                                        f'💰 ምርቱ ከምንያሂል ዋጋ ማነስ እንዳላበት በብር ያስገቡ።\nለምሳሌ፡- 550, 2000, 1000000.\n እባክዎን ቁጥር ብቻ ማስገባትዎን ያረጋግጡ ብር የምለዊን ቃል አያካትቱ.')
    return aNSWER_2

async def ANSWER_2(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    if update.message.text.lower() == '/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        try:
            max_price= float(update.message.text)
            context.user_data['max_price'] = max_price
        except ValueError:
            await update.message.reply_text(f'⚠️Invalid response. Please enter a number.\n💰Add the maximum price for your product in birrs.\nExample:- 550, 2000, 1000000.\n please make sure you input only a number do not include birr\n\n '
                                            f'⚠️ምርቱ ከምንያሂል ዋጋ ማነስ እንዳላበት በብር ያስገቡ።\nለምሳሌ፡- 550, 2000, 1000000.\n💰 እባክዎን ቁጥር ብቻ ማስገባትዎን ያረጋግጡ ብር የምለዊን ቃል አያካትቱ.')
            return aNSWER_2
    await update.message.reply_text(f'💰Add the minimum price for your product in birrs.\nExample:- 450, 2000, 1000000.\n please make sure you input only a number do not include birr\n\n'
                                        f'💰ምርቱ ከምንያሂል ዋጋ መቡለት እንዳላበት በብር ያስገቡ።\nለምሳሌ፡- 450, 2000, 1000000.\n እባክዎን ቁጥር ብቻ ማስገባትዎን ያረጋግጡ ብር የምለዊን ቃል አያካትቱ.')
    return aNSWER_3

async def ANSWER_3(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    if update.message.text.lower() == '/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        try:
            min_price = float(update.message.text)
            context.user_data['min_price'] = min_price
        except ValueError:
            await update.message.reply_text(f'⚠️Invalid response. Please enter a number.\n💰Add the minimum price for your product in birrs.\nExample:- 450, 2000, 1000000.\n please make sure you input only a number do not include birr\n\n'
                                            f'⚠️ልክ ያልሆነ ምላሽ ነው ይስገቡት እባክዎን ቁጥር ይስገባ።\n💰ምርቱ ከምንያሂል ዋጋ መቡለት እንዳላበት በብር ያስገቡ።\nለምሳሌ፡- 450, 2000, 1000000.\n እባክዎን ቁጥር ብቻ ማስገባትዎን ያረጋግጡ ብር የምለዊን ቃል አያካትቱ.')
            return aNSWER_3
    await update.message.reply_text(f'🔵Please input only one of this 3 states of you want for your product.\nStates:- brand new, slightly used, used\n\n'
                                    f'🔵ለምርትዎ ከሚፈልጉት 3 ይዘቶች ውስጥ አንዱን ብቻ ያስገቡ።\nይዘቶች- አዲስ፣ ትንሽ ጥቅም ላይ የዋለ፣ ጥቅም ላይ የዋለ')
    return aNSWER_4

async def ANSWER_4(update: Update,context: ContextTypes.DEFAULT_TYPE)-> int:
    status_supply = update.message.text.lower()
    if status_supply =='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        status_supply = update.message.text.lower()
        context.user_data['status_supply'] = status_supply
        await update.message.reply_text(f'📝 Add a description of the product.\nThis can include the specific model of the product.\nExample:- iphone 8 , nike ,adidas, specific laptop type.\n\n'
                                        f'📝 የምርቱን መግለጫ ያክሉ።\nይህ የምርቱን ልዩ ሞዴል ሊያካትት ይችላል።\nለምሳሌ፡- iphone 8፣ nike፣adidas።')
    
    return aNSWER_5
    
async def ANSWER_5(update: Update, context: ContextTypes.DEFAULT_TYPE)-> int:
    description_supply = update.message.text.lower()
    if description_supply=='/cancel':
        await update.message.reply_text('Conversation cancelled')
        return ConversationHandler.END
    else:
        context.user_data['description_supply'] = description_supply
        user_name = update.message.from_user.username
        context.user_data['user_name'] = user_name
        current_date = datetime.now()
        date = current_date.strftime('%m-%d-%Y')
        context.user_data['date'] = date
    
    
        product_type_supply = context.user_data['product_type_supply']
        max_price = context.user_data['max_price']
        min_price = context.user_data['min_price']  
        status_supply = context.user_data['status_supply']
        description_supply = context.user_data['description_supply']
        user_name = '@'+context.user_data['user_name']
        date = context.user_data['date']
    
        database.insert_supply(product_type_supply,max_price,min_price,status_supply,description_supply,user_name,date)
    
        records = database.query(product_type_supply,max_price,min_price,status_supply,description_supply )
        if len(records)==0:
            await update.message.reply_text(f'sorry there are no items with your specific needs.\n type /start again then try changing your price range\n\n'
                                            f'ይቅርታ ከፍላጎቶችህ ጋር ምንም አይነት እቃዎች አልተገኘም.\n እንደገና /start ብለው ይጀምር ከዛ የዋጋ ክልሎን ለመቀየር ይሞክሩ')
        else:
            for record in records:
                if record[7] != None:
                    photo_json1_string= record[7]
                    photo_json1_dict = json.loads(photo_json1_string)
                    url1= photo_json1_dict['file_path']
                    response = requests.get(url1)
                    photo1 = InputFile(io.BytesIO(response.content), filename='file_1.jpg')
                
                if record[8] != None:
                    photo_json2_string =record[8]
                    photo_json2_dict = json.loads(photo_json1_string)
                    url2 = photo_json2_dict['file_path']
                    response = requests.get(url2)
                    photo2 = InputFile(io.BytesIO(response.content), filename='file_2.jpg')
                if record[9] != None:
                    photo_json3_string= record[9]
                    photo_json3_dict = json.loads(photo_json3_string)
                    url3= photo_json3_dict['file_path']
                    response = requests.get(url3)
                    photo3 = InputFile(io.BytesIO(response.content), filename='file_3.jpg')
                await update.message.reply_text(f'Product type ={record[1]}\nPrice = {record[2]}birrs\nSellers telegram username = {record[3]}\nPhone number = {record[4]}\nProduct status = {record[5]}\nProduct Description = {record[6]}')
                if record[7] != None:
                    await bot.send_photo(chat_id=update.message.chat_id, photo=photo1)
                if record[8] != None:
                    await bot.send_photo(chat_id=update.message.chat_id, photo=photo2)
                if record[9] != None:
                    await bot.send_photo(chat_id=update.message.chat_id, photo=photo3)
    await update.message.reply_text(f'See you soon.\nIf you have an feedback on how we can improve tell us on our channel at https://t.me/Addis_Market_channel \nand our group at https://t.me/Addis_Market_Group')
    return ConversationHandler.END

async def cancel(update, context):
    await update.message.reply_text('Conversation cancelled')
    return ConversationHandler.END

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main()-> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    #application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    conv_handler_2 = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        aNSWER_1: [MessageHandler(filters.TEXT, ANSWER_1)],
        aNSWER_2: [MessageHandler(filters.TEXT, ANSWER_2)],
        aNSWER_3: [MessageHandler(filters.TEXT, ANSWER_3)],
        aNSWER_4: [MessageHandler(filters.TEXT, ANSWER_4)],
        aNSWER_5: [MessageHandler(filters.TEXT, ANSWER_5)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],

)
    application.add_handler(conv_handler_2)
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

    #app.run_polling(poll_interval=5)
