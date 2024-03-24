

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
import gmpy2
import sympy

with open("flag1.pem", 'rb') as f:
    c = f.read()
c=libnum.s2n(c)
with open("pubckey1.pem", 'rb') as f:
    key = f.read()
rsakey = RSA.importKey(key)
n= rsakey.n
e= rsakey.e
p1=libnum.nroot(n,2)
p=gmpy2.next_prime(p1)
q=sympy.prevprime(p)
print(n==p*q)
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m=pow(c,d,n)
print(libnum.n2s(int(m)))
