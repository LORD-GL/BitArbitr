""" 
        KUKOIN API TEST
"""

from kucoin.client import Client

client = Client(
    api_key = "629f806bc437540001f82190",
    api_secret = "05cea257-7163-4b72-87a8-fbb9cd6b40c2",
    passphrase = ""
)

# price = client.get_ticker("BTC-USDT")

# print(price['price'])

def get_price(symbol):
    if "DAI-USDT" in symbol:
        symbol = "USDT-DAI"
    try:
        return float(client.get_ticker(symbol)['price'])
    except:
        return -1


# print(client.get_order_book("BTC-DAI"))
# print(get_price("BTC-DAI"))