from typing import ItemsView
from telebot import types
import telebot
import sqlite3

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)


# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "*Hello, {0.first_name} 👋*".format(message.from_user, bot.get_me()), reply_markup=remove_keyboard, parse_mode="Markdown")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_schedule = types.KeyboardButton("📰 Schedule")
    keyboard.add(item_schedule)
    bot.send_message(message.chat.id, "*If you are a doctor, then you can view the schedule of your patients here*", parse_mode="Markdown", reply_markup=keyboard)
    # # / nickname
    # global id_from_bot
    # nickname_from_bot = message.from_user.first_name
    # print(f"User nickname: {nickname_from_bot}")
    # # / username
    # global id_from_bot
    # username_from_bot = message.from_user.username
    # print(f"User username: {username_from_bot}")
    # # / id
    # global id_from_bot
    # id_from_bot = message.from_user.id
    # print(f"User id: {id_from_bot}")
    # login_ask(message)


# # ! login_ask
# def login_ask(message):
#     bot.send_message(message.chat.id, "Send me your *login*", parse_mode="Markdown")
#     # goto login_ask_complete
#     bot.register_next_step_handler(message, login_ask_complete)
# def login_ask_complete(message):
#     # / login
#     global login_from_bot
#     login_from_bot = message.text
#     print(f"User login: {login_from_bot}")
#     # goto password_ask
#     password_ask(message)


# # ! password_ask
# def password_ask(message):
#     bot.send_message(message.chat.id, "Send me your *password*", parse_mode="Markdown")
#     # goto password_ask_complete
#     bot.register_next_step_handler(message, password_ask_complete)
# def password_ask_complete(message):
#     # / password
#     global password_from_bot
#     password_from_bot = message.text
#     print(f"User password: {password_from_bot}\n")
#     # goto database
#     database(message)


# # ! database
# def database(message):
#     global db, sql
#     db = sqlite3.connect('server.db')
#     sql = db.cursor()
#     sql.execute('''CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)''')
#     db.commit()

    # sql.execute(f'SELECT login FROM users WHERE login = "{login_from_bot}"')
    # # sql.execute(f'SELECT telegramID FROM users WHERE telegramID = "{id_from_bot}"')
    # if sql.fetchone() is None:
    #     sql.execute(f"INSERT INTO users VALUES (?, ?)", (login_from_bot, password_from_bot))
    #     db.commit()
    #     print("[Registered successfully]\n")
    #     bot.send_message(message.chat.id, "*[Registered successfully]*", parse_mode="Markdown")
    #     signup_complete(message)
    # else:
    #     print("[Such account already exists]\n")
    #     bot.send_message(message.chat.id, "*[Such account already exists]*", parse_mode="Markdown")



    # sql.execute(f'SELECT login FROM users WHERE login = "{login_from_bot}" ')
    # if sql.fetchone() is None:
    #     print("*[No such user]*")
    #     bot.send_message(message.chat.id, "*[Such account already exists]*", parse_mode="Markdown")
    #     login_ask(message)

    # sql.execute(f'SELECT password FROM users WHERE password = "{password_from_bot}" ')
    # if sql.fetchone() is None:
    #     print("*[Wrong password]*")
    #     bot.send_message(message.chat.id, "*[Wrong password]*", parse_mode="Markdown")
    #     login_ask(message)


# # ! signup_complete
# def signup_complete(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item_schedule = types.KeyboardButton("📰 Schedule")
#     keyboard.add(item_schedule)
#     bot.send_message(message.chat.id, "Ok, I got it", parse_mode="Markdown", reply_markup=keyboard)


# ! buttons
@bot.message_handler(content_types=["text"])
def buttons(message):
    # ! ADMIN
    # / remove webhook
    if message.text == "remove_webhook":
        bot.delete_message(message.chat.id, message.message_id)
        bot.remove_webhook()
    # / stop polling
    elif message.text == "stop_polling":
        bot.delete_message(message.chat.id, message.message_id)
        bot.stop_bot()
    # / secret
    elif message.text == "CHOSEN ONES":
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "*CHOSEN ONES ARE THE BEST!*", parse_mode="Markdown")
    # ! schedule
    elif message.text == "📰 Schedule":
            bot.send_message(message.chat.id, "*Schedule of your patients:*", parse_mode="Markdown")
            file = open("apoInfo.txt", "r")
            toRead = file.read()
            print(toRead)
            file.close()
            bot.send_message(message.chat.id, toRead, parse_mode="Markdown")
            # bot.send_message(message.chat.id, "*Name:* fullName, *Date:* date, *Time:* time", parse_mode="Markdown")


# ! polling
bot.infinity_polling()
