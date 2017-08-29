'''
:::  crypto.py 				        :::
::: Easy gnupg keypair encryption/decryption    :::
::: Author:  Omar Metwally, MD		        :::
::: omar.metwally@gmail.com		        :::
::: MIT License				        :::
'''

import gnupg
import os.path

class PGPUser:
	""" Instantiate PGP user """
	
	"""
	.. function:: __init__(self, workdir)
	:workdir is the working directory and must be set
	"""
	def __init__(self, workdir='/gnupg'):
		self.workdir = workdir
		self.identities_filename = "identity.pkl"
                self.keypair_filename = "keypair.asc"
		self.identities_path = self.workdir+'/'+self.identities_filename
                self.keypair_path = self.workdir+'/'+self.keypair_filename
		self.gpg = gnupg.GPG(gnupghome=workdir)
		self.keys = []
                self.key_index = 0

        	
        # check if PGP keys present on machine
        def check_keys(self):
           self.keys = self.gpg.list_keys()
           if len(self.keys) > 0: 
               print "The following PGP keys were found: "
               for index,key in enumerate(self.keys):
                   print "key "+str(index)+": "+key['keyid'] 
               return self.keys
           print "No PGP keys were found."
           return 1

        # choose which PGP key to use
        def set_key(self,index):
            assert(len(self.keys) >0)
            assert(index < len(self.keys))

            self.key_index = index
            print "You're now using keyid "+str(self.keys[self.key_index])

        def delete_key(self,index):
            assert(len(self.keys) > 0)
            assert(index < len(self.keys))

            fp = self.keys[index]['fingerprint']
            print str(self.gpg.delete_keys(fp,True))  # delete private key
            print str(self.gpg.delete_keys(fp))       # delete pubkey
        

        def load_profile(self):
		# an identities.kc file (located in workdir) 
		# associates aliases with PGP pubkey fingerpints
		# check to see if one already exists on loading
		if os.path.isfile(self.identities_path): 
			with open(self.identities_path,'rb') as f:
			    print "File identities.pkl found in: "+identities_path
                            pass
			    # self.users = pickle.load(f)
                        
                        # print "Loaded user: \'"+self.users.keys()[0]
                        import_result =self.gpg.recv_keys('pgp.mit.edu',self.keys[self.key_index]['fingerprint'])

                if os.path.isfile(self.keypair_path):
                    key_data = open(self.keypair_path).read()
                    import_result = self.gpg.import_keys(key_data)

		    print "Loaded keypair file \'keypair.asc\'"


                return True



	def new_keypair(self,key_type="RSA",key_length=1024):
		input_data = self.gpg.gen_key_input(key_type=key_type, key_length=key_length)
		self.key = self.gpg.gen_key(input_data)

		self.save_user()

                print "New PGP key created: "+str(self.key) 

	# method save_user saves an asc file to disk
	# and pickles the identities dict populated with 
	# (key,value) = (alias,pubkey fingerprint)
        # it also uploads the pubkey to a public keyserver
	def save_user(self):
		ascii_armored_public_keys = self.gpg.export_keys(str(self.keys[self.key_index]))
		ascii_armored_private_keys = self.gpg.export_keys(str(self.keys[self.key_index]),True) 
                with open(self.keypair_path,'w') as f:
                    f.write(ascii_armored_public_keys)
                    f.write(ascii_armored_private_keys)

                '''
		with open(self.identities_path,'wb') as f:
			pickle.dump(self.users,f,pickle.HIGHEST_PROTOCOL)
                '''

                self.gpg.send_keys('pgp.mit.edu',self.keys[self.key_index]['fingerprint'])
