from core import binance_core as binance, bybit_core as bybit
from core import kucoin_core as kucoin, huobi_core as huobi
# from core import exmo_core as exmo 
# from core import coinbase_core as coinbase ERROR AttributeError: module 'collections' has no attribute 'MutableMapping'
from core import okex_core as okx, kraken_core as kraken
from core import phemex_core as phemex, gateio_core as gateio # НЕПОНЯТНАЯ ОШИБКА
from core import aex_core as aex #hoo_core as hoo,  # woo_core as woo
from core import lbank_core as lbank, bitfinex_core as bitfinex # ONLY USDT
# import poloniex_core as poloniex
# from core import genimi_core as genimi
from core import mexc_core as mexc, crypto_core as crypto
#from core import aex_core as aex

from conf import *
from time import gmtime, strftime, time, sleep

from threading import Thread
from queue import Queue

def check_error(price):
    if price == -1:
        return " no data"
    else: return price

def count_dif_percent(bigger, smaller):
    try:
        return round(float((bigger-smaller)/bigger*100),2)
    except ZeroDivisionError:
        return 0

def find_min_max_price(pair_dict):
    max_price, min_price = -1, 10000000000
    ex_min, ex_max = "", ""
    dif = 0

    for ex in pair_dict:
        if ex != 'cur':
            if pair_dict[ex] > max_price: 
                max_price = pair_dict[ex]
                ex_max = ex
            if pair_dict[ex] < min_price and pair_dict[ex] != -1:
                min_price = pair_dict[ex]
                ex_min = ex
    
    dif = count_dif_percent(max_price, min_price)
    Exc = False
    if dif < 1 or dif > 70:
        Exc = True

    return {
    "max" : {"exchanger" : ex_max, "price" : max_price},
    "min" : {"exchanger" : ex_min, "price" : min_price},
    "dif_percent" : dif,
    "cur" : pair_dict['cur'],
    "Exception" : Exc
    }

def make_dict_ex_price(pair): # update or inf
    ex_price = {}
    ex_vol = {}
    mes = ""

    ex_price['cur'] = pair
    ex_vol['cur'] = pair

    ex_price['Bybit'], ex_vol['Bybit'] = bybit.get_price(symbol="".join(pair)) #ETHUSDT, 11111
    ex_price['Binance'], ex_vol['Binance'] = binance.get_price(symbol="".join(pair)) 
    ex_price['Kucoin'], ex_vol['Kucoin'] = kucoin.get_price(symbol="-".join(pair))
    ex_price['Huobi'], ex_vol['Huobi'] = huobi.get_price(symbol="".join(pair).lower())
    #ex_price['Coinbase'], ex_vol['Coinbase'] = coinbase.get_price(symbol="-".join(pair))
    ex_price['OKEX'], ex_vol['OKEX'] = okx.get_price(symbol="-".join(pair))
    ex_price['Kraken'], ex_vol['Kraken'] = kraken.get_price(symbol="".join(pair))
    ex_price['Phemex'], ex_vol['Phemex'] = phemex.get_price(symbol="".join(pair))
    ex_price['Gate.io'], ex_vol['Gate.io'] = gateio.get_price(symbol="_".join(pair))
    ex_price['LBank'], ex_vol['LBank'] = lbank.get_price(symbol="_".join(pair).lower())
    ex_price['Bitfinex'], ex_vol['Bitfinex'] = bitfinex.get_price(pair[0].lower(), pair[1].lower())
    #ex_price['Genimi'], ex_vol['Genimi'] = genimi.get_price(pair[0].lower(), pair[1].lower()) # NONE
    ex_price['MEXC'], ex_vol['MEXC'] = mexc.get_price(symbol="".join(pair))
    ex_price['Crypto.com'], ex_vol['Crypto.com'] = crypto.get_price(symbol="_".join(pair))
    #ex_price['Hoo'], ex_vol['Hoo'] = hoo.get_price(symbol="-".join(pair))
    # ex_price['AEX'], ex_vol['AEX'] = ftx.get_price(pair[0], pair[1])

    mes += "(Bybit)         | " + str(check_error(ex_price.get("Bybit"))) + f" | Vol: {check_error(ex_vol['Bybit'])}\n"
    mes += "(Binance)    | " + str(check_error(ex_price.get("Binance"))) + f" | Vol: {check_error(ex_vol['Binance'])}\n"
    mes += "(Kucoin)      | " + str(check_error(ex_price.get("Kucoin"))) + f" | Vol: {check_error(ex_vol['Kucoin'])}\n"
    mes += "(Huobi)       | " + str(check_error(ex_price.get("Huobi"))) + f" | Vol: {check_error(ex_vol['Huobi'])}\n"
    #mes += "(Coinbase) | " + str(check_error(ex_price.get("Coinbase"))) + f" | Vol: {check_error(ex_vol['Coinbase'])}\n"
    mes += "(OKEX)        | " + str(check_error(ex_price.get("OKEX"))) + f" | Vol: {check_error(ex_vol['OKEX'])}\n"
    mes += "(Kraken)     | " + str(check_error(ex_price.get("Kraken"))) + f" | Vol: {check_error(ex_vol['Kraken'])}\n"
    mes += "(Phemex)   | " + str(check_error(ex_price.get("Phemex"))) + f" | Vol: {check_error(ex_vol['Phemex'])}\n"
    mes += "(Gate.io)     | " + str(check_error(ex_price.get("Gate.io"))) + f" | Vol: {check_error(ex_vol['Gate.io'])}\n"
    mes += "(LBank)       | " + str(check_error(ex_price.get("LBank"))) + f" | Vol: {check_error(ex_vol['LBank'])}\n"
    mes += "(Bitfinex)    | " + str(check_error(ex_price.get("Bitfinex"))) + f" | Vol: {check_error(ex_vol['Bitfinex'])}\n"
    #mes += "(Gemini)     | " + str(check_error(ex_price.get("Genimi"))) + f" | Vol: {check_error(ex_vol['Genimi'])}\n"
    mes += "(MEXC)        | " + str(check_error(ex_price.get("MEXC"))) + f" | Vol: {check_error(ex_vol['MEXC'])}\n"
    mes += "(Crypto.com)| " + str(check_error(ex_price.get("Crypto.com"))) + f" | Vol: {check_error(ex_vol['Crypto.com'])}\n"
    #mes += "(Hoo)            | " + str(check_error(ex_price.get("Hoo"))) + f" | Vol: {check_error(ex_vol['Hoo'])}\n"
    #mes += "(AEX)            | " + str(check_error(ex_price.get("AEX"))) + f" | Vol: {check_error(ex_vol['AEX'])}\n"

    return ex_price, mes

