//SPDX-License-Identifier:  GPL-3.0
pragma solidity >=0.7.0 <0.9.0 ;

//chainlink contract
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PayUB {
    // Add student bill
    // Withdraw the payments
    // Student pay bill
    // Student view bill
    
    address owner;
    address[] students_billed;
    mapping(address => uint256) bills_to_pay;

    modifier  OnlyOwner () {
        require(msg.sender==owner,"You are not Authorized");
        _;
    }

    constructor(){
        owner = msg.sender;
    }

    function AddBill(address _student , uint256 _bill_amount) public OnlyOwner {
        students_billed.push(_student);
        bills_to_pay[_student] += _bill_amount;
    }

    function ViewBill() public view returns(uint256) {
        return bills_to_pay[msg.sender];
    }

    function Withdraw() public payable OnlyOwner {
        payable(owner).transfer(address(this).balance); //transfer from contract to this owner
    }

    function Get_Price() public view returns(uint256) {
        AggregatorV3Interface price_feed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        (,int256 price,,,) = price_feed.latestRoundData(); //extract second vlue as price data
        // uint decimal = price_feed.decimals(); //
        return uint256(price*10**10); //18 decimal places for etherium compatibility and precision
    }

    function Get_conversion_rate(uint256 eth_amount) public view returns(uint256) {
        uint256 eth_price = Get_Price();
        uint256 eth_amount_in_usd = (eth_price * eth_amount) / 10**18;
        return eth_amount_in_usd;
    }

    function Pay() public payable  {
        uint256 amount_paid = Get_conversion_rate(msg.value); // this will get the valuee from solidity ui
        bills_to_pay[msg.sender] -= amount_paid;
    }
}