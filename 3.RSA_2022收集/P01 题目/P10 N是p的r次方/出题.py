import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
n = p ** 5
e = 65537
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
