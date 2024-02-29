# # main program

# import json
# from dotenv import load_dotenv
# from solcx import compile_standard , install_solc
# install_solc("0.8.19")
# from web3 import Web3
# import os


# def compile(contract):

#     # Get the current directory of the deploy.py script
#     current_dir = os.path.dirname(os.path.realpath(__file__))

#     # Construct the file path to SimpleStorage.sol
#     file_path_ssol = os.path.join(current_dir, f'{contract}')

#     # Read the content of SimpleStorage.sol
#     with open(file_path_ssol, "r") as file:
#         simple_storage_file = file.read()

#     # Compile the Solidity code
#     compiled_sol = compile_standard(
#         {
#             "language": "Solidity",
#             "sources": {f"{contract}": {"content": simple_storage_file}},
#             "settings": {
#                 "outputSelection": {
#                     "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
#                     # "*": {"*": ["abi"]}

#                 }
#             },
#         },
#         solc_version="0.8.19", #should conside with pragme version range in the contract
#     )

#     # print(compiled_sol)
#     # Construct the file path to SimpleStorage json
#     file_path_json = os.path.join(current_dir, 'SimpleStorage_compiled.json')

#     with open(file_path_json, "w") as file: #writes compile.sol output to a file
#         json.dump(compiled_sol, file)

#     abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
#     bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]


#     return abi, bytecode

# def deploy(w3,wallet,chain_id):
    
#     contract = "SimpleStorage.sol"

#     abi, bytecode = compile(contract)

#     simple_storage = w3.eth.contract(abi=abi, bytecode=bytecode) #interface to the contract

#     nonce = w3.eth.get_transaction_count(wallet) #obtain number of transactions

#     print(nonce)

#     transaction = simple_storage.constructor().build_transaction(
#         {

#         "chainId": chain_id,
#         "gasPrice": w3.eth.gas_price,
#         "from": wallet,
#         "nonce": nonce,
#         }

#     )

#     #signing transaction using private key
#     signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

#     #getting the hash for trx
#     tx_hash = w3.eth. send_raw_transaction(signed_txn.rawTransaction)

#     #getting the receipt for trx
#     tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#     # print(tx_receipt)

#     return tx_receipt,abi

# def interact(contract_address,abi,w3,wallet):
#     nonce = w3.eth.get_transaction_count(wallet)
#     simple_storage = w3.eth.contract(address=contract_address, abi=abi)

#     #blue can just be called out of the blue
#     stored_number = simple_storage.functions.retrieve().call()

#     print(f'Original Number: {stored_number}')

#     number = 204
#     #orange transaction is built
#     store_transaction = simple_storage.functions.store(number).build_transaction(
#         {
#             "chainId": chain_id,
#             "gasPrice": w3.eth.gas_price,
#             "from": wallet,
#             "nonce": nonce,
#         }
#     )

#     signed_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
#     tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#     tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#     stored_number = simple_storage.functions.retrieve().call()

#     print(f'Modified Number: {stored_number}')

# if __name__ == "__main__":
#     load_dotenv()
#     wallet = os.getenv("WALLET")
#     private_key = os.getenv("PRIVATE_KEY")
#     #connecting to ganache/sepolia
#     # w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545")) #rpc server from ganache
#     w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/3c28100a3d694b179102ef9eeb204351")) #rpc server from ganache

#     # chain_id = 1337 #  network id from ganache
#     chain_id = 11155111 #  network id from ganache
#     tx_receipt,abi = deploy(w3,wallet,chain_id)
#     interact(tx_receipt.contractAddress , abi , w3 , wallet)













# def compile(contract):
# with open(f"./contracts/{contract}.sol", "r") as file:
# simple_storage_file = file.read()

# compiled_sol = compile_standard(

# "language": "Solidity",
# "sources": {f"{contract}. sol": {"content": simple_storage_file}},
# "settings": {
# "outputSelection": {
# "*": {"*": ["abi", "metadata", "evm.bytecode", "evm. sourceMap"]}

# solc_version="0.8.19",

# with open(f".\compiled\{contract}_compiled.json", "w") as file:
# json. dump(compiled_sol, file)

# abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# return abi, bytecode

#Final
# import json
# from solcx import compile_standard
# from web3 import Web3

# def compile(contract): ...

# abi, bytecode = compile("SimpleStorage")

# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
# chain_id = 1337

# wallet = "0xc218F3838CC150D609A4C4d47f82977837BF030e"
# private_key = "a23a9f84251dfea5b62ec9dcd5c52870c1d60ebd49700573b62431f770984386"

# simple_storage = w3.eth.contract(abi=abi, bytecode=bytecode)

# nonce = w3.eth.get_transaction_count(wallet)

# transaction = simple_storage.constructor().build_transaction(
# {

# "chainId": chain_id,
# "gasPrice": w3.eth.gas_price,
# "from": wallet,
# "nonce": nonce,

# signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# tx_hash = w3.eth. send_raw_transaction(signed_txn.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


# def deploy():

# abi, bytecode = compile("SimpleStorage")

# load_dotenv()

# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
# chain_id = 1337

# wallet = os.getenv("WALLET")
# private_key = os.getenv("PRIVATE_KEY")

# simple_storage = w3.eth.contract(abi=abi, bytecode=bytecode)

# nonce = w3.eth.get_transaction_count(wallet)

# transaction = simple_storage.constructor().build_transaction(

# "chainId": chain_id,
# "gasPrice": w3.eth.gas_price,
# "from": wallet,
# "nonce": nonce,

# signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# return tx_receipt
    


# def deploy():

# abi, bytecode = compile("SimpleStorage")

# wallet = os.getenv("WALLET")
# private_key = os.getenv("PRIVATE_KEY")

# simple_storage = w3.eth.contract(abi=abi, bytecode=bytecode)

# nonce = w3.eth.get_transaction_count(wallet)

# transaction = simple_storage.constructor().build_transaction(

# "chainId": chain_id,
# "gasPrice": w3.eth.gas_price,
# "from": wallet,
# "nonce": nonce,

# (variable) bytecode: Any

# I

# }

# signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# return tx_receipt

