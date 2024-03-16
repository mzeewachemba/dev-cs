from brownie import myStudentId , accounts


def deploy_my_student_id ( ) :
    # Deploy the contract
    student_id = 123456789  # Example student ID
    account = accounts [ 0 ]

    my_contract = myStudentId.deploy ( student_id , {'from' : account} )

    # Print contract address
    print ( "Contract deployed at:" , my_contract.address )


def main ( ) :
    deploy_my_student_id ( )
