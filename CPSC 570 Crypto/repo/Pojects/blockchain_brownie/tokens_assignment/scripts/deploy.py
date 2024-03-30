from brownie import UBStudentToken 
from scripts.util import get_account

def send_tokens():
    account = get_account()
    token = UBStudentToken.deploy(10000000 * 10**18, {'from': account})
    recipient = "0xCDdE8850c5F52B9A03631C1Bf241423164fb3d43"
    amount = 1000 * 10**18  # 1,000 tokens
    token.transfer(recipient, amount, {'from': account})

    # Print token details for verification
    print(f'Token Name: {token.name()}')
    print(f'Token Symbol: {token.symbol()}')
    print(f'Total Supply: {token.totalSupply()}')
    print(f'Recipient Balance: {token.balanceOf(recipient)}')

def main():
    send_tokens()

