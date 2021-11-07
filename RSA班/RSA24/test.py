import gmpy2
import libnum
import uuid

p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
p1 = gmpy2.invert(p, q)
q1 = gmpy2.invert(q, p)
print(gmpy2.bit_length(n))
print(gmpy2.bit_length(p1 * p + q1 * q - 1))
print(p1 * p + q1 * q - 1 == n)
True
