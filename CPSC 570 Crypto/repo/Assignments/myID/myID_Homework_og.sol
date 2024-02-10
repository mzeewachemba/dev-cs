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
    mapping (___) ____;

    // Create a modifier onlyOwner
    modifier onlyOwner{
        // statements
    }

    constructor(string memory _first, string memory _last, uint _id) {

        // assign the ID structure to the variable
        id = ______________;

        //  Assign the createor of this contract as the owner
        owner = _______;

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
        require(____________ || ________ ,"You are not approved to view this ID");

        return(id);
    }
}


