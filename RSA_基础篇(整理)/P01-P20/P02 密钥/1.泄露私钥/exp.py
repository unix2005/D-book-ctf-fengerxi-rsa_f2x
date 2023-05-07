from Crypto.PublicKey import RSA
import libnum
with open("flag.pem", 'rb') as f:
    c = int(f.read().hex(),16)

with open("pubckey.pem", 'rb') as f:
    key = f.read()

rsakey = RSA.importKey(key)
# print(rsakey)

d = rsakey.d
n = rsakey.n
m = pow(c,d,n)
print(libnum.n2s(m))
# flag{947ce8a3-40ee-46c0-a00e-0026e583f8da}