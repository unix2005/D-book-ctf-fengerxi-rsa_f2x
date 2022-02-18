import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
while True:
    p = libnum.generate_prime(1024)
    q = libnum.generate_prime(1024)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 3
    if gmpy2.gcd(e, phi_n) == 1:
        break
d = gmpy2.invert(e, phi_n)
d1 = d & ((1 << 256) - 1)
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
print("d1=", d)
