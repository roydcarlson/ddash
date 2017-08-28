# Distributed Data Sharing Hyperledger (DDASH)

             _____  _____           _____ _    _ 
            |  __ \|  __ \   /\    / ____| |  | |
            | |  | | |  | | /  \  | (___ | |__| |
            | |  | | |  | |/ /\ \  \___ \|  __  |
            | |__| | |__| / ____ \ ____) | |  | |
            |_____/|_____/_/    \_\_____/|_|  |_|
                                             

:earth_americas: :rocket: :boom: :rocket: :earth_asia: :boom: :rocket: :boom: :earth_africa: :rocket: :boom: :rocket: :earth_americas:

Copyright (C) 2017  [Omar Metwally, MD](https://omarmetwally.wordpress.com) 

Twitter: [@osmode](https://www.twitter.com/osmode)

Email: [omar.metwally@gmail.com](mailto:omar.metwally@gmail.com)

UCSF Medical Center, Department of Clinical Informatics


---
## What is DDASH?
DDASH is a distributed networking permissions manager that inferfaces between the Interplanetary File System ([IPFS](https://github.com/ipfs/ipfs)) and the [Ethereum](https://www.ethereum.org) blockchain. 

## Why DDASH?
Despite the wealth of data produced by academic institutions, research labs, hospitals, and companies, only a small percentage of data is used to its fullest potential. DDASH is an emerging protocol for sharing data on the distributed IPFS network and storing permissions on the Ethereum blockchain. 

###In its usual siloed state, data is a liability rather than an asset.

*DDASH turns data into digital assets.*

No longer confined to a single machine, data hosted on the IPFS network flows perputually through network nodes, rendering it indestructable and instantly accessible. Permissions are managed via PGP keypair encryption and stored on the Ethereum blockchain. Network participants are rewarded with cryptographic tokens to incentivize effective data sharing and utilization and growth of the network.

Our goals are to:

1. Break down all barriers to information exchange within and among organizations.
2. Provide granular control over who can access distributed data
3. Create economies around digital assets to incentivize effective data sharing.

## Ethereum network
DDASH currently runs on the *blackswan* private Ethereum network at 104.236.141.200.

## Prerequisites
This project is built on [IPFS](https://github.com/ipfs/ipfs), [Ethereum](https://www.ethereum.org), [OpenPGP](https://www.openpgp.org), [web3.py](https://github.com/pipermerriam/web3.py), [py-ipfs](https://github.com/ipfs/py-ipfs-api). 

## License
MIT License (see *LICENSE* file above).

## Getting Started
Make sure you have the [Go Ethereum client](https://github.com/ethereum/go-ethereum) installed on your machine, and install the *web3.py* and *py-ipfs* Python packages. The instructions here are for machines running Ubuntu 16.04. [This tutorial](https://omarmetwally.wordpress.com/2017/07/25/how-to-create-a-private-ethereum-network/) covers basic Ethereum networking.

Start by creating these directories in your root directory:
```
mkdir /root/blackswan
mkdir /root/blackswan/data
```

To connect to the *blackswan* network, you'll need to use the same genesis block defined in *genesis.json*. Move this file to `/root/blackswan` and set your genesis block (you only need to do this once, and you need to install the Ethereum go client *geth* and Ethereum developer tools first):
```
cd /root/blackswan/data
geth --datadir=/root/blackswan/data init /root/blackswan/genesis.json
bootnode --genkey=boot.key
bootnode --nodekey=boot.key 
```

In order to use the *web3.py* and *ipfs* wrappers, you'll need to run *geth* and ipfs daemons in the background, respectively:
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
The above code block demonstrates how to execute a simple contract method (greet_omar), add a record (push_record), and retrieve a record(get_record). Note the difference between locally calling a method (using *call().method()*) and sending a transaction to the blockchain (*contract.transact(tx).push_record(...)*)

## Adding files to the IPFS network
Make sure you already have *geth* and *ipfs* daemons running, and start an interactive python shell. In this example, we'll add *experimentData.csv* to the distributed IPFS network via:
```
import ipfsapi
api = ipfsai.connect()
api.add('/path/to/experimentData.csv')
 {'Hash':'QmRmE1vnc7mbEiqQv5SjrW3ctAmXXt4MQqbykenJmSqPuk', 'Name':'experimentData.csv'}
```
You can access your *experimentData.csv* file by copy-pasting this URL in your web browser:
```
ipfs.io/QmRmE1vnc7mbEiqQv5SjrW3ctAmXXt4MQqbykenJmSqPuk
```

We will use the private *blackswan* blockchain to let the world know that you shared this file with the world:


```
contract.transact(tx).push_record("QmRmE1vnc7mbEiqQv5SjrW3ctAmXXt4MQqbykenJmSqPuk","Data from Phase I Clinical Trial","08-3983-1398","public")
```

## Mining on the *blackswan* Ethereum network
Mining difficulty is currently very easy (0x00001) on the blackswan network. Go ahead and make a few million Ether by running:
```
geth --verbosity 4 --datadir /Users/breitkopf/Desktop/blackswan/data --networkid 4828 --port 30303 --rpc 104.236.141.200 --rpcport 8545  --mine console
```

## Permissions management 
Data on the IPFS network cannot be removed and can be accessed by anyone who has your content hash. DDASH utilizes PGP keypair encryption to control permissions. The above examples demonstrated how to share data at IPFS address *QmRmE1vnc7mbEiqQv5SjrW3ctAmXXt4MQqbykenJmSqPuk*. If I only want Steven to be able to view the contents of this file, I'll create a directory named after his public key ID, encrypt the file using Steven's public key, and add it to the directory named after his pubkey. Finally I'll upload entire directory to IPFS and add the resulting hashes to the *blackswan* blockchain.

```
# set up your working directory
import gnupg
workdir = '/ddash'
gpg = gnupg.GPG(gnupghome=workdir)

# list PGP keys on your machine
gpg.list_keys()  

# create PGP key
input_data = gpg.gen_key_input(key_type="RSA",key_length=1024)
key = gpg.gen_key(input_data)
print key

# save keypair to file *mykeyfile.asc* 
ascii_armored_public_keys  = gpg.export_keys(str(key))
ascii_armored_private_keys = gpg.expoert_keys(str(key),True)
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)

# save public key to public PGP server
gpg.send_keys('pgp.mit.edu',key.fingerprint)

# receive key from keyserver
import_result = gpg.recv_keys('pgp.mit.edu',key.fingerprint)
gpg.list_keys()

# list keys
gpg = gnupg.GPG(gnupghome=workdir)
public_keys = gpg.list_keys(c_keys = gpg.list_keys()
public_fingerprint = public_keys[0]['fingerprint']
private_keys = gpg.list_keys(True)
print 'public keys:'
pprint(public_keys)
print 'private keys:'
pprint(private_keys))

# import keys from local file
key_data = open('mykeyfile.asc').read()
import_result = gpg.import_keys(key_data)
print import_result.results

# encrypt file using a public key fingerprint
encrypted_file_path = workdir+'/stevens_pubkey_id/my-encrypted-file.gpg'

with open('/path/to/experimentData.csv','rb') as f:
    status = gpg.encrypt_file(
    f, recipients=[public_fingerprint],
    output=encrypted_file_path) 

    print 'ok: ', status.ok
    print 'status: ', status.status
    print 'stderr: ', status.stderro

# decrypt file
decrypted_file_path = '/Users/steven/Desktop/decrypted'
decrypted_file_path += '/my-decrypted-file.gpg'

with open(encryped_file_path, 'rb') as f:
    status = gpg.decrypt_file(f,
    output = decrypted_file_path)

    print 'ok: ',status.ok
    print 'status:', status.status
    print 'stderr: ',status.stderr
```

## Contribute
---
### Use cases
I envisioned DDASH as a better way for medical and life science researchers to collaborate and share data. If you or your organization use DDASH to do something that would otherwise be impossible using a distributed system, please share your experience and help others learn how they could do the same! 

### Bug reports
You can submit bug reports using the [GitHub issue tracker](https://github.com/osmode/ddash/issues).

### Pull requests
Pull requests are welcome.

### Miners
The strength of a distributed network lies in distributed computing power. You can strengthen the DDASH network by running a *blackswan* network node. See above for details.


