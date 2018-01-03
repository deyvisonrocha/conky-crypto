import requests, json
import babel.numbers, decimal

bitcoin = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=BRL"
data = requests.get(bitcoin).json()
with open('./tmp/bitcoin', 'w') as outfile:
    json.dump(data, outfile)

raiblocks = "https://api.coinmarketcap.com/v1/ticker/raiblocks/?convert=BRL"
data = requests.get(raiblocks).json()
with open('./tmp/raiblocks', 'w') as outfile:
    json.dump(data, outfile)

requestnetwork = "https://api.coinmarketcap.com/v1/ticker/request-network/?convert=BRL"
data = requests.get(requestnetwork).json()
with open('./tmp/request-network', 'w') as outfile:
    json.dump(data, outfile)

xtrabytes = "https://api.coinmarketcap.com/v1/ticker/xtrabytes/?convert=BRL"
data = requests.get(xtrabytes).json()
with open('./tmp/xtrabytes', 'w') as outfile:
    json.dump(data, outfile)
