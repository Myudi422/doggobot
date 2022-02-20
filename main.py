from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re
from telegram import (ParseMode, Update, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, 
                      KeyboardButton)

def get_url():
    contents = requests.get('https://arugaz.herokuapp.com/api/nekonime').json()
    url = contents['result']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    msg = update.effective_message
    url = get_image_url()
    context.bot.send_photo(chat_id=chat_id, photo=url)
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]

    

def main():
    updater = Updater('1811863530:AAFFYY_EqvKapAYf93HiO2j3qD-pGKNHgLg', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
