// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {

    uint256 favoriteNumber;
    uint256 myvar;

    // This is a comment!
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;

    constructor() public {
        favoriteNumber = 42;
    }
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber ,uint multiplier) public {
        favoriteNumber = _favoriteNumber * multiplier;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}