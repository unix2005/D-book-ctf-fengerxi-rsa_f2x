from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
import gmpy2

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
print(p)
print(q)
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
flag = b'flag{01d80670b01b654fe4831a3e81870734}'
m = libnum.s2n(flag)

#
# 生成公钥
rsa_components = (int(n), int(e))
keypair = RSA.construct(rsa_components)
with open('pubckey.pem', 'wb') as f:
    f.write(keypair.exportKey())

rsa_components = (int(n), e,)
arsa = RSA.construct(rsa_components)
rsakey = RSA.importKey(arsa.exportKey())
rsakey = PKCS1_OAEP.new(rsakey)
c = rsakey.encrypt(flag)
print(c)
with open("flag.pem", "wb") as f:
    f.write(c)
