import gmpy2
import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
n = p * q
m1 = ((m >> 12) << 12)
e = 3
c = pow(m, e, n)
print("n=", n)
print("c=", c)
print("e=", e)
print("m1=", m1)
