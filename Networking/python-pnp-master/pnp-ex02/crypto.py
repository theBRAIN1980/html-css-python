import urllib.request as http
import json
import datetime

APISERVER = "https://api.binance.com"
def test():
    print("Testing connectivity ...")
    resp = http.urlopen(f"{APISERVER}/api/v3/ping").read()
    print(resp)

def getTime():
    print("Getting time ...")
    resp = http.urlopen(f"{APISERVER}/api/v3/time").read().decode("ascii")
    respDict = json.loads(resp)
    print(respDict["serverTime"])

def getTrades(sym):
    print("Getting trades ...")
    resp = http.urlopen(f"{APISERVER}/api/v3/trades?symbol={sym}").read().decode("ascii")
    respList = json.loads(resp)
    # for trade in respList:
    #     print(f"{trade['time']}\t{trade['qty']}\t{trade['price']}")
    tFirst = respList[0]['time']
    tLast = respList[-1]['time']
    dt = (tLast - tFirst) / 1000
    print(f"\nTransaction window: {dt}")
    print(f"{len(respList) / dt} transactions per second")
    print(f"Minimum price: {min([t['price'] for t in respList])}")
    print(f"Last price: {respList[-1]['price']}")
    print(f"Volume: {sum([float(t['quoteQty']) for t in respList])}")

def getSym():
    print("Getting symbols ...")
    resp = http.urlopen(f"{APISERVER}/api/v3/exchangeInfo").read().decode("ascii")
    respDict = json.loads(resp)
    symbols = respDict["symbols"]
    symbolsList = [s['symbol'] for s in symbols]
    print(symbolsList)
    print(len(symbolsList))

# test()
# getTime()
#getTrades("BNBUSDT")
getSym()