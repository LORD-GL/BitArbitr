""" 
        KUKOIN API TEST
"""

from kucoin.client import Client

client = Client(
    api_key = "629f806bc437540001f82190",
    api_secret = "05cea257-7163-4b72-87a8-fbb9cd6b40c2",
    passphrase = ""
)

def get_price(symbol="BTC-USDT"):
    if "DAI-USDT" in symbol:
        symbol = "USDT-DAI"
    data = client.get_ticker(symbol)
    try:
        return float(data['price']), round(float(client.get_24hr_stats(symbol)['vol']), 2)
    except:
        return -1, -1
