// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// import "../interfaces/IERC20.sol";

// contract UBToken is IERC20 {
contract UBStudentToken {

    address owner;
    string public name = "UBStudent";
    string public symbol = "US";
    uint8 public decimals = 18;
    uint public totalSupply;

    event Transfer(address indexed _from, address indexed _to, uint256 _value);

    mapping(address => uint) public balanceOf;

    constructor(uint initialSupply) {
        totalSupply = initialSupply;
        owner = msg.sender;
        balanceOf[owner] = initialSupply;
    }

    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(amount <= balanceOf[msg.sender], "Insufficient balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
}