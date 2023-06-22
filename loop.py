import threading
from tracemalloc import stop
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/bdf1fa41e5684998838209c7861d19ae"))
private_key = "<98d283573e373704a1e5b85fadd85c84aecf0c1442f8a81492220315c476d533>"
pub_key ="<0xc8491fE4C330e974405f57a5Ae6d6591d6fD41b9>"

recipient_pub_key = "<0x5c98bd53E5E583Cd2bCBC97932dC89fB0ea4689A>"
def loop():
    while True:
        balance = w3.eth.get_balance(pub_key)
        print()
        print(balance)
        gasPrice = w3.toWei('1100', 'gwei')
        gasLimit = 21000
        nonce = w3.eth.getTransactionCount(pub_key)
        tx = {
            'chainId': 1,
            'nonce': nonce,
            'to': recipient_pub_key,
            'value': balance-gasLimit*gasPrice,
            'gas': gasLimit,
            'gasPrice': gasPrice
        }

        try:
         if balance > 0:
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(w3.toHex(tx_hash))
        except:
            print("insufficient funds")

threading.Thread(target=loop, daemon=True).start()
input('Press Enter to exit.')
