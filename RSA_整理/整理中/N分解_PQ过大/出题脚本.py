import libnum
import gmpy2
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(32)
n = p * q
e = 65537
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
print(flag)