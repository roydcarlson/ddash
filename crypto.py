'''
:::  crypto.py 				:::
::: Easy keypair encryption/decryption  :::
::: Author:  Omar Metwally, MD		:::
::: omar.metwally@gmail.com		:::
::: MIT License				:::
'''

import gnupg
import os.path

class User:
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
		self.key = None
		self.users = {}

		# an identities.kc file (located in workdir) 
		# associates aliases with PGP pubkey fingerpints
		# check to see if one already exists on loading
		if os.path.isfile(self.identities_path): 
			with open(self.identities_path,'rb') as f:
				print "File identities.pkl found in: "+identities_path
				self.users = pickle.load(f)
                        print "Loaded user: \'"+self.users.keys()[0]

                if os.path.isfile(self.keypair_path):
                    key_data = open('mykeyfile.asc').read()
                    import_result = gpg.import_keys(key_data)

		    print "Loaded keypair file \'keypair.asc\'"

        	
	def new_keypair(alias,key_type="RSA",key_length=1024):
		self.input_data = gpg.gen_key_input(key_type, key_length)
		self.key = self.gpg.gen_key(input_data)

		self.users[alias] = self.key
		self.save_user()

                return "Created user with pubkey fingerprint: "+self.users['alias']

	# method save_user saves an asc file to disk
	# and pickles the identities dict populated with 
	# (key,value) = (alias,pubkey fingerprint)
	def save_user():
		ascii_armored_public_keys = self.gpg.export_keys(str(self.key))
		ascii_armored_private_keys = self.gpg.export_keys(str(self.key),True) 
                with open(self.keypair_path,'w') as f:
                    f.write(ascii_armored_public_keys)
                    f.write(ascii_armored_private_keys)

		with open(self.identities_path,'wb') as f:
			pickle.dump(self.users,f,pickle.HIGHEST_PROTOCOL)

	def key_found():
		public_keys = gpg.list_keys()
		if len(public_keys) ==0:
			
			
