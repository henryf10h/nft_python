from abi import abi
from web3 import Web3, HTTPProvider
from test2 import ipfs_to_id
from dotenv import load_dotenv
import os

load_dotenv()

# CONNECTING TO CONTRACT

polygon_url = os.getenv("POLYGON_URL")
contract_address = os.getenv("CONTRACT")
contract_abi = abi
web3 = Web3(HTTPProvider(polygon_url))
print(web3.isConnected())
contract = web3.eth.contract(address = contract_address, abi = contract_abi)
#all_func = contract.all_functions()
#print(all_func)
# Nonce: The number of transactions made by the sender prior to this one
# getTransactionCount(): Get the number of transactions sent from this address
nonce = web3. eth. getTransactionCount('0x2BFFE2aE8BC653FbEF35ED7812F625f18AAb504A')
#print(nonce)
tx = {
      
     'value': web3.toWei(0,"ether"),
     'gas': 200000,
     'gasPrice': web3.toWei('60',"gwei"),
     'nonce': nonce,
     'chainId': 80001
}
# GET LAST ID
#id = contract.functions.tokenCounter().call() - 1
#print('Your token Id is: ',id)
#tokenCounter = contract.functions.tokenCounter().call()
#print('the number of nfts deployed are: ', tokenCounter)
key = os.getenv("PRIVATE_KEY")
# MINT
id = 4
set_token_uri_tx = contract.functions.setTokenURI(id,ipfs_to_id(id)).buildTransaction(tx)
print(type(ipfs_to_id(id)))
print(set_token_uri_tx)
signed =web3.eth.account.sign_transaction(set_token_uri_tx,key)
signed.rawTransaction
tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)
print(tx_hash)
token_uri = contract.functions.tokenURI(id).call()
print(token_uri)
print("https://testnets.opensea.io/assets/{}/{}".format(contract_address,id))