import telebot
from telebot import TeleBot
from config import *

bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        bot.send_message(message.chat.id, "you_banned_by_admins")
    else:
        global message_one
        message_one = bot.send_message(message.chat.id, text=welcome_text)
        bot.register_next_step_handler(message_one, send_to_chanel_def, sendchanel, send_confrim)

def send_to_chanel_def(message):
    user_id = message.from_user.id
    global sendchanel
    sendchanel = bot.send_message(chanel_of_messages, """new message:
    {message_one} from {user_id}""")
    global send_confrim
    send_confrim = bot.send_message(message.chat.id, "your message sended for admins")


@bot.message_handler(commands=['send_user'])
def send_to_user(message):
    user_id = message.from_user.id
    if user_id in admin:
        global get_user_to_send
        get_user_to_send = bot.send_message(message.chat.id, "send the user_id to send message to user you selected")
        bot.register_next_step_handler(get_user_to_send,sendmessagetouserdef, getmessagefromadmin, sendtouserthetext, sendconfrimtoadmin)
def sendmessagetouserdef(message):
    global getmessagefromadmin
    getmessagefromadmin = bot.send_message(message.chat.id, "send your message to user")
    global sendtouserthetext
    sendtouserthetext = bot.send_message(get_user_to_send, "you have new message from admins: {getmessagefromadmin}")
    global sendconfrimtoadmin
    sendconfrimtoadmin = bot.send_message(message.chat.id, "sended")

       
bot.infinity_polling(skip_pending=True)