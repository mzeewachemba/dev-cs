# from brownie import UBNFT , UBToken , network , config
# from scripts.util import get_account
# from scripts.deploy import deploy_nft

# def mint():
#     account = get_account()
#     if network.show_active() == 'development' or len(UBNFT) == 0:
#         nft, token = deploy_nft()
#     else:
#         nft = UBNFT[-1]
#         token = UBToken[-1]

#     fee = nft.fee({'from': account})
#     token.approve(nft.address, fee, {'from':account})
#     nft.deposit(fee,{'from':account})
#     nft.mint({'from':account})

#     # ubnft = deploy_nft()
#     # ubnft.mint({'from': account})

# def main():
#     mint()


from brownie import UBNFT, UBToken, network, config
from scripts.util import get_account
from scripts.deploy import deploy_nft

def mint():
    account = get_account()
    if network.show_active() == 'development' or len(UBNFT) == 0:
        nft, token = deploy_nft()
    else:
        nft = UBNFT[-1]
        token = UBToken[-1]

    fee = nft.fee({'from': account})
    token.approve(nft.address, fee, {'from': account})
    nft.deposit(fee, {'from': account, 'gas_limit': 1000000})  # Set the gas limit here
    nft.mint({'from': account, 'gas_limit': 1000000})  # Set the gas limit here

def main():
    mint()
