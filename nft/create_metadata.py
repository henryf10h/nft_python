from web3 import Web3, HTTPProvider
from sample_metadata import metadata_template
from abi import abi
from pathlib import Path
import json
import requests
import time

# CONNECTING TO CONTRACT

polygon_url = 'https://polygon-mumbai.infura.io/v3/7bc810d95b2a4b289c5b57fed441236d'
contract_address = '0xf99F9BA4CF4c791F833397ECC2047D34B3fdb19E'
contract_abi = abi
web3 = Web3(HTTPProvider(polygon_url))
print(web3.isConnected())
contract = web3.eth.contract(address = contract_address, abi = contract_abi)

# COUNTER

id = contract.functions.tokenCounter().call() - 1
print('Last token Id deployed: ',id)
tokenCounter = contract.functions.tokenCounter().call()
print('the number of nfts deployed are: ', tokenCounter)


# DEFINE A FNCTION TO UPLOAD TO IPFS
def upload_ipfs(filepath):
    print("Loading file to IPFS")
    with Path(filepath).open("rb") as fp:
        obj = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(ipfs_url + "/api/v0/add",files={"file": obj})
        print(response)
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        file_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash,filename)
        print(file_uri)
        
    return file_uri

# DEFINE A FUNCTION TO SAVE URIS TO A FILE

def save_uri(ipfs_uri):
    with open("uris","a") as file:
        file.write(ipfs_uri + "\n")
        return file

# DEFINE A FUNCTION TO WRITE NFT'S METADATA

def write_metadata():
    for i in range(tokenCounter):
        nft_metadata = metadata_template
        metadata_file_name = (
            "./nft/metadata/" + str(i) + ".json"
        )
        
        if Path(metadata_file_name).exists():
            print("{} already exists!".format(metadata_file_name))
        else:
            print("creating metadata file: {}".format(metadata_file_name))
            nft_metadata["name"] = i
            nft_metadata["description"] = "Vagabundo #{}".format(i)
            image_path = "./nft/metadata/{}.png".format(i)
            image_to_upload = upload_ipfs(image_path)
            nft_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w",encoding = "utf-8") as write_file:
                json.dump(nft_metadata, write_file)
                write_file.close()
                print(metadata_file_name)
                uri = upload_ipfs(metadata_file_name)
                save_uri(uri)
                
                
# WRITE METADATA
write_metadata()



