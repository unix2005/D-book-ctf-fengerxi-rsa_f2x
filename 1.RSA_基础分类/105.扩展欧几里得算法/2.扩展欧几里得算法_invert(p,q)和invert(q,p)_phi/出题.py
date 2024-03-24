import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
# print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)

e = 65537
n = p * q
phi = (p - 1) * (q - 1)
pinv = gmpy2.invert(p, q)
qinv = gmpy2.invert(q, p)
c = pow(m, e, n)

print("e=", e)
print("phi=", phi)
print("c=", c)
print("pinv=", pinv)
print("qinv=", qinv)
