# Distributed Data Sharing Hyperledger (DDASH)

             _____  _____           _____ _    _ 
            |  __ \|  __ \   /\    / ____| |  | |
            | |  | | |  | | /  \  | (___ | |__| |
            | |  | | |  | |/ /\ \  \___ \|  __  |
            | |__| | |__| / ____ \ ____) | |  | |
            |_____/|_____/_/    \_\_____/|_|  |_|
                                             

:earth_americas: :rocket: :boom: :rocket: :earth_asia: :boom: :rocket: :boom: :earth_africa: :rocket: :boom: :rocket: :earth_americas:


## What is DDASH?
---
DDASH is a distributed networking permissions manager that inferfaces between the Interplanetary File System ([IPFS](https://github.com/ipfs/ipfs)) and the [Ethereum](https://www.ethereum.org) blockchain. 

## Why DDASH?
---
Despite the wealth of data produced by academic institutions, research labs, hospitals, and companies, only a small percentage of data is used to its fullest potential. DDASH is an emerging protocol for sharing data on the distributed IPFS network and storing permissions on the Ethereum blockchain. 

### In its usual siloed state, data is a liability rather than an asset.

### *DDASH turns data into digital assets.*

No longer confined to a single machine, data hosted on the IPFS network flows perputually through network nodes, rendering it persistent and rapidly accessible. Permissions are managed via PGP keypair encryption and stored on the Ethereum blockchain. Network participants are rewarded with cryptographic tokens to incentivize generation and dissemination of knowledge, effective data sharing, and growth of the network.

Our goals are to:

1. Eliminate barriers to information exchange within and among organizations.
2. Provide granular permission control.
3. Build economies around knowledge and information

## Ethereum network
---
DDASH currently runs on the *blackswan* private Ethereum network at 104.236.141.200.

## Prerequisites
---
This project is built on awesome work by the [IPFS](https://github.com/ipfs/ipfs), [Ethereum](https://www.ethereum.org), [OpenPGP](https://www.openpgp.org), [web3.py](https://github.com/pipermerriam/web3.py), and [py-ipfs](https://github.com/ipfs/py-ipfs-api) communities. 

## Precautions
The technologies used here are still in alpha. If you own cryptoassets such as Bitcoin and Ether, make sure you keep these on a completely separate machine. This software is being developed for academic purposes, is still in development, and has not been audited for security.

## Getting Started
---
You should have the [Go Ethereum client](https://github.com/ethereum/go-ethereum) installed on your machine, and install the *web3.py* and *py-ipfs* Python packages. The instructions here are for machines running Ubuntu 16.04. [This tutorial](https://omarmetwally.wordpress.com/2017/07/25/how-to-create-a-private-ethereum-network/) covers basic Ethereum networking.

You will need an Ethereum node connected to the blackswan private network and the ability to lock/unlock this account to send transactions.

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
Be very careful when enabling RPC while your accounts are unlocked. This can lead to Ethereum wallet attacks, hence the warning above about keeping your development environment completely separate from any real Ether you might own.

The above command starts the go Ethereum client on your local machine and attempts to connect to the blackswan server at 104.236.141.200. Remember to set your genesis block according to the above directions. Trying to join this network with a different genesis block (such as the default genesis block) will not work.

Then open a new terminal window or tab and start the ifps daemon:
```
ipfs daemon
```

### DDASH command line interface
Once your Ethereum and IPFS nodes are running, your account is unlocked, and you can interact with both clients, start the DDASH command line interface (CLI):

```
python main.py

        _____  _____           _____ _    _ 
       |  __ \|  __ \   /\    / ____| |  | |
       | |  | | |  | | /  \  | (___ | |__| |
       | |  | | |  | |/ /\ \  \___ \|  __  |
       | |__| | |__| / ____ \ ____) | |  | |
       |_____/|_____/_/    \_\_____/|_|  |_|
                                                                
    ::: Distributed Data Sharing Hyperledger :::
    Copyright (C) 2017 Omar Metwally, MD
                                                                         omar.metwally@gmail.com
                                                                         Welcome to the DDASH Command Line Interface.


[1]  ddash> new key
[2]  ddash> show keys
        ...
[3]  ddash> use key 0
[4]  ddash> set recipient your_recipient's_pubkey_id 
[5]  ddash> set file /path/to/clinical/trial/data.csv
[6]  ddash> encrypt
[7]  ddash> upload
```
The above commands 
[1]  generate a new PGP keypair 
[2]  list all PGP keypairs on your machine
[3]  uses the first (index 0) keypair as your identity
[4]  specifies an intended recipient's public key
[5]  specifies file you want to upload to IPFS
[6]  encrypts the file using recipient's public key fingerprint
[7]  uploads the file to IPFS and creates transaction containing the hash, user id of the person who uploaded the file, and recipient's public key id (or "public" indicating that it's not encrypted).



## Mining on the *blackswan* Ethereum network
---
Mining difficulty is currently very easy (0x00001) on the blackswan network. Go ahead and make a few million Ether by running:
```
geth --verbosity 4 --datadir /Users/breitkopf/Desktop/blackswan/data --networkid 4828 --port 30303 --rpc 104.236.141.200 --rpcport 8545  --mine console
```

## Permissions management 
Data on the IPFS network cannot be removed and can be accessed by anyone who has your content hash. DDASH utilizes PGP keypair encryption to control permissions. The above examples demonstrated how to share data at IPFS address *QmRmE1vnc7mbEiqQv5SjrW3ctAmXXt4MQqbykenJmSqPuk*. If I only want Steven to be able to view the contents of this file, I'll create a directory named after his public key ID, encrypt the file using Steven's public key, and add it to the directory named after his pubkey. Finally I'll upload entire directory to IPFS and add the resulting hashes to the *blackswan* blockchain.

## Contribute
---
### Use cases
If you or your organization use DDASH to do something that would otherwise be impossible using a centralized system, please share your experience!

### Bug reports
You can submit bug reports using the [GitHub issue tracker](https://github.com/osmode/ddash/issues).

### Pull requests
Pull requests are welcome.

### Miners
The strength of a distributed network lies in distributed computing power. You can strengthen the DDASH network by running a *blackswan* network node (and earn crytographic tokens in return). See above for details.


## License
MIT License (see *LICENSE* file for details).


