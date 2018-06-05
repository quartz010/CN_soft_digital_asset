import time
from web3 import Web3, HTTPProvider

<<<<<<< HEAD

=======
api = "https://ropsten.infura.io/EF0HiTihtDEGGyVZ5Yvs"
>>>>>>> 422a917935b9ab2b66b0f1aab7b1f5869608c2dd

web3 = Web3(HTTPProvider(api))

if web3.isConnected:

    print('remote loaded!')
    print(web3.eth.getBalance("0x7Aba3b6723eb1651e1a99494dB7f871c3C53ff01"))
