import telebot
import os
import json
import urllib3

urllib3.disable_warnings()

<<<<<<< HEAD
HTTP_API = "5323831907:AAHSZmJmnOAhB8lgJJ5KOfny3WbhgQlAw90"
=======
HTTP_API = "5486335698:AAGGCNfpkDknsb2ZtTwcpV3J8Oe4MDGvWq4"
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
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

        ["DAI", "USDT"], ["WBTC", "USDT"],      ["LINK", "USDC"],
        ["TRX", "USDT"], ["LEO", "USDT"],       ["LTC", "USDC"],
        ["AVAX", "USDT"], ["SHIB", "USDT"],     ["APE", "USDC"], ["EOS", "USDC"],
        ["MATIC", "USDT"], ["FTT", "USDT"],     ["DOT", "USDC"], ["ATOM", "USDC"],
        ["LTC", "USDT"], ["CRO", "USDT"],       ["AVAX", "USDC"], ["ALGO", "USDC"],

        ["LINK", "USDT"], ["XLM", "USDT"],      ["MATIC", "USDC"], ["XCN", "USDC"],
        ["UNI", "USDT"], ["XMR", "USDT"],       ["FTM", "USDC"], ["LUNC", "USDC"],
        ["BCH", "USDT"], ["NEAR", "USDT"],      ["BAT", "USDC"], ["KDA", "USDC"],
        ["ALGO", "USDT"], ["ETC", "USDT"],      ["MANA", "USDC"], ["BCH", "USDC"],
        ["ATOM", "USDT"], ["GMT", "USDT"],      ["SHIB", "USDC"], ["NEAR", "USDC"],

        ["GST", "USDT"], ["VET", "USDT"],       ["RUNE", "USDC"], ["VRA", "USDC"],
        ["FLOW", "USDT"], ["MANA", "USDT"],     ["DOGE", "USDC"], ["GMT", "USDC"],
        ["HBAR", "USDT"], ["XTZ", "USDT"],      ["LUNA", "USDC"],
        ["ICP", "USDT"], ["TUSD", "USDT"],      ["ZEC", "USDC"], ["ZIL", "USDC"],
        ["FIL", "USDT"], ["THETA", "USDT"],     ["OP", "USDC"], ["SAND", "USDC"],
                                                ############# DAI ################
        ["SAND", "USDT"], ["APE", "USDT"],      ["BTC", "DAI"], 
        ["HNT", "USDT"], ["VRA", "USDT"],       ["ETH", "DAI"], 
        ["EGLD", "USDT"], ["EOS", "USDT"],      ["XBT", "DAI"], 
        ["HT", "USDT"], ["BSV", "USDT"],        
        ["AXS", "USDT"], ["AAVE", "USDT"],     

        ["GALA", "USDT"], ["MKR", "USDT"],      
        ["GRT", "USDT"], ["XEC", "USDT"],       
        ["IOTA", "USDT"], ["KLAY", "USDT"],     
        ["NEO", "USDT"], ["OKB", "USDT"],       
        ["RUNE", "USDT"], ["PAXG", "USDT"],     

        ["QNT", "USDT"], ["CHZ", "USDT"],       
        ["WAVES", "USDT"], ["LRC", "USDT"],     
        ["CAKE", "USDT"], ["STX", "USDT"],      
        ["DASH", "USDT"], ["NEXO", "USDT"],     
        ["ZIL", "USDT"], ["BAT", "USDT"],

        ["CELO", "USDT"], ["BORA", "USDT"],
        ["ENJ", "USDT"], ["XDC", "USDT"],
        ["CRV", "USDT"], ["DCR", "USDT"],
        ["HOT", "USDT"], ["MINA", "USDT"],
        ["XEM", "USDT"], ["KAVA", "USDT"], 

        ["GT", "USDT"], ["ONE", "USDT"],
        ["GNO", "USDT"], ["1INCH", "USDT"],
        ["KDA", "USDT"], ["AR", "USDT"],
        ["QTUM", "USDT"], ["XYM", "USDT"],
        ["BTG", "USDT"], ["GLMR", "USDT"],

        ["OMG", "USDT"], ["ROSE", "USDT"],
        ["CVX", "USDT"], ["IOST", "USDT"],
        ["COMP", "USDT"], ["IOTX", "USDT"],
        ["KNC", "USDT"], ["SRM", "USDT"],
        ["ICX", "USDT"], ["TFUEL", "USDT"],    
]