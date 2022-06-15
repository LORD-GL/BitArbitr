""" 
        BINANCE API TEST
        Artem owner
"""


from binance import Client

client = Client(
        api_key = "829xiDt1qVppZpbICFxGpdOk0jzYL1wRud4o8AvhPCd8MPBJ8VBemH4wwLO979c7",
        api_secret = "Il90XntF9CV2gbGRNfcEg2yhaXq6FmuncacBNEgBWAUiJ4qPx7wEdx56eHRdDSRE"
)

def get_price(symbol="ETHUSDT"):
    try:
        if "BTTUSDT" in symbol:
                symbol = "BTTCUSDT"
        elif "DAIUSDT" in symbol:
                symbol = "USDTDAI"
        elif "DOGEUSDC" in symbol or "FTMUSDC" in symbol or "BATUSDC" in symbol or "ALGOUSDC" in symbol: return -1
        return float(client.get_symbol_ticker(symbol=symbol).get('price'))
    except:
            return -1

# def get_price(symbol="ETHUSDT"):
#         return client.get_symbol_ticker(symbol=symbol).get('price')

# price["ETH/USDT"] = client.get_symbol_ticker(symbol="ETHUSDT")
# price["BTC/BUSD"] = client.get_symbol_ticker(symbol="BTCBUSD")

# print(price["ETH/USDT"])
# # print(price["BTC/BUSD"])
# print("ETH/USDT: ", get_price(symbol = "ETHUSDT"))
# print("BTC/BUSD: ", get_price(symbol = "BTCBUSD"))