//SPDX-License-Identifier:  GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

import "./PersonalID.sol";

//blockchain cannot have random numbers
//vrf oracle can generate random numbers for you

contract IDBureau {
    address public bureau_chief; //owner
    //uint next_id = 100000;

    // mapping (uint => address) public id_register; //maps int to an address indexed by int
    mapping(bytes32 => address) public id_register; //maps int to an address indexed by int
    mapping(address => bytes32) public id_owner; //maps address to int
    mapping(address => uint256) private funds;

    uint256 public Fee = 0.01 ether; //1**16 wei

    constructor() {
        bureau_chief = msg.sender;
    }

    function get_id(string memory _first_name , string memory _last_name , uint _dob) public pure returns (bytes32) {
        return  sha256(abi.encode(_first_name , _last_name , _dob));
    }

    modifier IsChief() {
        require(msg.sender == bureau_chief, "You are not authorized to use this system");
        _;
    }

    //Emit (create an id)

    function emit_id(
        address _recipient , 
        string memory _first_name , 
        string memory _last_name , 
        uint _dob

        ) public IsChief returns (address) {
        
        require(funds[_recipient] >= Fee, "Insufficient funds to emit ID"); //check if hey have enough funds
        // uint curr_id = next_id;
        // next_id++;

        bytes32 curr_id = get_id(_first_name , _last_name , _dob);
        personalID new_id = new personalID(_recipient , curr_id , _first_name , _last_name , _dob); //creates the contract

        id_register[curr_id] = address(new_id);
        id_owner[_recipient] = curr_id;

        funds[_recipient] -= Fee;

        return address(new_id);
    }

    //Pay for ID, because emitting an ID costs money
    function payFee() public payable {
        require(msg.value == Fee, "Money sent does not equal fee"); //check if the amount is equal to the fee
        funds[msg.sender] += msg.value;
    }

    function withdraw() public payable IsChief {
        payable(bureau_chief).transfer(address(this).balance);//transfer balance from contract to bureau chief
    }
}
