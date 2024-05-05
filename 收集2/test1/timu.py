

from Crypto.Util.number import *
from libnum import *
key = 'aa'

p = getPrime(512)
q = getPrime(512)
n = p*p*q
e = n

c = pow(s2n(key), n, n)
d = inverse(n, (p-1)*(q-1))


print(f'n = {n}')
print(f'd = {d}')
print(f'c = {c}')
print(f'p = {p}')
print(f'q = {q}')
