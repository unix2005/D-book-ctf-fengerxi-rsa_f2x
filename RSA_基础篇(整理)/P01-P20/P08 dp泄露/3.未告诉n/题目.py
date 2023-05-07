import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
dp = d % (p - 1)
c = pow(m, e, n)
print("e=", e)
print("c=", c)
print("dp=", dp)
