# from solcx import compile_standard
# import json
# from web3 import Web3
#
# with open("./SimpleStorage.sol",'r') as file:
# simple_storage_file = file.read()
#
# compiled_sol = compile_standard(
#
# "language": "Solidity",
# "sources":
# {"SimpleStorage.sol":
# {"content": simple_storage_file}
#
# "settings": {
# "outputSelection":
#
# #Get bytecode and ABI
# bytecode =
# compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["ekm"]
# ["bytecode"]["object"]
# abi =
# compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
#
# #connection information
# W3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# chain_id = 1337
# my_address = "0x85c793b0e522d6cB241290207421eEc1F4Aa1201"
# private_key =
# "0x50923f6fc6b30c69bfdfe73e8e0430c5327299298f2f7a3123dde1148d174ffe"
#
# ["abi", "metdata", "evm. bytecode", "evm. sourceMap" ]
#
# solc_version="0.6.0",
#
# with open("compiled_code.json","w") as file:
# json.dump(compiled_sol,file)
#
# SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
# nonce = w3.eth.get_transaction_count(my_address)
#
# transaction = SimpleStorage.constructor() .buildTransaction(
# {"chainId":chain_id,"gasPrice":
# w3.eth.gas_price, "from":my_address, "nonce": nonce})
#
# signed_txn = w3.eth.account.sign_transaction(transaction,private_key)
#
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)