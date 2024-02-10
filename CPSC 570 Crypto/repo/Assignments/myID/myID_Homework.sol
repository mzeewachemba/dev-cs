// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract myID {

    struct ID {
        string firstName;
        string LastName;
        uint studentID;
    }

    ID id;

    address owner;

    // Create a mapping called isApproved
    //  maps an address to a bool
    mapping (address => bool) isApproved;

    // Create a modifier onlyOwner
    modifier onlyOwner{
        require(msg.sender == owner,"Not Authorized if you are not a owner");
        _;
    }

    constructor(string memory _first, string memory _last, uint _id) {

        // assign the ID structure to the variable
        id = ID(_first , _last , _id);

        //  Assign the creator of this contract as the owner
        owner = msg.sender;

    }

    function setID(uint _id) public onlyOwner {

        id.studentID = _id;
    }

    function approveViewer(address viewer) public {

        isApproved[viewer] = true;
    }

    function getID() public view returns(ID memory){

        // require that the person requesting the id is approved or the owner
        // || is the logical or operator in Solidity
        require( isApproved[msg.sender] || msg.sender == owner ,"You are not approved to view this ID");

        return(id);
    }
}


