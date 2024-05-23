import gmpy2
import libnum
import random
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

while 1:
    e = random.randint(100, 1000)
    p = libnum.generate_prime(512)
    q = libnum.generate_prime(512)
    phi_n = (p - 1) * (q - 1)
    t = gmpy2.gcd(e, phi_n)
    if t == e:
        continue
    t1 = e // t
    if gmpy2.invert(t1, phi_n) and t > 1:
        break
n = p * q
c = pow(m, e, n)
print("p=", p)
print("q=", q)
print("e=", e)
print("c=", c)
