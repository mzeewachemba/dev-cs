from solcx import compile_standard,install_solc
install_solc("0.8.19")
import json
from web3 import Web3
import os
from dotenv import load_dotenv


def deploy():

    load_dotenv()

    with open("./blockchain_2/contracts/newContract.sol",'r') as file:  #change to path and name of newContract
        new_contract_file = file.read()

    compiled_sol = compile_standard(  #change all refrences of SimpleStorage to newContract
        {
            "language": "Solidity",
            "sources": {"newContract.sol": {"content": new_contract_file}},
            "settings": {
                "outputSelection":  {
                    "*": {
                        "*":["abi","metdata","evm.bytecode","evm.sourceMap"]
                    }
                }
            },
        },
        solc_version="0.8.19"
    )

    with open("compiled_code.json","w") as file:
        json.dump(compiled_sol,file)
        
    # change references of SimpleStorage to newContract

    bytecode = compiled_sol["contracts"]["newContract.sol"]["newContract"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["newContract.sol"]["newContract"]["abi"]

    #make sure you have your .env file set up with these variables
    w3 = Web3(Web3.HTTPProvider(os.getenv("PROVIDER")))
    chain_id = os.getenv("CHAINID")
    my_address = os.getenv("ACCOUNT")
    private_key = os.getenv("PRIVATE_KEY")

    # TODO
    # create a variable newContract that get assigned a contract reference from w3.eth.contract
    newContract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # create a variable nonce that get assigned the transaction count of my_address from w3.eth.getTransactionCount
    nonce = w3.eth.get_transaction_count(my_address)

    # create a variable transaction that gets assigned the newContract.constructor().buildTransaction() method
    transaction = newContract.constructor().build_transaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": my_address,
            "nonce": nonce,
        }
    )

    # create a variable signed_txn that gets assigned the w3.eth.account.sign_transaction() method
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)


    print("Deploying Contract!")
    # Send it!
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


    return tx_receipt.contractAddress

if __name__ == '__main__':
    contractAddress = deploy()
    print(contractAddress)