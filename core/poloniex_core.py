from poloniex import Poloniex
polo = Poloniex()
def get_price(base="BTC", quor="USDT"):
    #symbol="USDT_BTC"):
    try:
        ticker = polo.returnTicker()[quor + "_" + base]
    except:
        return -1, -1
    #print(ticker['quoteVolume'])
<<<<<<< HEAD
    return float(ticker['last']), float(ticker['quoteVolume'])
=======
    return float(ticker['last'])

>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
