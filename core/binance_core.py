""" 
        BINANCE API TEST
        Artem owner
"""


# from binance import Client
# import requests

# client = Client(
#         api_key = "829xiDt1qVppZpbICFxGpdOk0jzYL1wRud4o8AvhPCd8MPBJ8VBemH4wwLO979c7",
#         api_secret = "Il90XntF9CV2gbGRNfcEg2yhaXq6FmuncacBNEgBWAUiJ4qPx7wEdx56eHRdDSRE"
# )

# def get_price(symbol="ETHUSDT"):
#     try:
#         if "BTTUSDT" in symbol:
#                 symbol = "BTTCUSDT"
#         elif "DAIUSDT" in symbol:
#                 symbol = "USDTDAI"
#         elif "DOGEUSDC" in symbol or "FTMUSDC" in symbol or "BATUSDC" in symbol or "ALGOUSDC" in symbol: return -1
#         return float(client.get_symbol_ticker(symbol=symbol).get('price'))
#     except:
#             return -1

# print(client.get_symbol_ticker(symbol="BTCUSDT"))
# print(client.get_orderbook_ticker(symbol="BTCUSDT"))
#api.binance.com/api/v3/ticker/24hr'

# code : -1121
import requests
import time

list_p = []
respond = requests.get("https://api.binance.com/api/v1/exchangeInfo").json()
for i in respond['symbols']:
       list_p.append(i['symbol'])

# print(resp['lastPrice'])
# print(resp['volume'])

def get_price(symbol="BTCUSDT"):
        if symbol not in list_p:
                return -1, -1
        resp = requests.get(f"https://api.binance.com/api/v1/ticker/24hr?symbol={symbol}").json()
        if resp['lastPrice'] == 0:
                print(resp)
        try:
                return float(resp['lastPrice']), round(float(resp['volume']), 2)
        except:
                return -1, -1

# def get_price(symbol="ETHUSDT"):
#         return client.get_symbol_ticker(symbol=symbol).get('price')

# price["ETH/USDT"] = client.get_symbol_ticker(symbol="ETHUSDT")
# price["BTC/BUSD"] = client.get_symbol_ticker(symbol="BTCBUSD")

# print(price["ETH/USDT"])
# # print(price["BTC/BUSD"])
# print("ETH/USDT: ", get_price(symbol = "ETHUSDT"))
# print("BTC/BUSD: ", get_price(symbol = "BTCBUSD"))