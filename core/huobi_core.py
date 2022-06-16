""" 
        HUOBI API TEST
"""

from huobi import HuobiRestClient

client = HuobiRestClient(
    access_key = "56d2c9bd-67054997-ur2fg6h2gf-d00e4",
    secret_key = "893b8599-394ee401-7da5f115-0c040"
)

# price = client.market_history_trade(symbol="btcusdt").data


# print(price['data'][0]['data'][0]['price'])

def get_price(symbol):
    try:
        if "hotusdt" in symbol:
            return -1
        elif "gstusdt" in symbol:
            return -1
        return float(client.market_history_trade(symbol=symbol).data['data'][0]['data'][0]['price'])
    except:
        return -1