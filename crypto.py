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
		self.identities_path = self.workdir+'/'+self.identities_filename
		self.gpg = gnupg.GPG(gnupghome=workdir)
		self.key = None
		self.users = {}

		# an identities.kc file (located in workdir) 
		# associates aliases with PGP pubkey fingerpints
		# check to see if one already exists on loading
		if os.path.isfile(identities_path): 
			with open(identities_path,'rb') as f:
				print "File identities.pkl found in: "+identities_path
				self.users = pickle.load(f)
				return self.users

		return "No identities found. Create an identity using the create_user method."
	
	def create_user(alias,key_type="RSA",key_length=1024):
		self.input_data = gpg.gen_key_input(key_type, key_length)
		self.key = self.gpg.gen_key(input_data)

		self.users['alias'] = self.key
		self.save_user()

	def save_user():
		with open(self.identities_path,'wb') as f:
			pickle.dump(self.users,f,pickle.HIGHEST_PROTOCOL)

	def key_found():
		public_keys = gpg.list_keys()
		if len(public_keys) ==0:
			
			
