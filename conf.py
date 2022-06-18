import telebot
import os
import json

HTTP_API = "5486335698:AAGGCNfpkDknsb2ZtTwcpV3J8Oe4MDGvWq4"
ADMINS = ["LORD_GL", "Spanda82"]
bot = telebot.TeleBot(HTTP_API)
main_keyboard = telebot.types.ReplyKeyboardMarkup(True)
main_keyboard.row('Обновить')

def read_usernames():
    cwd = os.getcwd()
    fileD = open(cwd + '\\usernames.json', 'r') # + '\\main\\'
    data = json.load(fileD)
    fileD.close()
    return data['data']

USERNAME_LIST = read_usernames()
THREAD_COUNT = 50
UPDATING_TIME = 10

pairs = [
        ############# USDT ##############       ############# USDC ##############
        ["ETH", "USDT"], ["BTC", "USDT"],       ["BTC", "USDC"], ["ETH", "USDC"],
        ["USDC", "USDT"], ["BNB", "USDT"],      ["TRX", "USDC"],
        ["ADA", "USDT"], ["XRP", "USDT"],       ["USDD", "USDC"], ["XBT", "USDC"],
        ["BUSD", "USDT"], ["SOL", "USDT"],      ["ADA", "USDC"], ["BNB", "USDC"],
        ["DOT", "USDT"], ["DOGE", "USDT"],      ["SOL", "USDC"], ["DAI", "USDC"],

        ["DAI", "USDT"], ["WBTC", "USDT"],      ["WIN", "USDC"], ["LINK", "USDC"],
        ["TRX", "USDT"], ["LEO", "USDT"],       ["LTC", "USDC"],
        ["AVAX", "USDT"], ["SHIB", "USDT"],     ["APE", "USDC"], ["EOS", "USDC"],
        ["MATIC", "USDT"], ["FTT", "USDT"],     ["DOT", "USDC"], ["ATOM", "USDC"],
        ["LTC", "USDT"], ["CRO", "USDT"],       ["AVAX", "USDC"], ["ALGO", "USDC"], 
]