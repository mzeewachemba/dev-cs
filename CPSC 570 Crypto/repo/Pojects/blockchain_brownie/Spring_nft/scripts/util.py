from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200_000_000_000

def get_account(index=2):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[index]
    else:
        return accounts.add(config["wallets"]["from_key"])

# # def deploy_mocks(account):
# def deploy_mocks(account):
#     print(f'The active network is {network.show_active()}')
#     if len(MockV3Aggregator) == 0:
#         aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from': account})
#         print('Mocks Deployed!')
#     else:
#         aggregator = MockV3Aggregator[-1]
#     return aggregator.address
