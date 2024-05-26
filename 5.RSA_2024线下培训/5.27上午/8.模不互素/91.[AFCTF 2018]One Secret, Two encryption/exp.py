from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
import gmpy2
import sympy
with open("flag_encry1","rb") as f:
    c1=libnum.s2n(f.read())

with open("public1.pub", 'rb') as f:
    key1 = f.read()

with open("public2.pub", 'rb') as f:
    key2 = f.read()
rsakey1= RSA.importKey(key1)
rsakey2= RSA.importKey(key2)

n1= rsakey1.n
e1= rsakey1.e
n2= rsakey2.n
e2= rsakey2.e
print(e1)
print(e2)

p=libnum.gcd(n1,n2)
q1=n1//p
phi1=(p-1)*(q1-1)
d1=libnum.invmod(e1,phi1)
m1=pow(c1,d1,n1)
print(libnum.n2s(m1))
