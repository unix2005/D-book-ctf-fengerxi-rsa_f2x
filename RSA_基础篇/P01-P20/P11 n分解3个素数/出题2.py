import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
r = libnum.generate_prime(512)
z = libnum.generate_prime(512)
n = p * q * r * z
e = 65537
c = pow(m, e, n)
print("p=", p)
print("q=", q)
print("r=", r)
print("z=", z)
print("n=", n)
print("e=", e)
print("c=", c)
