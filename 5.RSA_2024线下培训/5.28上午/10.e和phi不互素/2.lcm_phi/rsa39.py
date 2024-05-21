import libnum
import uuid
from Crypto.Util.number import *
import gmpy2

flag = "flag{" + str(uuid.uuid4()) + "}"
# print(flag)
m=libnum.s2n(flag)

p = getPrime(512)
q = getPrime(512)
n=p*q
hint = gmpy2.lcm(p - 1 , q - 1)
e=54722
c=pow(m,e,n)

print("n=",n)
print("e=",e)
print("c=",c)
print("hint=",hint)
