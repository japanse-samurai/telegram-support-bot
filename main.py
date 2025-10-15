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
    
@bot.message_handler(commands=['ban'])
def ban_user_by_admin(message):
    user = message.from_user.id
    if user in admin:
        global get_user_for_ban
        get_user_for_ban = bot.send_message(message.chat.id, "send userid for ban:")
        bot.register_next_step_handler(get_user_for_ban, set_baned, set_baned_m)
    else:
        bot.send_message(message.chat.id, "you dont have promission for this command")
def set_baned(message):
    global set_baned_m
    set_baned_m = bot.send_message(message.chat.id, "banned from bot")
    banned_users.append({get_user_for_ban})
@bot.message_handler(commands=['unban'])
def unban_user_by_admin(message):
    user = message.from_user.id
    if user in admin:
        global get_user_for_unban
        get_user_for_unban = bot.send_message(message.chat.id, "send userid for ban:")
        bot.register_next_step_handler(get_user_for_unban, set_unbaned, set_unbaned_m)
    else:
        bot.send_message(message.chat.id, "you dont have promission for this command")
def set_unbaned(message):
    global set_unbaned_m
    set_unbaned_m = bot.send_message(message.chat.id, "banned from bot")
    banned_users.remove({get_user_for_unban})


@bot.message_handler(commands=['help'])
def say_help_for_all(message):
    bot.send_message(message.chat.id, """welcome to the support bot! her is the commands:
                     
/start for sending message again
admins command:
/ban - to ban a user from bot
/unban - to unban a user from bot""")




bot.infinity_polling(skip_pending=True)