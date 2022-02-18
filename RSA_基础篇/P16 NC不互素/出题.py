import gmpy2
import libnum
import random
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
print(p)
print(q)
n = p * q
e = 65537
c = pow(m*p + n, e, n)
print("n=", n)
print("c=", c)
print("e=", e)
