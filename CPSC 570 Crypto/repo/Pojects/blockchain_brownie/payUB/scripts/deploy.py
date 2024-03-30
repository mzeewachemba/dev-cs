from brownie import payUB, accounts

def deploy_payUB():
    account = accounts[0]
    payUB.deploy({'from': account})

def main():
    deploy_payUB()