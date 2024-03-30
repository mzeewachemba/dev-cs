// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// import "../interfaces/IERC20.sol";

// contract UBToken is IERC20 {
contract UBToken {

    address owner;

    string public name = "University of Bridgeport Token";
    string public symbol = "UBT";
    uint8 public decimals = 12;
    uint public totalSupply;

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

    mapping(address => uint) public balanceOf;
    mapping(address => mapping(address => uint)) public allowance;

    modifier only_owner {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

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

    function approve(address spender, uint amount) external returns (bool) {
        require(amount <= balanceOf[msg.sender], "Insufficient balance");
        allowance[msg.sender][spender] += amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint amount) external returns (bool) {
        require(amount <= balanceOf[sender], "Insufficient balance");
        require(amount <= allowance[sender][msg.sender], "Insufficient allowance");
        allowance[sender][msg.sender] -= amount;
        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
    
    //custom functions
    function mint(uint amount) external only_owner {
        totalSupply += amount;
        balanceOf[owner] += amount;
        emit Transfer(address(this), owner, amount);
    }

    function burn(uint amount) external {
        require(amount <= balanceOf[msg.sender], "Insufficient balance");
        totalSupply -= amount;
        balanceOf[msg.sender] -= amount;
        emit Transfer(msg.sender, address(0), amount); // Burn tokens
    }
}