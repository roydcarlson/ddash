'''
:::  interface.py                                   :::
    ::: IPFS <> blockchain interface                :::
'''

import ipfsapi, os, json
from web3 import Web3, HTTPProvider, IPCProvider
from random import randint

# ipfs daemon needs to be running first


class Interface:

    # construct points to ddash contract address on blackswan Ethereum network
    # by default

    def __init__(self,host='localhost',port=5001):
        self.last_hash_added = None
        self.api = ipfsapi.connect(host='localhost',port=5001)
        self.web3 = Web3(HTTPProvider('http://localhost:8545'))
        self.blockNumber = self.web3.eth.blockNumber
        self.eth_accounts = self.web3.personal.listAccounts
        
        self.tx = {}

        print "Welcome to the DDASH interface manager."

    def load_contract(self,abi=None,sender_address="0xafc473881370c6be639ac259e6f36cdc86b6a778",contract_address="0xadb16223621e10d0864ff5df8d4ff5c686ca87bb"):

        self.tx['to'] = contract_address
        self.tx['from'] = sender_address

        if not abi:
            t = r"""[{"constant":false,"inputs":[{"name":"_row","type":"uint256"}],"name":"get_record","outputs":[{"name":"_id","type":"uint256"},{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_by_fingerprint","type":"string"},{"name":"_shared_with_fingerprint","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"die","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"seed","type":"uint256"}],"name":"randomGen","outputs":[{"name":"randomNumber","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_with_fingerprint","type":"string"},{"name":"_shared_by_fingerprint","type":"string"}],"name":"push_record","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_i","type":"uint256"}],"name":"greet_omar","outputs":[{"name":"greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_id","type":"uint256"},{"indexed":false,"name":"_ipfs_hash","type":"string"},{"indexed":false,"name":"_description","type":"string"},{"indexed":false,"name":"_shared_with_fingerprint","type":"string"},{"indexed":false,"name":"_shared_by_fingerprint","type":"string"}],"name":"RecordCreated","type":"event"}]"""

            json_abi = json.loads(t)
            self.contract = self.web3.eth.contract(abi=json_abi,address=contract_address)
            if self.contract: 
                print "You are now interfacing with contract at address "+contract_address



    def sanity_check(self):
        if not (self.api):
           print "I don't see IPFS running. Please make sure IPFS daemon is running first."
           return 1
        if not (self.blockNumber):
            print "I don't see geth running. Please run the go Ethereum client in the background."
            return 1
        if self.api and self.blockNumber:
            print "IPFS and geth appear to be running."
            return 0

    def random(self):
        assert(self.contract)
        assert(self.tx)

        i = randint(0,9)

        return self.contract.transact(self.tx).randomGen(i)

    def heyo(self):
        assert(self.contract)

        i = randint(0,4)
        print self.contract.call().greet_omar(i)
        return 0


    def upload(self,filepath):
        assert(os.path.isfile(filepath))
        assert(self.api)
        
        self.last_hash_added = result = self.api.add(filepath)
        if self.last_hash_added:
            print "'"+result['Name']+"' was uploaded to IPFS with hash:\n "+result['Hash']
            return result['Name'],result['Hash']

        print "Failed to upload file "+str(filepath)+" to IPFS"
        return 1


    def push_ipfs_hash_to_chain(self,ipfs_hash,description,sender_id,recipient_id):
        assert(self.contract)
        assert(self.tx)
        if not self.last_hash_added: 
            print "You must upload a file to IPFS first. Try Interface.upload(filepath)."
            return 1
        if not (ipfs_hash): 
            print "No IPFS hash specified. You must specify an IPFS hash to add to the blockchain."
            return 1
        if not (description):
            print "No description provided. You must describe the IPFS hash you're adding to the blockchain."
            return 1
        if not sender_id:
            print "No sender provided. You must specify a sender's pubkey id." 
            return 1
        if not recipient_id:
            print "No recipient provided. YOu must specify the recipient's pubkey id (if the resource is encrypted) or \'public\'."
            return 1

        tx_hash = self.contract.transact(self.tx).push_record(ipfs_hash,description,recipient_id,sender_id)

        print "New record added to blockchain. Object at IPFS hash "+ipfs_hash+" was shared with "+recipient_id+" by user "+sender_id+"."

        return tx_hash


