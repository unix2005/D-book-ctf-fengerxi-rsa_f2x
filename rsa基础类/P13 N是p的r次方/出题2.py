import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
n = p ** 3 * q
e = 65537
c = pow(m, e, n)
print("q=", q)
print("n=", n)
print("e=", e)
print("c=", c)
