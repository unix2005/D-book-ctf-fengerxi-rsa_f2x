import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(256)
q = libnum.generate_prime(256)
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
print("d=", d)
dp = d % (p - 1)
dq = d % (q - 1)
c = pow(m, e, n)

print("p=", p)
print("q=", q)
print("c=", c)
print("dp=", dp)
print("dq=", dq)
