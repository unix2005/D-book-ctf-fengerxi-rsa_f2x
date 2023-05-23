import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
# print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
assert  q>p
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
p1 = gmpy2.invert(p, q)
q1 = gmpy2.invert(q, p)-p
c = pow(m, e, n)

print("e=", e)
print("phi=", phi)
print("c=", c)
print("p1=", p1)
print("q1=", q1)
