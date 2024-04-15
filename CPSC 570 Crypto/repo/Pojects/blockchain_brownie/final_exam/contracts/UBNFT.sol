// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; 

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UBNFT is ERC721,Ownable {
    
    uint total_supply = 5000;
    uint public token_counter = 1;
    mapping(uint => address) public token_owner;

    string base_uri = "";

    address payment_token;
    mapping(address => uint) public paid_fees;
    uint public fee = 1000 * 10**18;
    uint total_fees = 0;

    constructor(address _token) ERC721("University of Bridgeport Logos", "UBL") {
        payment_token = _token;

    }

    function getFee() public view returns (uint256) {
        return fee;
    }
   
    function set_baseURI(string memory _uri) public onlyOwner {
        base_uri = _uri;
    }
    function _baseURI() internal view override returns (string memory) {
        return base_uri;
    }
    function baseURI() public view returns (string memory) {
        return _baseURI();
    }

    function tokenURI(uint tokenID) public view virtual override returns (string memory) {
        require(tokenID <= token_counter, "Token ID does not exist");
        return string(abi.encodePacked(_baseURI(), "/", Strings.toString(tokenID)));
    }

    function deposit(uint _amount) public payable {
        require(IERC20(payment_token).allowance(msg.sender, address(this)) >= _amount, "Allowance not enough");

        IERC20(payment_token).transferFrom(msg.sender, address(this), _amount);
        paid_fees[msg.sender] += _amount;
        total_fees += _amount;

    }

    function mint() public  {
        require(paid_fees[msg.sender] >= fee, "Not enough fees");
        paid_fees[msg.sender] -= fee;
        token_owner[token_counter] = msg.sender;
        _safeMint(msg.sender, token_counter);
        token_counter++;
    }

    function withdraw_tokens() public payable onlyOwner {

        IERC20(payment_token).transfer(msg.sender, IERC20(payment_token).balanceOf(address(this)));
    }

}