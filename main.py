from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
def get_url():
    contents = requests.get('https://arugaz.herokuapp.com/api/nekonime').json()
    url = contents['result']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",result).group(1).lower()
    return url
def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=result)
def main():
    updater = Updater('1811863530:AAFFYY_EqvKapAYf93HiO2j3qD-pGKNHgLg')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
