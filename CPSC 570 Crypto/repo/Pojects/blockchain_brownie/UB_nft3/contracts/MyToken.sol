// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; 

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {

    constructor () ERC20("Picha Kali", "ALL") {
        _mint(msg.sender, 1000000 * 10 ** 18); //creates tokens and asign them to deployer's address
    }
}
