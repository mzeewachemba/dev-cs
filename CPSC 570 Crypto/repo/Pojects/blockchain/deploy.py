# main program

import _json
from solcx import compile_standard
from web3 import Web3

with open(f'./contracts/SimpleStorage.sol',"r") as file: #store contract as variable
    simple_storage_file = file.read()

compiled_sol = compile_standard( #helps to compile the code
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm. sourceMap"]}
            }
        },
    },
    solc_version="0.8.19",
)

print(compiled_sol)