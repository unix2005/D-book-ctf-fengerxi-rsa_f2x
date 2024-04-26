import libnum
import uuid
from Crypto.Util.number import *
import gmpy2

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m=libnum.s2n(flag)

p = getPrime(512)
q1 = getPrime(512)
q2 = getPrime(512)
n1 = p * q1
n2 = p * q2
e = 65537
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)

print("e=",e)
print("n1=",oct(n1)[2:])
print("n2=",oct(n2)[2:])
print("c1=",oct(c1)[2:])
print("c2=",oct(c2)[2:])
