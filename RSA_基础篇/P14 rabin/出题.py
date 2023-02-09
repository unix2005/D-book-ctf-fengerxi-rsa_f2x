import gmpy2
import libnum
import random
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
n = p * q
e = 2
c = pow(m, e, n)
print("p=", p)
print("q=", q)
print("n=", n)
print("c=", c)
print("e=", e)
