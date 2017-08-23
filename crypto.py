'''
:::  crypto.py 				:::
::: Easy keypair encryption/decryption  :::
::: Author:  Omar Metwally, MD		:::
::: omar.metwally@gmail.com		:::
::: MIT License				:::
'''

import gnupg

class User:
	""" Instantiate PGP user """
	
	def __init__(self, workdir='~/.gnupg'):
		self.gpg = gnupg.GPG(gnupghome=workdir)
		self.key = None
		self.users = {}

		return "DDASH working directory set to: "+workdir
	
	def create_user(alias,key_type="RSA",key_length=1024):
		self.input_data = gpg.gen_key_input(key_type, key_length)
		self.key = self.gpg.gen_key(input_data)

		self.users['alias'] = self.key
	def   



