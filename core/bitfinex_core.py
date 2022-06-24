import requests
import json 
import time
# tBTCUSDT https://api.bitfinex.com/v1/pubticker/{symbol}

p_list = [
  "btcusd", "ltcusd","ltcbtc","ethusd", "ethbtc",
  "etcbtc", "etcusd","rrtusd","zecusd","zecbtc","xmrusd","xmrbtc",
  "dshusd",
  "dshbtc",
  "btceur",
  "btcjpy",
  "xrpusd",
  "xrpbtc",
  "iotusd",
  "iotbtc",
  "ioteth",
  "eosusd",
  "eosbtc",
  "eoseth",
  "sanusd",
  "omgusd",
  "omgbtc",
  "omgeth",
  "neousd",
  "neobtc",
  "etpusd",
  "etpbtc",
  "qtmusd",
  "qtmbtc",
  "edousd",
  "btgusd",
  "btgbtc",
  "datusd",
  "gntusd",
  "sntusd",
  "batusd",
  "mnausd",
  "mnabtc",
  "funusd",
  "zrxusd",
  "zrxbtc",
  "zrxeth",
  "trxusd",
  "trxbtc",
  "trxeth",
  "repusd",
  "btcgbp",
  "etheur",
  "ethjpy",
  "ethgbp",
  "eoseur",
  "requsd",
  "lrcusd",
  "waxusd",
  "daiusd",
  "daibtc",
  "daieth",
  "bftusd",
  "antusd",
  "antbtc",
  "anteth",
  "stjusd",
  "xlmusd",
  "xlmbtc",
  "xvgusd",
  "mkrusd",
  "kncusd",
  "kncbtc",
  "lymusd",
  "utkusd",
  "veeusd",
  "zcnusd",
  "iqxusd",
  "zilusd",
  "zilbtc",
  "bntusd",
  "xrausd",
  "vetusd",
  "vetbtc",
  "gotusd",
  "xtzusd",
  "xtzbtc",
  "trxeur",
  "mlnusd",
  "omnusd",
  "pnkusd",
  "dgbusd",
  "bsvusd",
  "bsvbtc",
  "enjusd",
  "rbtusd",
  "rbtbtc",
  "ustusd",
  "euteur",
  "eutusd",
  "udcusd",
  "tsdusd",
  "paxusd",
  "pasusd",
  "vsyusd",
  "vsybtc",
  "bttusd",
  "btcust",
  "ethust",
  "clousd",
  "ltcust",
  "eosust",
  "gnousd",
  "atousd",
  "atobtc",
  "atoeth",
  "wbtusd",
  "xchusd",
  "eususd",
  "leousd",
  "leobtc",
  "leoust",
  "leoeth",
  "gtxusd",
  "kanusd",
  "gtxust",
  "kanust",
  "ampusd",
  "algusd",
  "algbtc",
  "algust",
  "ampust",
  "uosusd",
  "uosbtc",
  "ampbtc",
  "fttusd",
  "fttust",
  "paxust",
  "udcust",
  "tsdust",
  "chzusd",
  "chzust",
  "dotusd",
  "adausd",
  "adabtc",
  "adaust",
  "fetusd",
  "fetust",
  "dotust",
  "ksmusd",
  "ksmust",
  "uniusd",
  "uniust",
  "snxusd",
  "snxust",
  "yfiusd",
  "yfiust",
  "balusd",
  "balust",
  "filusd",
  "filust",
  "jstusd",
  "jstbtc",
  "jstust",
  "iqxust",
  "xdcusd",
  "xdcust",
  "pluusd",
  "sunusd",
  "sunust",
  "eutust",
  "xmrust",
  "xrpust",
  "dotbtc",
  "xlmust",
  "ctkusd",
  "ctkust",
  "solusd",
  "solust",
  "celusd",
  "celust",
  "bmiusd",
  "bmiust",
  "mobusd",
  "mobust",
  "iceusd",
  "oxyusd",
  "oxyust",
  "idxusd",
  "idxust",
  "qtfusd",
  "qtfbtc",
  "ftmusd",
  "ftmust",
  "icpusd",
  "icpbtc",
  "icpust",
  "fclusd",
  "fclust",
  "mirusd",
  "mirust",
  "grtusd",
  "grtust",
  "btceut",
  "xrdusd",
  "xrdbtc",
  "exousd",
  "etcust",
  "neoust",
  "atoust",
  "xtzust",
  "batust",
  "vetust",
  "trxust",
  "etheut",
  "eurust",
  "axsusd",
  "axsust",
  "hmtusd",
  "hmtust",
  "solbtc",
  "ancusd",
  "ancust",
  "aixusd",
  "aixust",
  "mimusd",
  "mimust",
  "btcmim",
  "mkrust",
  "srmusd",
  "srmust",
  "crvusd",
  "crvust",
  "zmtusd",
  "zmtust",
  "dvfusd",
  "pngusd",
  "pngust",
  "kaiusd",
  "kaiust",
  "woousd",
  "wooust",
  "sgbusd",
  "sgbust",
  "sxxusd",
  "sxxust",
  "ccdusd",
  "ccdust",
  "ccdbtc",
  "gbpust",
  "gbpeut",
  "jpyust",
  "bmnusd",
  "bmnbtc",
  "hixusd",
  "hixust",
  "apeusd",
  "apeust",
  "b2musd",
  "b2must",
  "stgusd",
  "stgust",
#   "gmtusd",
#   "gmtust",
  "gstusd",
  "gstust",
  "vraust",
  "rlyusd",
  "rlyust",
  ]

def get_price(base="btc", quor='usdt'):
    if "usdc" in quor or "dai" in quor:
        return -1, -1
    elif "usdt" in quor:
        quor = "ust"
    elif base == 'GST' or base == "GNO" or base == "BTG":
        return -1, -1
    if base+quor in p_list:
        resp = requests.get(f"https://api.bitfinex.com/v1/pubticker/{base+quor}").json()
    else:
        return -1, -1
    try:
        return float(resp['last_price']), round( float(resp['volume']), 2)
    except:
        return -1, -1
