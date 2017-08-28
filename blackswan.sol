pragma solidity ^0.4.0;
contract BlackSwan {

	struct Record {
        uint id;
        string shared_with_fingerprint;
        string description;
        string shared_by_fingerprint;
        address shared_by_address;
        
	}

    Record[] records;

	// keep track of stack sizes
	uint num_records;
	uint records_index; // pointer to current stack element

	address public owner;

	string[6] greetings;

	function BlackSwan() {
		owner = msg.sender;
		num_records = 0;
		records_index = 0;
        
		greetings[0] = "Hi, my name is Omar Metwally.";
		greetings[1] = "I am the creator of this contract.";
		greetings[2] = "Black Swan Lives!";
		greetings[3] = "Watching Parnassus on a beautiful, sunny day in SF...";
		greetings[4] = "Healthcare is a human right.";

	}
	
    /* Generates a random number from 0 to 10 based on the last block hash */
    function randomGen(uint seed) constant returns (uint randomNumber) {
        return(uint(sha3(block.blockhash(block.number-1), seed ))%10);
    }
	
	event RecordCreated (
		uint _id,
		string _shared_with_fingerprint,
		string _description,
		string _shared_by_fingerprint,
		address _shared_by_address
	);

	function push_record(string _shared_with_fingerprint,
	    string _description, string _shared_by_fingerprint, 
	    address _shared_by_address) {
        
		// prevent duplicate entries
		
		records.push( Record(
		    {
		        id: num_records+1,
		        description: _description,
		        shared_with_fingerprint: _shared_with_fingerprint,
		        shared_by_fingerprint: _shared_by_fingerprint,
		        shared_by_address: _shared_by_address
		    })
		);

		num_records+=1;
		
		// log event
		RecordCreated(num_records, _description, _shared_with_fingerprint,
		    _shared_by_fingerprint, _shared_by_address);
		 
	}

    /*
	function pop_record() returns (uint _mrn, string _name) {
		require( patients.length > 0);
		_mrn = patients[patient_index[msg.sender]-1].mrn;
		_name = patients[patient_index[msg.sender]-1].name;
		patient_index[msg.sender] -=1;	
		
		patients_size -= 1;
	}
	*/

	// unlike pop_administration, get_administration retrieves a record 
	// by its row id number
	// argument _row starts from 0
	function get_record(uint _row) public returns (uint _id, string _description,
	    string _shared_by_fingerprint, string _shared_with_fingerprint,
	    address _shared_by_address) {
	    

		// note that this assumes that argument _id is equal to the row
		// max legal _row value is administrations.length
		
        require(_row>=0);
        require(_row < records.length);
        
		// if 'records' is empty, return null object
		if (records.length ==0 ) {
			_id = 0;
			_description="none";
			_shared_with_fingerprint="none";
			_shared_by_fingerprint="none";
			_shared_by_address=0x0;
			
		} else {	
		    _id = records[_row].id;
		    _description = records[_row].description;
		    _shared_with_fingerprint = records[_row].shared_with_fingerprint;
		    _shared_by_fingerprint = records[_row].shared_by_fingerprint;
		    _shared_by_address = records[_row].shared_by_address;
		}
	}

	function greet_omar(uint _i) public returns (string greeting) {
		require(_i>0);
		require(_i<greetings.length);
		return greetings[_i];
	}

	function die() public {
			if (msg.sender == owner) {
				suicide(owner);
			}
	}
}		

