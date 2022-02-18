import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n = p * q
e = 65537
p1 = ((p >> 462) << 462)
p2 = ((p >> 462))
c = pow(m, e, n)
print("n=", n)
print("c=", c)
print("e=", e)
print("p =", p)
print("p1=", p1)
print("p2=", p2)
