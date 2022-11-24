import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import base64


# Creating Private Key of 1024 bits and Public Key

def rsakeys():  
     length=1024  
     privatekey = RSA.generate(length, Random.new().read)  
     publickey = privatekey.publickey()  
     return privatekey, publickey
 
 
# Encryption function which takes public key, plain text as arguments. 
# This function returns a base64 encoded string of ciphertext.

def encrypt(rsa_publickey,plain_text):
     encryptor = PKCS1_OAEP.new(rsa_publickey)
     cipher_text=encryptor.encrypt(plain_text.encode('utf-8'))
     b64cipher=base64.b64encode(cipher_text)
     return b64cipher.decode()
 
 
#  Decryption function that takes ciphertext and private key as arguments.

def decrypt(rsa_privatekey,b64cipher):
     decoded_ciphertext = base64.b64decode(b64cipher)
     decryptor = PKCS1_OAEP.new(rsa_privatekey)
     plaintext = decryptor.decrypt(decoded_ciphertext)
     return plaintext.decode('utf-8')
 
 
 

# privatekey,publickey = rsakeys() #generating keys
# msg = 4
# msg1 = str(msg)
# text=msg1   #"Hello Srikanth!" #Text to encrypt
# ct=encrypt(publickey,text)
# print(ct)
# print("len ", len(ct))
# print("type ", type(ct))

# print("##########")

# dct = decrypt(privatekey, ct.encode('utf-8'))
# print(dct)



# from cryptography.fernet import Fernet
# # Put this somewhere safe!

# def generate_key():
#      key = Fernet.generate_key()
#      f = Fernet(key)
#      return f

# def encrypt(key, msg):
#      token = key.encrypt(msg.encode('utf-8'))
#      return token.decode()
     

# def decrypt(key, ciphertext):
#      msg = key.decrypt(ciphertext)
#      return msg.decode('utf-8')

# key = generate_key()
# msg = str(5)
# ciphertext = encrypt(key, msg)
# #ci = ciphertext.encode('utf-8')
# print(ciphertext)
# origin = decrypt(key, ciphertext.encode('utf-8'))
# print(origin)