from brownie import SimpleStorage , accounts , myContract



def deploy_simple_storage ( ) :
    account = accounts [ 0 ]
    print ( account )

    SimpleStorage.deploy ( {'from' : account} )


def main ( ) :
    deploy_simple_storage ( )
