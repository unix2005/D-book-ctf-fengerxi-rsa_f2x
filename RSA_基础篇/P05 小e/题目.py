import libnum
import gmpy2
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
while True:
    p = libnum.generate_prime(454)
    q = libnum.generate_prime(454)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 3
    if gmpy2.gcd(e, phi_n) == 1:
        break
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
