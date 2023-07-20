
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

def get_currency_price():
    url = 'https://nobitex.ir/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_='price').text.strip()
    return price

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to Currency Bot!')

def get_price(update, context):
    price = get_currency_price()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Current currency price: {price}')

def main():
    updater = Updater(token='YOUR_TELEGRAM_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    price_handler = CommandHandler('price', get_price)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(price_handler)

    updater.start_polling()

if name == '__main__':
    main()

