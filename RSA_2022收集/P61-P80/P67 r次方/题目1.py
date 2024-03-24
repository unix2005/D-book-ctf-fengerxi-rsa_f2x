
import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
from Crypto.Util.number import *


r = getRandomNBitInteger(64)
print("r=",r)
p = r**5 + r**4 - r**3 + r**2 - r + 2023
q = r**5 - r**4 + r**3 - r**2 + r + 2023
p = gmpy2.next_prime(p)
q = gmpy2.next_prime(q)
n = p*q
e=65537

c=pow(m,e,n)
print("p=",p)
print("q=",q)
print("n=",n)
print("c=",c)
