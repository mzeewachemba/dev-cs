from brownie import UBToken , UBTokenEasy
from scripts.util import get_account

def deploy_easy():
    account = get_account()
    token = UBTokenEasy.deploy(1000*10 ** 12, {'from': account})
    print(token.balanceOf(account.address))

def deploy_token():
    account = get_account()
    token = UBToken.deploy(1000*10**12, {'from': account})
    print('initial deploy')
    print(token.name())
    print(token. symbol())
    print(token. totalSupply())
    print(token.balanceOf(account.address))
    token.mint(100*10 ** 12, {'from': account})
    print('minting')
    print(token. totalSupply())
    print(token.balanceOf(account.address))
    print('burning')
    token.burn(1000*10 ** 12, {'from': account})
    print(token.totalSupply())
    print(token.balanceOf(account.address))

def main():
    # deploy_token()
    deploy_easy()
