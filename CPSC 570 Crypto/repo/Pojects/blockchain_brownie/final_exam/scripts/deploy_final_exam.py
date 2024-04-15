from brownie import accounts, UBToken, UBNFT, Deposit
from scripts.util import get_account

def deploy_token():
    account = get_account(0) # Get the deployer's account
    ubtoken = UBToken.deploy({'from': account})
    recipient_acc = get_account(1)
    ubtoken.transfer(recipient_acc, 1000 * 10 ** 18)  # Transfer 1000 tokens to another account

def deploy_NFT():
    account = get_account(0)  # Get the deployer's account
    ubtoken = UBToken[-1]  # Assuming UBToken has been deployed previously
    ubnft = UBNFT.deploy(ubtoken.address, {'from': account})
    ubnft.set_baseURI('https://your-base-uri.com')  # Set the base URI for NFTs

def register_token():
    account = get_account(0) # Get the deployer's account
    deposit_contract = Deposit.deploy({'from': account})
    ubtoken = UBToken[-1]  # Assuming UBToken has been deployed previously
    deposit_contract.registerToken("UB", ubtoken.address, {'from': account})

def deposit_token():
    account = get_account(0)  # Get the deployer's account
    ubtoken = UBToken[-1]  # Assuming UBToken has been deployed previously
    ubnft = UBNFT[-1]  # Assuming UBNFT has been deployed previously
    ubtoken.approve(ubnft.address, 1000 * 10 ** 18, {'from': account})
    ubnft.deposit(1000 * 10 ** 18, {'from': account})

def mint_nft():
    account = get_account()  # Get the deployer's account
    ubnft = UBNFT[-1]  # Assuming UBNFT has been deployed previously
    ubnft.mint({'from': account})

def main():
    deploy_token()  # Step 1: Deploy token and transfer 1000 tokens
    deploy_NFT()    # Step 2: Deploy NFT with a token fee
    register_token()  # Step 3: Register 'UB' token for use in the NFT
    deposit_token()   # Step 4: Deposit 'UB' tokens into the NFT
    mint_nft()        # Step 5: Mint an NFT with a predefined URI

if __name__ == "__main__":
    main()
