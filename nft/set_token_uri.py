from abi import abi
from web3 import Web3, HTTPProvider
from test2 import ipfs_to_id

# CONNECTING TO CONTRACT

polygon_url = 'https://polygon-mumbai.infura.io/v3/7bc810d95b2a4b289c5b57fed441236d'
contract_address = '0xf99F9BA4CF4c791F833397ECC2047D34B3fdb19E'
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
key = 'fc77c63111af8a027126fe702aeefe631315506088834f5da81c9d315cc9d0b8'
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