def print_min_max_data(data, curr, id, bot, msg_id=0, iter=0):
    mes = ""
    mes += f"{'/'.join(curr)}:\n"
    mes += f"Max price: {data['max']['price']} | {data['max']['exchanger']}\n"
    mes += f"Min price: {data['min']['price']} | {data['min']['exchanger']}\n"
    #mes += f"Difference: {count_dif_percent(min_max['max']['price'], min_max['min']['price'])}\n"
    mes += f"Spread: {data['dif_percent']}%\n"
    if iter:
        mes += f"\n(Повторение: {iter}) | Данные обновятся {UPDATING_TIME} раз"
        bot.edit_message_text(chat_id = id, text = mes, message_id = msg_id)
    else:
        bot.send_message(id, mes)

def run(queue, result_queue, trash_queue):
    while not queue.empty():
        element = queue.get_nowait()
        pair, mes = make_dict_ex_price(element)
        data = find_min_max_price(pair)
        if not data['Exception']:
            result_queue.put_nowait(data)
        else:
            trash_queue.put_nowait(data)
        queue.task_done()

def check_admin(message):
    if 'admin' in message.text:
        print(f"USER: {message.from_user.username}  made ADMIN request! at", end = " | ")
        print(strftime('%d %b %Y %H:%M:%S (+0)', gmtime()))
        return True
    else:
        return False

def private(func):
    def wrapper(*args, **kwargs):
        print("USER:", args[0].from_user.username, f" made request with text: \"{args[0].text}\"", end=" | ")
        print(strftime('%d %b %Y %H:%M:%S (+0)', gmtime()))
        if args[0].from_user.username in USERNAME_LIST:
            func(*args, **kwargs)
        else:
            print(f"Access refused for {args[0].from_user.username}", end = " | ")
            print(strftime('%d %b %Y %H:%M:%S (+0)', gmtime()))
            bot.send_message(args[0].chat.id, "Это приватный бот!\n(Купите АБОНЕМЕНТ для доступа или получити БЕСПЛАТНЫЙ пробный период, подробности на канале: https://t.me/bitarbitr)")
    return wrapper

def admin_add_user(username, id):
    if username not in USERNAME_LIST:
        cwd = os.getcwd()
        fileD = open(cwd + '\\usernames.json', 'w') # '\\main\\' + 
        USERNAME_LIST.append(username)
        json_list = json.dumps({"data" : USERNAME_LIST})
        fileD.write(json_list)
        fileD.close()
        bot.send_message(id, f"User {username} was successfully added!")
    else:
        bot.send_message(id, f"User {username} ALREADY in the list")

def admin_userslist(id):
    mes = "List of users:\n"
    for i in USERNAME_LIST:
        mes += "Username: @" + i + "\n"
    bot.send_message(id, mes)

def admin_getinfo(username, id):
    if username in USERNAME_LIST:
        bot.send_message(id, f"User {username} have access to the bot")
    else:
        bot.send_message(id, f"There is no user with {username} username")

def admin_delete_user(username, id):
    if username in USERNAME_LIST:
        cwd = os.getcwd()
        fileD = open(cwd + '\\usernames.json', 'w') # '\\main\\' + 
        USERNAME_LIST.remove(username)
        json_list = json.dumps({"data" : USERNAME_LIST})
        fileD.write(json_list)
        fileD.close()
        bot.send_message(id, f"User {username} was successfully deleted!")
    else:
        bot.send_message(id, f"There is no user with {username} username. Sorry, i can't delete him")

def load_min_max_data(data, curr, id, bot, msg_id=0, iter=0):
    mes = ""
    mes += f"{'/'.join(curr)}:\n"
    mes += f"Max price: {data['max']['price']} | {data['max']['exchanger']}\n"
    mes += f"Min price: {data['min']['price']} | {data['min']['exchanger']}\n"
    #mes += f"Difference: {count_dif_percent(min_max['max']['price'], min_max['min']['price'])}\n"
    mes += f"Spread: {data['dif_percent']}%\n"
    mes += "@@@@@@@"
    return mes

def update_iterator(id, bot):
    while True:
        list_data = []
        start_time = time()
        queue = Queue()
        result_queue = Queue()
        trash_queue = Queue()
        data_to_load = ""

        for i in pairs:
            queue.put(i)

        for i in range(THREAD_COUNT):
            thread = Thread(target=run, args=(queue, result_queue, trash_queue))
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
            #print_min_max_data(list_data[i], list_data[i]['cur'], id, bot)
            data_to_load += load_min_max_data(list_data[i], list_data[i]['cur'], id, bot)
 
        cwd = os.getcwd()
        fileD = open(cwd + '\\data.txt', 'w') # '\\main\\' +
        fileD.write("")
        fileD.write(data_to_load)
        fileD.close()
        print(f"Updated with {time()-start_time} seconds")
