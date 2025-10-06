import telebot
from telebot import types
from telebot import TeleBot
from config import *

bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, text=welcome_text)

@bot.send_message(commands=['sendtouser'])
def sendtouser_handler(message)
    bot.reply_to(message, "please wait to fully develop its start-up")