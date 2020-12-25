import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1354323195:AAGRfCBUHOkgZ0ymJ7Jkx_PYGeJ2tbYzyqU'
    bot_chatID = '1365735229'
    send_text = 'https://api.telegram.org/bot'+ bot_token+'/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    


