from web3 import Web3, HTTPProvider
import json
from abi import abi
from dotenv import load_dotenv
import os

#import time 



load_dotenv()


polygon_url = os.getenv("POLYGON_URL")
print(polygon_url)
address = os.getenv("CONTRACT")
print(address)
contract_abi = abi

#web3 = Web3(HTTPProvider(polygon_url))
#print(web3.isConnected())
#contract = web3.eth.contract(address = address, abi = contract_abi)
#all_func = contract.all_functions()
#print(all_func)
# Nonce: The number of transactions made by the sender prior to this one
# getTransactionCount(): Get the number of transactions sent from this address
#nonce = web3. eth. getTransactionCount('0x2BFFE2aE8BC653FbEF35ED7812F625f18AAb504A')
#print(nonce)

#tx = {
#      
#     'value': web3.toWei(0,"ether"),
#     'gas': 320000,
#     'gasPrice': web3.toWei('60',"gwei"),
#     'nonce': nonce,
#     'chainId': 80001
#}

key = os.getenv("PRIVATE_KEY")
print(key)

# MINT
#mint_tx = contract.functions.createCollectible().buildTransaction(tx)
#print(mint_tx)
#signed =web3.eth.account.sign_transaction(mint_tx,key)
#signed.rawTransaction
#tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)
#print(tx_hash)

# GET LAST ID
#id = contract.functions.tokenCounter().call() - 1
#print('Your token Id is: ',id)
#tokenCounter = contract.functions.tokenCounter().call()
#print('the number of nfts deployed are: ', tokenCounter)

# GET RANDOM NUMBER 
#for i in range(100):
#     vago_random_number = contract.functions.idToRandomNumber(id).call()
#     print(vago_random_number)
#     time.sleep(2)

# PRINT SPECIFIC RANDOM NUMBER TO ID
#def rand_to_nft(_id):
#     random_number = contract.functions.idToRandomNumber(_id).call()
#     print(random_number)
#     return random_number
