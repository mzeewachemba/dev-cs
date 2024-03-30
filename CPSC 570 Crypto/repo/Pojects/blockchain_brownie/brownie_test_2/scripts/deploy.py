from brownie import SimpleStorage , accounts , config , network 

def deploy_simple_storage ( ) :
    # account = accounts [ 1 ]
    account = get_account( )

    print ( account )

    simple_storage = SimpleStorage.deploy ( {'from' : account} )

    return simple_storage

def interract_simple_storage ( simple_storage ) :
    account = get_account( )

    stored_value = simple_storage.retrieve ( )

    print( f'origina;: \n {stored_value}' )

    traansaction = simple_storage.store(15 , 10 , {'from' : account})

    traansaction.wait(1)

    updated_stored_value = simple_storage.retrieve ( )

    print( f'upadated : \n {updated_stored_value}' )

def get_account():

    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])

def main():
    # print(f'NETWORK: \n {network.show_active()}') # returns the name of the network that we deploy
    simple_contract =  deploy_simple_storage ( )
    interract_simple_storage(simple_contract)
