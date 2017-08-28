var browser_blackswan_sol_blackswanContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_row","type":"uint256"}],"name":"get_record","outputs":[{"name":"_id","type":"uint256"},{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_by_fingerprint","type":"string"},{"name":"_shared_with_fingerprint","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"die","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"seed","type":"uint256"}],"name":"randomGen","outputs":[{"name":"randomNumber","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_ipfs_hash","type":"string"},{"name":"_description","type":"string"},{"name":"_shared_with_fingerprint","type":"string"},{"name":"_shared_by_fingerprint","type":"string"}],"name":"push_record","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_i","type":"uint256"}],"name":"greet_omar","outputs":[{"name":"greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_id","type":"uint256"},{"indexed":false,"name":"_ipfs_hash","type":"string"},{"indexed":false,"name":"_description","type":"string"},{"indexed":false,"name":"_shared_with_fingerprint","type":"string"},{"indexed":false,"name":"_shared_by_fingerprint","type":"string"}],"name":"RecordCreated","type":"event"}]);
var browser_blackswan_sol_blackswan = browser_blackswan_sol_blackswanContract.new(
           {
                    from: web3.eth.accounts[0], 
                         data: '0x606060405234156200001057600080fd5b5b33600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550600060018190555060006002819055506040805190810160405280601d81526020017f48692c206d79206e616d65206973204f6d6172204d657477616c6c792e00000081525060046000600681101515620000a957fe5b0160005b509080519060200190620000c3929190620002a0565b50606060405190810160405280602281526020017f4920616d207468652063726561746f72206f66207468697320636f6e7472616381526020017f742e000000000000000000000000000000000000000000000000000000000000815250600460016006811015156200013257fe5b0160005b5090805190602001906200014c929190620002a0565b506040805190810160405280601181526020017f426c61636b205377616e204c6976657321000000000000000000000000000000815250600460026006811015156200019457fe5b0160005b509080519060200190620001ae929190620002a0565b50606060405190810160405280603581526020017f5761746368696e67205061726e6173737573206f6e206120626561757469667581526020017f6c2c2073756e6e792064617920696e2053462e2e2e0000000000000000000000815250600460036006811015156200021d57fe5b0160005b50908051906020019062000237929190620002a0565b506040805190810160405280601c81526020017f4865616c74686361726520697320612068756d616e2072696768742e000000008152506004806006811015156200027e57fe5b0160005b50908051906020019062000298929190620002a0565b505b6200034f565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10620002e357805160ff191683800117855562000314565b8280016001018555821562000314579182015b8281111562000313578251825591602001919060010190620002f6565b5b50905062000323919062000327565b5090565b6200034c91905b80821115620003485760008160009055506001016200032e565b5090565b90565b610fc1806200035f6000396000f30060606040523615610076576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806310ea91421461007b57806335f4699414610266578063434b14e71461027b5780638da5cb5b146102b2578063a4f7693214610307578063f4b965701461042d575b600080fd5b341561008657600080fd5b61009c60048080359060200190919050506104ca565b6040518086815260200180602001806020018060200180602001858103855289818151815260200191508051906020019080838360005b838110156100ef5780820151818401525b6020810190506100d3565b50505050905090810190601f16801561011c5780820380516001836020036101000a031916815260200191505b50858103845288818151815260200191508051906020019080838360005b838110156101565780820151818401525b60208101905061013a565b50505050905090810190601f1680156101835780820380516001836020036101000a031916815260200191505b50858103835287818151815260200191508051906020019080838360005b838110156101bd5780820151818401525b6020810190506101a1565b50505050905090810190601f1680156101ea5780820380516001836020036101000a031916815260200191505b50858103825286818151815260200191508051906020019080838360005b838110156102245780820151818401525b602081019050610208565b50505050905090810190601f1680156102515780820380516001836020036101000a031916815260200191505b50995050505050505050505060405180910390f35b341561027157600080fd5b610279610942565b005b341561028657600080fd5b61029c60048080359060200190919050506109d6565b6040518082815260200191505060405180910390f35b34156102bd57600080fd5b6102c5610a1a565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561031257600080fd5b61042b600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050610a40565b005b341561043857600080fd5b61044e6004808035906020019091905050610d1f565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561048f5780820151818401525b602081019050610473565b50505050905090810190601f1680156104bc5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60006104d4610dfb565b6104dc610dfb565b6104e4610dfb565b6104ec610dfb565b600086101515156104fc57600080fd5b6000805490508610151561050f57600080fd5b60008080549050141561060557600094506040805190810160405280600481526020017f6e6f6e650000000000000000000000000000000000000000000000000000000081525093506040805190810160405280600481526020017f6e6f6e650000000000000000000000000000000000000000000000000000000081525092506040805190810160405280600481526020017f6e6f6e650000000000000000000000000000000000000000000000000000000081525090506040805190810160405280600481526020017f6e6f6e65000000000000000000000000000000000000000000000000000000008152509150610929565b60008681548110151561061457fe5b906000526020600020906005020160005b5060000154945060008681548110151561063b57fe5b906000526020600020906005020160005b506001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156106e45780601f106106b9576101008083540402835291602001916106e4565b820191906000526020600020905b8154815290600101906020018083116106c757829003601f168201915b505050505093506000868154811015156106fa57fe5b906000526020600020906005020160005b506002018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156107a35780601f10610778576101008083540402835291602001916107a3565b820191906000526020600020905b81548152906001019060200180831161078657829003601f168201915b505050505092506000868154811015156107b957fe5b906000526020600020906005020160005b506003018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156108625780601f1061083757610100808354040283529160200191610862565b820191906000526020600020905b81548152906001019060200180831161084557829003601f168201915b5050505050905060008681548110151561087857fe5b906000526020600020906005020160005b506004018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109215780601f106108f657610100808354040283529160200191610921565b820191906000526020600020905b81548152906001019060200180831161090457829003601f168201915b505050505091505b8484848385945094509450945094505b91939590929450565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614156109d357600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b5b565b6000600a60014303408360405180836000191660001916815260200182815260200192505050604051809103902060019004811515610a1157fe5b0690505b919050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008054806001018281610a549190610e0f565b916000526020600020906005020160005b60a06040519081016040528060018054018152602001888152602001878152602001868152602001858152509091909150600082015181600001556020820151816001019080519060200190610abc929190610e41565b506040820151816002019080519060200190610ad9929190610e41565b506060820151816003019080519060200190610af6929190610e41565b506080820151816004019080519060200190610b13929190610e41565b50505050600180600082825401925050819055507f87861418a5c83112bc84fe7031b6eb09fa52df791b229bddc3db9799373a54f1600154858585856040518086815260200180602001806020018060200180602001858103855289818151815260200191508051906020019080838360005b83811015610ba25780820151818401525b602081019050610b86565b50505050905090810190601f168015610bcf5780820380516001836020036101000a031916815260200191505b50858103845288818151815260200191508051906020019080838360005b83811015610c095780820151818401525b602081019050610bed565b50505050905090810190601f168015610c365780820380516001836020036101000a031916815260200191505b50858103835287818151815260200191508051906020019080838360005b83811015610c705780820151818401525b602081019050610c54565b50505050905090810190601f168015610c9d5780820380516001836020036101000a031916815260200191505b50858103825286818151815260200191508051906020019080838360005b83811015610cd75780820151818401525b602081019050610cbb565b50505050905090810190601f168015610d045780820380516001836020036101000a031916815260200191505b50995050505050505050505060405180910390a15b50505050565b610d27610dfb565b60008210151515610d3757600080fd5b600682101515610d4657600080fd5b600482600681101515610d5557fe5b0160005b508054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610dee5780601f10610dc357610100808354040283529160200191610dee565b820191906000526020600020905b815481529060010190602001808311610dd157829003601f168201915b505050505090505b919050565b602060405190810160405280600081525090565b815481835581811511610e3c57600502816005028360005260206000209182019101610e3b9190610ec1565b5b505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610e8257805160ff1916838001178555610eb0565b82800160010185558215610eb0579182015b82811115610eaf578251825591602001919060010190610e94565b5b509050610ebd9190610f28565b5090565b610f2591905b80821115610f2157600080820160009055600182016000610ee89190610f4d565b600282016000610ef89190610f4d565b600382016000610f089190610f4d565b600482016000610f189190610f4d565b50600501610ec7565b5090565b90565b610f4a91905b80821115610f46576000816000905550600101610f2e565b5090565b90565b50805460018160011615610100020316600290046000825580601f10610f735750610f92565b601f016020900490600052602060002090810190610f919190610f28565b5b505600a165627a7a7230582009dda443538b799c448fd22f4fbc37348219bf5c9f41ca926e4138b879d555cb0029', 
                              gas: '4300000'
                                     }, function (e, contract){
                                             console.log(e, contract);
                                                 if (typeof contract.address !== 'undefined') {
                                                              console.log('Contract mined! address: ' + contract.address + ' transactionHash: ' + contract.transactionHash);
                                                                  }
                                                  })