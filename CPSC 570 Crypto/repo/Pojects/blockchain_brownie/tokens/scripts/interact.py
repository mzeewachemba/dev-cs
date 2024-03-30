from scripts.util import get_account
from brownie import interface , network

TOKEN_ADDRESS = "0xc132ec2e4B6130273AE6C6eD0a1B8bEE2C3815a0"

def get_total_supply():
    account = get_account()
    token = interface.ERC20(TOKEN_ADDRESS)
    print(token.totalSupply())
    print(token.balanceOf(account.address))

def main():
    get_total_supply()