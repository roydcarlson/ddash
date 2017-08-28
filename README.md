# Distributed Data Sharing Hyperledger (DDASH)
Omar Metwally, MD
UCSF Medical Center, Department of Clinical Informatics
---
## Description
DDASH is a distributed networking permissions manager running on the Interplanetary File System ([IPFS](https://github.com/ipfs/ipfs)) and [Ethereum](https://www.ethereum.org). It utilizes the web3.py and ipfsapi python modules, among others.

## Why DDASH?
The majority of produced and hosted by academic institutions, hospitals, and corporations is completely un-utilized. DDASH is an emerging protocol for sharing data on the distributed IPFS network and storing permissions on the Ethereum blockchain. In its usual siloed state, data is a liability rather than an asset, requiring increasing energy to maintain and secure as an organization's data grows. 
DDASH turns data into digital assets. Data hosted on the IPFS network takes a life of its own. No longer bound to a single machine, it travels through all network nodes, is effectively indestructable, and can be accessed nearly instantaneously. Permissions are managed via Pretty Good Privacy (OpenPGP) keypair encryption and stored on the Ethereum blockchain. Network participants are rewarded with cryptographic tokens to incentivize 

Our goals are to:

1. Break down all barriers to information exchange within and among organizations.
2. Provide granular control over who can access distributed data
3. Create economies around digital assets to incentivize responsible and effective data sharing.

## Ethereum network
DDASH currently runs on the **blackswan** private Ethereum network at 104.236.141.200.

## Getting Started
Make sure you have the [Go Ethereum client](https://github.com/ethereum/go-ethereum) installed on your UNIX machine. The instructions here are for machines running Ubuntu 16.04.

Start by creating these directories in your root directory:
```
mkdir /root/blackswan
mkdir /root/blackswan/data
```

To connect to the blackswan network, you'll need to use the same genesis block defined in *genesis.json*. Move this file to `/root/blackswan` and set your genesis block (you only need to do this once):
```
cd /root/blackswan/data
geth --datadir=/root/blackswan/data init /root/blackswan/genesis.json
bootnode --genkey=boot.key
bootnode --nodekey=boot.key 
```

In order to use the web3py and ipfs wrappers, you'll need to run *geth* and ipfs daemons in the background, respectively:
```
geth --verbosity 1 --datadir /root/blackswan/data --networkid 4828 --port 30303 --rpcapi="db,eth,net,web3,personal,web3" --rpc 104.236.141.200 --rpcport 8545  console 
```
The above command starts the go Ethereum client on your local machine and attempts to connect to the blackswan server at 104.236.141.200. Remember to set your genesis block according to the above directions. Trying to join this network with a different genesis block (such as the default genesis block) will not work.

Then open a new terminal window or tab and start the ifps daemon:
```
ipfs daemon
```

### Examples
In this example, we'll use the Python web3 object (analogous to web3.js) to interact with the private Ethereum network called *blackswan*. Make sure you have geth and ipfs running (see above). Start by opening a Python interactive shell and try:
```
from web3 import Web3, HTTPProvider, IPCProvider
import json

web3 = Web3(HTTPProvider('http://localhost:8545')
web3.eth.blockNumber
web3.personal.listAccounts

# to create account:  web3.personal.newAccount('your-passphrase')

web3.personal.unlockAccount('0x000youraccountaddress','your-passphrase')

t = r"""[{"constant":false,"inputs":[{"name":"_row","type":"uint256"}],"name":"get_record","outputs":[{"name":"_id","type":"uint256"},{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_by_fingerprint","type":"string"},{"name":"_shared_with_fingerprint","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"die","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"seed","type":"uint256"}],"name":"randomGen","outputs":[{"name":"randomNumber","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_with_fingerprint","type":"string"},{"name":"_shared_by_fingerprint","type":"string"}],"name":"push_record","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_i","type":"uint256"}],"name":"greet_omar","outputs":[{"name":"greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_id","type":"uint256"},{"indexed":false,"name":"_ipfs_hash","type":"string"},{"indexed":false,"name":"_description","type":"string"},{"indexed":false,"name":"_shared_with_fingerprint","type":"string"},{"indexed":false,"name":"_shared_by_fingerprint","type":"string"}],"name":"RecordCreated","type":"event"}]"""

json_abi = json.loads(t)
address = web3.eth.accounts[0]
tx = {}
tx['to'] = "0xadb16223621e10d0864ff5df8d4ff5c686ca87bb"  # ddash contract address on the blackswan private network
tx['from'] = web3.eth.accounts[0]

contract = web3.eth.contract(abi=json_abi,address=address)
contract.call().greet_omar(0)  #called locally; does not interact with blockchain
contract.transact(tx).greet_omar(0) # interacts with blockchain by broadcasting transaction; greet_omar(0 -> 4) is valid

contract.transact(tx).push_record("ipfshash","description","sender_pubkey_fingerprint","recipient_pubkey_fingerprint")

contract.call().get_record(0)  # retrieve record by row number
```
The above code block demonstrates how to execute a simple contract method (greet_omar), add a record (push_record), and retrieve a record(get_record). Note the difference between locally calling a method (using call().method()) and sending a transaction to the blockchain (contract.transact(tx).push_record(...)).


