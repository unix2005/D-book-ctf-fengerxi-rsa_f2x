from Crypto.PublicKey import RSA
import libnum
import gmpy2
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = libnum.s2n(flag)
c = pow(m, e, n)
#
c1 = libnum.n2s(int(c))

with open("flag1.pem", "wb") as f:
    f.write(c1)
# 生成公钥
rsa_components = (int(n), int(e))
keypair = RSA.construct(rsa_components)
with open('pubckey1.pem', 'wb') as f:
    f.write(keypair.exportKey())
