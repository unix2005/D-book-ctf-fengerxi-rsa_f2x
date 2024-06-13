

from Crypto.Util.number import *
import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)

p = getPrime(512)
q = getPrime(512)
n = p*p*q

c = pow(m, n, n)
d = inverse(n, (p-1)*(q-1))
print(f'n = {n}')
print(f'd = {d}')
print(f'c = {c}')

