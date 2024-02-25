// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.5.0;

// import "./deposit_receiver.sol";

contract Deposit_Sender {
    // Deposit_Receiver dr;
    address payable receiver;

    constructor (address payable _receiver) public {
        // dr = Deposit_Receiver(_receiver);
        receiver = _receiver;
    }

    function deposit() public payable {}

    function send() public payable {
        // dr.deposit.value(address(this).balance)();
        receiver.transfer(address(this).balance);

    }
}