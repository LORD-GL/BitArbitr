from conf import *
from time import time, gmtime, strftime
from threading import Thread
from queue import Queue
import bot_funcs as func

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
    bot.send_message(id, "Пожалуйста подождите, мы получаем данные с бирж...\n(Это может занять некоторое время)")
    list_data = []

    start_time = time()

    queue = Queue()
    result_queue = Queue()
    trash_queue = Queue()

    for i in pairs:
        queue.put(i)

    for i in range(THREAD_COUNT):
        thread = Thread(target=func.run, args=(queue, result_queue, trash_queue))
        thread.daemon = True
        thread.start()

    queue.join()

    while not result_queue.empty():
        data = result_queue.get_nowait()
        list_data.append(data)
    
    for _ in range(len(list_data)-1):
        for i in range(len(list_data)-1):
            if list_data[i]['dif_percent'] < list_data[i+1]['dif_percent']:
                list_data[i], list_data[i+1] = list_data[i+1], list_data[i]

    for i in range(len(list_data)):
        func.print_min_max_data(list_data[i], list_data[i]['cur'], id, bot)


    print(f"Working time with {THREAD_COUNT} treads and {len(pairs)} pairs is {time() - start_time}")

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

bot.polling(none_stop=True, interval=0)
