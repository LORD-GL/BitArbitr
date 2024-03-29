from conf import *
from time import time, gmtime, strftime, sleep
from threading import Thread
from queue import Queue

exc = True
while exc:
    try:
        import bot_funcs as func
        print("Connected!")
        exc = False
    except:
        print(f"Connection problems! {strftime('%d %b %Y %H:%M:%S (+0)', gmtime())}")
        sleep(15)
        pass

@bot.message_handler(func = lambda message: message.text == 'Справка')
@bot.message_handler(commands=["start"])
@func.private
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте! Нажмите \"Обновить\", чтобы получить список разниц цен \nВведите пару для того, чтобы узнать цены на разных биржах для неё(Пример: BTC/USDT)\nВведите \"Список пар\" для того, чтобы посмотреть все доступные в боте валюные пары.", reply_markup=main_keyboard)

@bot.message_handler(func = lambda message: message.text == 'Обновить')
@func.private
def update(message):
    id = message.chat.id
    bot.send_message(id, "Мы показываем только пары с разницой > 1%")
    bot.send_message(id, "Пожалуйста подождите, мы получаем данные с бирж...\n(Данные обновляются каждые 30 секунд)")

    cwd = os.getcwd()
    fileD = open(cwd + '\\data.txt', 'r')
    data = fileD.read().split("@@@@@@@")
    fileD.close()
    for i in range(len(data)-1):
        bot.send_message(id, data[i])

# admin method username
@bot.message_handler(func = lambda message: func.check_admin(message) == True)
@func.private
def admin(message):
    inf = "FORM: admin method [username]\nmathod - method to do:\n  add - add new user to access to bot\n   userslist - show all users who have access to bot\n     getinfo - get information about user\n  delete - delete user\nExemple: admin 12345 add me"
    data = message.text.split(" ")
    if len(data) == 1 or data[1] == "info":
        bot.send_message(message.chat.id, inf)
    elif message.from_user.username in ADMINS:
        if len(data) < 2:
            bot.send_message(message.chat.id, "You didn't send any method to do or username")
        elif data[1] == "add" and len(data) == 3:
            func.admin_add_user(data[2], message.chat.id)
        elif data[1] == "userslist":
            func.admin_userslist(message.chat.id)
        elif data[1] == "getinfo" and len(data) == 3:
            func.admin_getinfo(data[2], message.chat.id)
        elif data[1] == "delete" and len(data) == 3:
            func.admin_delete_user(data[2], message.chat.id)
        elif data[1] == "update":
            try:
                func.update_iterator(message.chat.id, bot)
            except:
                print("Updating went wrong, pleas RESTART updating")
        else:
            bot.send_message(message.chat.id, "Sorry, i don't know this method (send: admin info to see more)")
    else:
        print(f"User have tried access to the admin panel with without permission", end = " | ")
        print(strftime('%d %b %Y %H:%M:%S (+0)', gmtime()))
        bot.send_message(message.chat.id, "Permission Error")

@bot.message_handler(func = lambda message: message.text == "Список пар")
@func.private
def pair_list(message):
    mes = "Отсортированный по алфавиту список пар:\n"
    pairs.sort()
    for i in range(1, len(pairs)+1):
        mes += "/".join(pairs[i-1]) + f"({i})\n"
    mes += f"Всего: {len(pairs)}\n"
    bot.send_message(message.chat.id, mes)

@bot.message_handler(content_types=["text"])
@func.private
def pair_info(message):
    id = message.chat.id
    pair_inp = message.text.upper().split("/")
    if pair_inp in pairs:
        exs = bot.send_message(id, "Пожалуйста подождите...")
        dif = bot.send_message(id, "Мы ищим данные для показа...")
        for i in range(1, UPDATING_TIME+1):
            pair, mes = func.make_dict_ex_price(pair_inp)
            bot.edit_message_text(chat_id = id, text = mes + f"\n(Повторение:{i})", message_id = exs.message_id)
            min_max = func.find_min_max_price(pair)
            func.print_min_max_data(min_max, pair_inp, id, bot, dif.message_id, i)
    else:
        bot.send_message(id, f"Я не знаю такой пары:(\nВведите: 'Список пар', чтобы посмотреть список доступных валютных пар или введите 'Справка', чтобы получить полную информацию о пользованнии ботом")

while True:
    try:
       bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print("Connection Error", e)
        print(strftime('%d %b %Y %H:%M:%S (+0)', gmtime()))
        sleep(10)
