// SPDX-Licence-Identifier: GPL-3.0 or MIT 
pragma solidity >=0.7.0 <0.9.0 ; //tells what compiler version to use

//--------------------1
// contract My_Storage { //
    
//     //State Variables - any variable outside a function, and exists in a block chain
//     uint256 number;

//     // mappings, events, modifiers

//     //functions
//     function store(uint256 num) public {
//         number = num;
//     }

//     function retrieve() public view returns (uint256) {
//         return number;
//     }
// }


//-------------------2
// contract Owner {
//     // State Variables
//     address private owner;

//     // Functions
//     modifier isOwner {
//         require(msg.sender == owner, "Only owner allowed to change");
//         _; //limit function based on condiions
//         //equivalent to assert in python, USED a lot of times
//     }

//     constructor() {
//         owner = msg.sender; //each time you call a contract it will auomatically pass you a message
//     }

//     // function show_msg() public view returns(address) {
//     //     return (msg.sender);
//     // }

//     function view_owner() public view  returns(address) {
//         return owner;
//     }

//     function change_owner(address new_owner) public {
//         owner = new_owner;
//     }

//     function func2() public isOwner{
//         owner = msg.sender;
//     }
// }


// contract Owner {

//     address owner;
//     //parameterized constructor
//     constructor(address new_owner) {
//         owner = new_owner; //each time you call a contract it will auomatically pass you a message
//     }
// }

contract convert_bytes32{

    function show_bytes32() public pure returns (bytes32){
        return bytes32("University of Bridgeport");
    }
}

