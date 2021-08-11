from Crypto.PublicKey import RSA
import os


key = RSA.generate(2048)
private_key = key.export_key()

file_out = open("private.key", "wb")
file_out.write(private_key)
file_out.close()
file_in = open("private.key")
private_key = file_in.read()


pub_key = key.publickey().export_key()
file_out = open("public.key", "wb")
file_out.write(pub_key)
file_out.close()
f = open("public.key")
public_key = f.read()


os.environ["public_k"] = public_key
os.environ["private_k"] = private_key
f.close()
file_out.close()

print(os.environ["private_k"])
print(os.environ["public_k"])
