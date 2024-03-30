# Create Sepolia Network
## in brownie
brownie networks add Ethereum sepolia host=https://sepolia.infura.io/v3/$WEB3_INFURA_PROJECT_ID explorer=https://api-sepolia.etherscan.io/api chainid=11155111 multicall2='0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696'

## in .brownie/network-config.yaml
- chainid: 11155111
explorer: https://api-sepolia.etherscan.io/api
host: https://sepolia.infura.io/v3/$WEB3_INFURA_PROJECT_ID
id: sepolia
name: sepolia

# Create Sepolia Testnet Network
brownie networks add Development sepolia-fork cmd=ganache-cli accounts=10 fork=https://eth-sepolia-public.unifra.io mnemonic=brownie port=8545 host=http:\\127.0.0.1