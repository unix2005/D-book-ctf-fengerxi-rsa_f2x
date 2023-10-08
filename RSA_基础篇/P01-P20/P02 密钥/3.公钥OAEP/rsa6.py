from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
import gmpy2
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
flag = flag.encode()

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)

#
# 生成公钥
rsa_components = (int(n), int(e), int(d))
keypair = RSA.construct(rsa_components)
with open('prikey2.pem', 'wb') as f:
    f.write(keypair.exportKey())

rsa_components = (int(n), e,)
arsa = RSA.construct(rsa_components)
rsakey = RSA.importKey(arsa.exportKey())
rsakey = PKCS1_OAEP.new(rsakey)
c = rsakey.encrypt(flag)
with open("flag2.pem", "wb") as f:
    f.write(c)
