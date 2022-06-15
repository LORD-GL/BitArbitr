from core import binance_core as binance, bybit_core as bybit
from core import kucoin_core as kucoin, huobi_core as huobi
# from core import exmo_core as exmo 
from core import coinbase_core as coinbase, ftx_core as ftx
from core import okex_core as okx, kraken_core as kraken
from core import phemex_core as phemex, gateio_core as gateio # НЕПОНЯТНАЯ ОШИБКА
#import hoo_core as hoo NOT DONE
from core import lbank_core as lbank, bitfinex_core as bitfinex # ONLY USDT
# import poloniex_core as poloniex

from conf import *
from time import gmtime, strftime


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
    if dif < 1:
        Exc = True

    return {
    "max" : {"exchanger" : ex_max, "price" : max_price},
    "min" : {"exchanger" : ex_min, "price" : min_price},
    "dif_percent" : dif,
    "cur" : pair_dict['cur'],
    "Exception" : Exc
    }

def make_dict_ex_price(pair):
    ex_price = {}
    mes = ""

    ex_price['cur'] = pair

    ex_price['Bybit'] = bybit.get_price(symbol="".join(pair)) #ETHUSDT
    mes = "(Bybit)         | " + "/".join(pair) + ': ' + str(check_error(ex_price.get("Bybit"))) + "\n"

    ex_price['Binance'] = binance.get_price(symbol="".join(pair)) 
    mes += "(Binance)    | " + "/".join(pair) + ': ' + str(check_error(ex_price.get("Binance"))) + "\n"

    ex_price['Kucoin'] = kucoin.get_price(symbol="-".join(pair))
    mes += "(Kucoin)      | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Kucoin"))) + "\n"

    ex_price['Huobi'] = huobi.get_price(symbol="".join(pair).lower())
    mes += "(Huobi)       | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Huobi"))) + "\n"

    # ex_price['Exmo'] = exmo.get_price(symbol="_".join(pair)) НЕТ ОБЪЕМОВ
    # mes += "(Exmo) " + "/".join(pair) + ": " + str(ex_price.get("Exmo")) + "\n"

    ex_price['Coinbase'] = coinbase.get_price(symbol="-".join(pair))
    mes += "(Coinbase) | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Coinbase"))) + "\n"

    ex_price['FTX'] = ftx.get_price(pair[0], pair[1])
    mes += "(FTX)            | " + "/".join(pair) + ": " + str(check_error(ex_price.get("FTX"))) + "\n"

    ex_price['OKEX'] = okx.get_price(symbol="-".join(pair))
    mes += "(OKEX)        | " + "/".join(pair) + ": " + str(check_error(ex_price.get("OKEX"))) + "\n"

    ex_price['Kraken'] = kraken.get_price(symbol="".join(pair))
    mes += "(Kraken)     | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Kraken"))) + "\n"

    ex_price['Phemex'] = phemex.get_price(symbol="".join(pair))
    mes += "(Phemex)   | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Phemex"))) + "\n"

    ex_price['Gate.io'] = gateio.get_price(symbol="_".join(pair))
    mes += "(Gate.io)     | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Gate.io"))) + "\n"

    ex_price['LBank'] = lbank.get_price(symbol="_".join(pair).lower())
    mes += "(LBank)       | " + "/".join(pair) + ": " + str(check_error(ex_price.get("LBank"))) + "\n"

    ex_price['Bitfinex'] = bitfinex.get_price(pair[0], pair[1])
    mes += "(Bitfinex)    | " + "/".join(pair) + ": " + str(check_error(ex_price.get("Bitfinex"))) + "\n"

    # ex_price['Poloniex'] = poloniex.get_price(pair[0], pair[1])
    # mes += "(Poloniex) " + "/".join(pair) + ": " + str(ex_price.get("Poloniex")) + "\n"

    return ex_price, mes

def print_min_max_data(data, curr, id, bot, msg_id=0, iter=0):
    mes = ""
    mes += f"{'/'.join(curr)}:\n"
    mes += f"Максимальная цена: {data['max']['price']} | Биржа: {data['max']['exchanger']}\n"
    mes += f"Минимальная цена: {data['min']['price']} | Биржа: {data['min']['exchanger']}\n"
    #mes += f"Difference: {count_dif_percent(min_max['max']['price'], min_max['min']['price'])}\n"
    mes += f"Максимальная Разница: {data['dif_percent']}%\n"
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
            bot.send_message(args[0].chat.id, "Sorry, It's private bot, buy an access to use it! \n(Купите АБОНЕМЕНТ для доступа)")
    return wrapper

def admin_add_user(username, id):
    if username not in USERNAME_LIST:
        cwd = os.getcwd()
        fileD = open(cwd + '/usernames.json', 'w') # '\\main\\' + 
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
        fileD = open(cwd + '/usernames.json', 'w') # '\\main\\' + 
        USERNAME_LIST.remove(username)
        json_list = json.dumps({"data" : USERNAME_LIST})
        fileD.write(json_list)
        fileD.close()
        bot.send_message(id, f"User {username} was successfully deleted!")
    else:
        bot.send_message(id, f"There is no user with {username} username. Sorry, i can't delete him")

