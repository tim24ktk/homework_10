import telebot
from telebot import types
from currency_model import get_currency


bot = telebot.TeleBot('5675523285:AAGGDUDJMp3RkPoXlzQl9tBv3QmO2G7sWT8')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.username}')
    bot.send_message(message.chat.id, f'Введите буквенный код валюты, которую хотите узнать!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, get_currency(message.text))


bot.infinity_polling()


