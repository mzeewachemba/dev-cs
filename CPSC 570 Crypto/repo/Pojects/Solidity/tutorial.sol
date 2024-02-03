//SPDX-License-Identifier:  GPL-3.0
pragma solidity >=0.7.0 <0.9.0 ; //tells what compiler version to use ,ranges are acceped here
// ^ is used as greater tha or equal to

contract contractName { // class
    // State Variables - Global variable - kept track out of block chain - they cost money
    uint private var1;
    int public var2 = 7896; // the samee as creating a function that returns var2
    //with inassigned int you can specify the size
    //smaller variable sizes are better
    uint176 var7;
    bytes32 var3; //same a uint256 used for not number but data
    bool var4; //true of false
    address var5; //addresss of a contract,wallet,transaction  or aything in the blockchain
    address  owner;
    // uint counter;

    uint[] my_array1; //dynamic array, grows/shrink
    uint[10] my_array2; //Fixed array or 10 positionss and is indexed from 0 to 9
    
    struct Student { // looks like an object
        uint id;
        string name;
        uint grade_average;
    }

    Student public student; 


    //other
    modifier is_student_20 {
        require(student.id == 20, "Not valid statement");
        _;
    }

    modifier is_owner {
        require(msg.sender == owner);
        _;
    }

    //function
    // function test() public returns(uint [] memory) {
    //     uint my_test_var;
    //     my_test_var = 10;
    //     var1 = my_test_var;

    //     // while(counter < 100){

    //     // }

    //     my_array1.push(10);
    //     my_array1.push(20);
    //     my_array1[1] = 10;
       
    //     return  my_array1;
    // }

    // function test2() public returns(uint [] memory) {
    //     my_array1.pop();
    //     return my_array1;
    // }

    // function test3() external   {
    //     student.id = 10;
    //     student.name = "allen";
    //     student.grade_average = 100;

    //     Student memory ubstudent = Student(20,"irene",100); //constructor type

    //     ubstudent = Student({id:30, name:"kaloo",grade_average:99});//using dictionary, order doesnt matter
    // }

    // //to call test3
    // // function test4() public {
    // //     test3();//can only be called from outside if its external 
    // // }

    // // memory is used to create a non state variable thus not of atomic type
    // function view_student() public view returns(Student memory) {
    //     return  student;
    // }


    // //pure functions don't change or access state variables
    // //view functions dont' change state variables but can access/ just read only
    // function test5() public pure {
    //     uint var1 = 10;
    // }

    //constructor - constructor variable name will be see in the deploy inputs
    constructor( uint _id) {
        owner = msg.sender; //each time you call a contract it will auomatically pass you a message
        student.id = _id;
        //student.name = _name;
    }

    //require
    function test7() public view is_student_20 returns(uint) {
        //loops
        // uint counter = 0;
        // while(counter < 100) {
        //     counter += 1;
        //     //break and continue keywords
        // }

        //do while

        //fo loop
        //for (uint cnt=0; cnt<100; cnt += 1){};
        return student.id; //return will be executed if above condition is true
    }

}

contract payme {

    address payable public owner;
    // address[10] depositors;
    // uint ccurrent_depositor;
    //mapping
    mapping (address => uint256) public depositors; //creates an array of uint256 values indexed by address

    //events and emit - used for auditing - LOGS
    event depossited(address indexed  depositor, uint256 indexed value);

    constructor() payable {
        owner = payable(msg.sender);
    }

    function deposit() public payable {
        // depositors[ccurrent_depositor] = msg.sender;
        // ccurrent_depositor += 1;
        depositors[msg.sender] = msg.value;
        emit depossited(msg.sender, msg.value);// writing logs
    }

    function withdraw() public {
        uint amount = address(this).balance;
        owner.transfer(amount); 
    }
}