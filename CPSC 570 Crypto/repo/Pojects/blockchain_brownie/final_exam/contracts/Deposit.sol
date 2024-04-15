// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Deposit is Ownable {
    mapping(string => address) public registeredTokens;
    mapping(address => mapping(string => uint)) public depositedTokens;
    mapping(address => mapping(string => uint)) public feesCharged;
    uint public totalFees;

    event TokenRegistered(string symbol, address tokenAddress);
    event TokensDeposited(uint amount, string symbol, address depositor);
    event FeeCharged(uint amount, address depositor, string symbol);
    event FeesWithdrawn(uint amount, address recipient);

    function registerToken(string memory symbol, address tokenAddress) external onlyOwner {
        require(registeredTokens[symbol] == address(0), "Token already registered");
        registeredTokens[symbol] = tokenAddress;
        emit TokenRegistered(symbol, tokenAddress);
    }

    function depositTokens(uint amount, string memory symbol) external {
        require(registeredTokens[symbol] != address(0), "Token not registered");
        IERC20 token = IERC20(registeredTokens[symbol]);
        require(token.allowance(msg.sender, address(this)) >= amount, "Allowance not enough");
        token.transferFrom(msg.sender, address(this), amount);
        depositedTokens[msg.sender][symbol] += amount;
        emit TokensDeposited(amount, symbol, msg.sender);
    }

    function chargeFee(uint amount, address depositor, string memory symbol) external onlyOwner {
        require(depositedTokens[depositor][symbol] >= amount, "Insufficient deposited tokens");
        depositedTokens[depositor][symbol] -= amount;
        feesCharged[depositor][symbol] += amount;
        totalFees += amount;
        emit FeeCharged(amount, depositor, symbol);
    }

    function withdrawFees() external onlyOwner {
        require(totalFees > 0, "No fees to withdraw");
        uint amount = totalFees;
        totalFees = 0;
        payable(msg.sender).transfer(amount);
        emit FeesWithdrawn(amount, msg.sender);
    }
}
