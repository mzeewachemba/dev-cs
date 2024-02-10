//SPDX-License-Identifier:  GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract personalID {

    address id_owner;

    struct StreetAddress {
        string street;
        string city;
        string sate;
        string zip;
    }

    struct Personal {
        // uint id;
        bytes32 id;
        string first_name;
        string last_name;
        StreetAddress home_address;
        uint date_of_birth;
        string phone_number;
        string email;
    }

    struct Financial {
        string bank_account;
        string routing_number;
        string credit_card;
        bool pay_with_credit_card;
    }

    struct Health {
        uint height; // expressed in cm implied decimals
        uint weight; // expressed in lbs with 2 implied decimals
        string blood_type;
        string allergies;
        string conditions;
        string medications;
    }

    struct Person {
        Personal personal_info;
        Health health_info;
        Financial financial_info;
    }

    Person person;

    event PersonalInfoUpdated(address updated_by, StreetAddress home_address , string phone , string email);
    event HealthInfoUpdated(address updated_by, uint height, uint weight, string blood_type, string allergies, string medications, string conditions);
    event FinancialInfoUpdated(address updated_by, string bank_account, string routing_number, string credit_card, bool pay_with_credit_card);

    modifier  OnlyOwner () {
        require(msg.sender == id_owner,"Only owner can call this function");
        _;
    }

    // set personal information
    // read personal information
    // authorize who reads

    mapping(address => bool) personal_info_authorized; // for everybody thaus authorized store true value
    mapping(address => bool) health_info_authorized;
    mapping(address => bool) financial_info_authorized;

    constructor(
        address _recipient,
        // uint _id,
        bytes32 _id,
        string memory _firrst_name,
        string memory _last_name,
        uint dob
    ){
        id_owner = _recipient;
        person.personal_info.id = _id;
        person.personal_info.first_name = _firrst_name;
        person.personal_info.last_name = _last_name;
        person.personal_info.date_of_birth = dob;

        personal_info_authorized[_recipient] = true;
    }

    function authorizePersonalInfo(address _addres) public OnlyOwner {
        personal_info_authorized[_addres] = true;
    }

    function authorizeHealthInfo(address _addres) public OnlyOwner {
        health_info_authorized[_addres] = true;
    } 

    function authorizeFinancialInfo(address _addres) public OnlyOwner {
        financial_info_authorized[_addres] = true;
    }

    function getPersonalInfo() public view returns (Personal memory) {
        require(personal_info_authorized[msg.sender],"Not Authorized to view personal info");
        return  person.personal_info;
    }

    function getHealthInfo() public view returns (Health memory) {
        require(health_info_authorized[msg.sender],"Not Authorized to view personal info");
        return  person.health_info;
    }

    function getFinancialInfo() public view returns (Financial memory) {
        require(financial_info_authorized[msg.sender],"Not Authorized to view personal info");
        return  person.financial_info;
    } 

    function setpersonalInfo(StreetAddress memory _home , string memory _phone , string memory _email) public OnlyOwner { //passing data type which are not simple requires to use memory
        person.personal_info.home_address = _home;
        person.personal_info.phone_number = _phone;
        person.personal_info.email = _email;
        emit PersonalInfoUpdated(msg.sender, _home, _phone, _email);
    }

    function setHealthInfo(uint _height, uint _weight, string memory _blood_type, string memory _allergies, string memory _medications, string memory _conditions) public OnlyOwner{
        require(health_info_authorized[msg.sender] == true, "Not authorized to update health info");
        emit HealthInfoUpdated(msg.sender, _height, _weight, _blood_type, _allergies, _medications, _conditions);
        person.health_info.height = _height;
        person.health_info.weight = _weight;
        person.health_info.blood_type = _blood_type;
        person.health_info.allergies = _allergies;
        person.health_info.medications = _medications;
        person.health_info.conditions = _conditions;
    }

    function setFinancialInfo(string memory _bank_account, string memory _routing_number, string memory _credit_card, bool _pay_with_credit_card) public OnlyOwner {
        emit FinancialInfoUpdated(msg.sender, _bank_account, _routing_number, _credit_card, _pay_with_credit_card);
        person. financial_info.bank_account = _bank_account;
        person. financial_info.routing_number = _routing_number;
        person.financial_info.credit_card = _credit_card;
        person. financial_info.pay_with_credit_card = _pay_with_credit_card;
    }
}