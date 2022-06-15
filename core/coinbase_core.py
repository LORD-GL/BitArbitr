import cbpro
client = cbpro.PublicClient( #AuthenticatedClient
    # "7sqshueErharJjBM",
    # "WeWBTRaKoFMPLV9wD0QqgJrricQuWbxd"
)

#print(client.get_product_ticker('BTC-USDT')['price'])

def get_price(symbol="ETH-USDT"):
    try:
        return float( client.get_product_ticker(symbol)['price'] )
    except:
        return -1
