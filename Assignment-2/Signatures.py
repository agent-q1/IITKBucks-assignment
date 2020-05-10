from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from cryptography.fernet import Fernet

PublicKey = input("enter path to key")
unencrypted = input("enter unencrypted text")
encrypted = input("enter encrypted text")

file = open(PublicKey, 'rb')
key = file.read()
file.close()

f = Fernet(key)

decrypted = f.decrypt(encrypted)

if(unencrypted==decrypted):
    print("Signature verified")
else :
    print ("verification failed")
