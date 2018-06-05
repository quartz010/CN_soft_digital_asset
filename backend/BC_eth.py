import time
from web3 import Web3, HTTPProvider

api = "https://ropsten.infura.io/EF0HiTihtDEGGyVZ5Yvs"

web3 = Web3(HTTPProvider(api))

if web3.isConnected:

    print('remote loaded!')
    print(web3.eth.getBalance("0x7Aba3b6723eb1651e1a99494dB7f871c3C53ff01"))
