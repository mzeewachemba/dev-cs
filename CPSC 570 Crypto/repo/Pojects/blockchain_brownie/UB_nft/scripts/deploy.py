from brownie import UBNFT, UBToken, accounts ,network , config
from scripts.pinata import upload_folder, get_pinned
from scripts.metadata import create_metadata
from scripts.util import get_account

def check_IPFS(): #cjecking if ifps has files
    pinned = get_pinned()
    # print(f'pinned is {pinned}')
    if 'images' not in pinned:
        upload_folder('.//images//')
    if 'metadata' not in pinned:
        create_metadata('.//images//', './/metadata//')
        upload_folder('.//metadata//')

    pinned = get_pinned()

    return pinned['metadata'] # gets the hash of the metadata

def deploy_token(): # Deploys an ERC20 token contract (UBToken) using the deployer's account .
    account = get_account()
    # print(f'Networks are: {config}')
    ubtoken = UBToken.deploy({'from': account}, publish_source=config['networks'][network.show_active()].get('verify', False))
    # ubtoken = UBToken.deploy({'from': account})
    return ubtoken # Returns the deployed token contract address


def deploy_nft():
    account = get_account()
    baseuri = check_IPFS()
    if network.show_active() == 'development' or len(UBToken) == 0: # Checks if the network is development or if the token has not been deployed yet.
        token = deploy_token()
    else:
        token = UBToken[-1]

    ubnft = UBNFT.deploy( 
        token.address ,  
        {"from": account},
        publish_source=config['networks'][network.show_active()].get('verify',False)
    )

    # ubnft = UBNFT.deploy( 
    #     token.address ,  
    #     {"from": account}
    # )

    # ubnft.set_baseURI('QmTJmA7AHFjsD3EPRvo75aKkigHb8whQDK495DKpUDHc89')

    ubnft.set_baseURI(f'ipfs://{baseuri}')
    return ubnft,token

def main():
    ubnft = deploy_nft()
    print(ubnft.tokenURI(1))
