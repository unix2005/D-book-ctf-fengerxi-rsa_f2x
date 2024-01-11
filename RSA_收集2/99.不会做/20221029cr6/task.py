from Crypto.Util.number import *
from gmpy2 import *
from random import *
from secret import flag

m=bytes_to_long(flag)
assert len(bin(m))-2<500
p=getPrime(1024)
q=getPrime(1024)
d=getPrime(1024)
n=p*q
phi=(p-1)*(q-1)


e1=getrandbits(1024)
e2=getrandbits(1024)
while True:
    try:
        D=invert(e2,phi)
        break
    except:
        e2=getrandbits(1024)
enc=pow(m,D,n)


c1=pow(enc+d,e1,n)
c2=pow(enc+d,e1*2,n)
c3=pow(enc+d,e1*3,n)
c4=pow(enc+2*d,D,n)
c5=pow(d,5,n)


print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c3 = {c3}")
print(f"c4 = {c4}")
print(f"c5 = {c5}")
print(f"e2 = {e2}")
