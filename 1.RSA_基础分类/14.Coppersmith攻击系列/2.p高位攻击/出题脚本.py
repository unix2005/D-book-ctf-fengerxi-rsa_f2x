import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n = p * q
e = 65537
p1 = ((p >> 256) << 256)
c = pow(m, e, n)
print("n=", n)
print("c=", c)
print("e=", e)
print("p1=",bin(p1))
print("p2=",bin(p))
