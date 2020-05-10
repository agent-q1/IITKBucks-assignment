
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

input_text1 = input("Enter text ")
print(input_text1)

private_key = input("Enter path to private key")

key = RSA.import_key(open(private_key).read())

encrypted = key.encrypt(input_text1,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
      salt_length=padding.PSS.MAX_LENGTH
    ))

print(encrypted)
