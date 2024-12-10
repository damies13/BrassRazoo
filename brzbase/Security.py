
from builtins import bytes
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Security:

	key_size = 8192

	#
	# souce inspiration for password encrypting and decrypting data:
	# https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python
	#

	def encrypt(self, string, password):
		"""
		It returns an encrypted string which can be decrypted just by the
		password.
		"""
		key = self.password_to_key(password)
		IV = self.make_initialization_vector()
		encryptor = AES.new(key, AES.MODE_CBC, IV)

		# store the IV at the beginning and encrypt
		return IV + encryptor.encrypt(self.pad_string(string))

	def decrypt(self, string, password):
		key = self.password_to_key(password)

		# extract the IV from the beginning
		IV = string[:AES.block_size]
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		string = decryptor.decrypt(string[AES.block_size:])
		return self.unpad_string(string)

	def password_to_key(self, password):
		"""
		Use SHA-256 over our password to get a proper-sized AES key.
		This hashes our password into a 256 bit string.
		"""
		return SHA256.new(password).digest()

	def make_initialization_vector(self, ):
		"""
		An initialization vector (IV) is a fixed-size input to a cryptographic
		primitive that is typically required to be random or pseudorandom.
		Randomization is crucial for encryption schemes to achieve semantic
		security, a property whereby repeated usage of the scheme under the
		same key does not allow an attacker to infer relationships
		between segments of the encrypted message.
		"""
		return Random.new().read(AES.block_size)

	def pad_string(self, string, chunk_size=AES.block_size):
		"""
		Pad string the peculirarity that uses the first byte
		is used to store how much padding is applied
		"""
		assert chunk_size  <= 256, 'We are using one byte to represent padding'
		to_pad = (chunk_size - (len(string) + 1)) % chunk_size
		return bytes([to_pad]) + string + bytes([0] * to_pad)

	def unpad_string(self, string):
		to_pad = string[0]
		return string[1:-to_pad]

	# def encode(self, string):
	# 	"""
	# 	Base64 encoding schemes are commonly used when there is a need to encode
	# 	binary data that needs be stored and transferred over media that are
	# 	designed to deal with textual data.
	# 	This is to ensure that the data remains intact without
	# 	modification during transport.
	# 	"""
	# 	return base64.b64encode(string).decode("utf-8")
	#
	# def decode(self, string):
	# 	return base64.b64decode(string.encode("utf-8"))
	#


	#
	# souce inspiration for digital signatures:
	# https://dev.to/u2633/the-flow-of-creating-digital-signature-and-verification-in-python-37ng
	#

	def generate_keys(self):
		# Generate a Key Pair
		# Generate private key
		keys = {}

		keys["private"] = rsa.generate_private_key(
		    public_exponent=65537,
			key_size=self.key_size,
		)

		# Generate public key from the private key
		keys["public"] = keys["private"].public_key()

		return keys

	def sign_string(self, instring, private_key):

		# Message to be signed
		# message = b"Hello, this is a secret message!"

		# Sign the message
		signature = private_key.sign(
			instring,
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
			),
			hashes.SHA256()
		)

		return signature

	def verify_string_signature(self, instring, signature, public_key):
		# Message to be verified
		message = b"Hello, this is a secret message!"

		# Verify the signature
		try:
			public_key.verify(
				signature,
				instring,
				padding.PSS(
					mgf=padding.MGF1(hashes.SHA256()),
					salt_length=padding.PSS.MAX_LENGTH
				),
				hashes.SHA256()
			)
			print("The signature is valid.")
			return True
		except:
		    print("The signature is invalid.")
			return False





#
