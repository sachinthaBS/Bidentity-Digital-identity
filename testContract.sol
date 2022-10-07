pragma solidity ^0.8.17;

// Creating a Smart Contract
contract uIdentity{

// Structure of id
struct id{
	
	// State variables
	uint256 nic;
	string firstName;
    string lastName;
	string addressline1;
    string addressline2;
}

id []ids;

// Function to add
// id details
function addid(
	uint256 nic, string memory firstName,
    string memory lastName,
	string memory addressline1,
	string memory addressline2
) public{
	id memory e
		=id(nic,
				firstName,
				lastName,
				addressline1,
                addressline2);
	ids.push(e);
}

// Function to get
// details of idholder
function getid(
	uint256 nic
) public view returns(
	string memory,
	string memory,
	string memory,
    string memory){
	uint i;
	for(i=0;i<ids.length;i++)
	{
		id memory e
			=ids[i];
		
		// Looks for a matching
		// id
		if(e.nic==nic)
		{
				return(e.firstName,
                    e.lastName,
					e.addressline1,
					e.addressline2);
		}
	}
	
	// If provided id
	// id is not present
	// it returns Not
	// Found
	return("Not Found",
			"Not Found",
			"Not Found",
            "Not Found");
}
}