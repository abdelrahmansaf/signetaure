from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def verify():
    key = RSA.import_key(open('public.key').read())
    file_in = open("message.txt", "rb")
    message = file_in.read()
    file_in.close()

    file_in = open("signature.pem", "rb")
    signature = file_in.read()
    file_in.close()
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return ("True")
    except (ValueError, TypeError):
        return ("False")
