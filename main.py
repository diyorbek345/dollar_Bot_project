import telebot
from dollar_sum import purchase_data, cell_data
from bot_token import token


bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Your name is {message.from_user.first_name}')


bot.polling(non_stop=True)