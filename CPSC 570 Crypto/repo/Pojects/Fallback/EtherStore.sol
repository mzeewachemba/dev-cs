// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;

contract Etherstore {
    // uint256 public withdrawalLimit = 1 ether;
    // mapping(address => uint256) public lastWithdrawTime;
    mapping(address => uint256) public balances;

    function depositFunds() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdrawFunds(uint256 _weiToWithdraw) public {
        // Infinite gas

        require(balances[msg.sender] >= _weiToWithdraw);

        // Limit the withdrawal
        // require(_weiToWithdraw <= withdrawalLimit, "Exceeds withdrawal limit");

        // Limit the time allowed to withdraw
        // require(now >= lastWithdrawTime[msg.sender] + 1 weeks, "Withdrawal time not reached yet");

        (bool success, ) = msg.sender.call.value(_weiToWithdraw)("");
        require(success, "Transaction not successful");

        balances[msg.sender] -= _weiToWithdraw;
        // lastWithdrawTime[msg.sender] = now;
    }
}
