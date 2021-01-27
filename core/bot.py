import requests
from core import config


def telegram_bot_sendtext(bot_message):
    
    bot_token = config.bot_token
    bot_chatID = config.bot_chatID
    send_text = 'https://api.telegram.org/bot'+ bot_token+'/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    send = requests.get(send_text)

   
    


