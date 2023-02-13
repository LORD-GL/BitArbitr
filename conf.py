import telebot
import os
import json
import urllib3

urllib3.disable_warnings()

HTTP_API = "5323831907:AAHSZmJmnOAhB8lgJJ5KOfny3WbhgQlAw90"
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
UPDATING_TIME = 5

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
        ["UNI", "USDT"], ["XMR", "USDT"],       ["FTM", "USDC"],
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
                                                ############ 
        ["GALA", "USDT"], ["MKR", "USDT"],      ["FEI", "USDT"], ["RVN", "USDT"],
        ["GRT", "USDT"], ["XEC", "USDT"],       ["PEOPLE", "USDT"], ["OP", "USDT"],
        ["IOTA", "USDT"], ["KLAY", "USDT"],     ["FXS", "USDT"], ["LDO", "USDT"],
        ["NEO", "USDT"], ["OKB", "USDT"],       ["SGB", "USDT"], ["DAO", "USDT"],
        ["RUNE", "USDT"], ["PAXG", "USDT"],     ["ZRX", "USDT"], ["RLY", "USDT"],

        ["QNT", "USDT"], ["CHZ", "USDT"],       ["ANKR", "USDT"], ["CHR", "USDT"],
        ["WAVES", "USDT"], ["LRC", "USDT"],     ["OSMO", "USDT"], ["SUSHI", "USDT"],
        ["CAKE", "USDT"], ["STX", "USDT"],      ["OMI", "USDT"], ["ENS", "USDT"],
        ["DASH", "USDT"], ["NEXO", "USDT"],     ["SFM", "USDT"], ["GLM", "USDT"],
        ["ZIL", "USDT"], ["BAT", "USDT"],       ["WOO", "USDT"], ["ORBS", "USDT"],

        ["CELO", "USDT"], ["BORA", "USDT"],     ["OKT", "USDT"], ["LPT", "USDT"],
        ["ENJ", "USDT"], ["XDC", "USDT"],       ["TWT", "USDT"], ["YFI", "USDT"],
        ["CRV", "USDT"], ["DCR", "USDT"],       ["OHM", "USDT"], ["DOME", "USDT"],
        ["HOT", "USDT"], ["MINA", "USDT"],      ["POKT", "USDT"], ["RACA", "USDT"],
        ["XEM", "USDT"], ["KAVA", "USDT"],      ["AUDIO", "USDT"], ["FX", "USDT"],

        ["GT", "USDT"], ["ONE", "USDT"],        ["NU", "USDT"], ["SKL", "USDT"],
        ["GNO", "USDT"], ["1INCH", "USDT"],     ["KUB", "USDT"], ["IMX", "USDT"],
        ["KDA", "USDT"], ["AR", "USDT"],        ["JST", "USDT"], ["BAL", "USDT"],
        ["QTUM", "USDT"], ["XYM", "USDT"],      ["ONT", "USDT"], ["UMA", "USDT"],
        ["BTG", "USDT"], ["GLMR", "USDT"],      ["SC", "USDT"], ["STORJ", "USDT"],

        ["OMG", "USDT"], ["ROSE", "USDT"],      ["SXP", "USDT"], ["MX", "USDT"],
        ["CVX", "USDT"], ["IOST", "USDT"],      ["CHSB", "USDT"], ["ASTR", "USDT"],
        ["COMP", "USDT"], ["IOTX", "USDT"],     ["MXC", "USDT"], ["DAG", "USDT"],
        ["KNC", "USDT"], ["SRM", "USDT"],       ["XIDO", "USDT"], ["LOOKS", "USDT"],
        ["ICX", "USDT"], ["TFUEL", "USDT"],     ["WAXP", "USDT"], ["POLY", "USDT"],

        ["SCRT", "USDT"], ["ELON", "USDT"],     ["RNDR", "USDT"], ["ACA", "USDT"],
        ["NFT", "USDT"], ["CUBE", "USDT"],      ["EVER", "USDT"], ["SYN", "USDT"],
        ["RPL", "USDT"], ["LSK", "USDT"],       ["KUNCI", "USDT"], ["CKB", "USDT"],
        ["XCH", "USDT"], ["CSPR", "USDT"],      ["ILV", "USDT"], ["FLUX", "USDT"],

        ["DGB", "USDT"], ["JUNO", "USDT"],      ["VLX", "USDT"], ["XNO", "USDT"],
        ["RSR", "USDT"], ["HIVE", "USDT"],      ["SPELL", "USDT"], ["WIN", "USDT"],
        ["SLP", "USDT"], ["REN", "USDT"],       ["ERG", "USDT"], ["WRX", "USDT"],
        ["PLA", "USDT"], ["BNT", "USDT"],       ["CFX", "USDT"], ["GAL", "USDT"],
        ["DYDX", "USDT"], ["GMX", "USDT"],      ["VGX", "USDT"], ["COTI", "USDT"],
        ###################################### ORDERED
        ["LUNC", "USDT"], ["LUNC", "USDC"],     ["SNT", "ETH"], ["UFT", "USDT"],
        ["FLOKI", "USDT"], ["BABYDOGE", "USDT"],["SNT", "USDT"], ["NMR", "USDT"],
        ["SPS", "USDT"], ["SNT", "BTC"],        ["UFT", "ETH"], ["NMR", "ETH"],
        ["NMR", "BTC"], ["REQ", "USDT"],        ["REQ", "BTC"], ["REQ", "ETH"],
        ["TORN", "USDT"], ["RLC", "USDT"],
        ###################################### COIN->COIN
        ["BNB", "ETH"], ["BNB", "BTC"],     ["XRP", "ETH"],
        ["ADA", "BTC"], ["ADA", "ETH"],     ["SOL", "BTC"], ["SOL", "ETH"],
        ["DOT", "BTC"], ["DOT", "ETH"],
]