
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os


def signe():
    message = (input('Veuillez entrer votre message : '))
    message = bytes(message, encoding='utf-8')
    key = RSA.import_key(open('private.key').read())
    h = SHA256.new(message)
    signer = pkcs1_15.new(key)
    signature = signer.sign(h)
    signature = signature

    file_out = open("signature.pem", "wb")
    file_out.write(signature)
    file_out.close()

    file_out = open("message.txt", "wb")
    file_out.write(message)
    file_out.close()
    return(os.getenv('public_k'))

    # return signature.hex()
print(signe())
