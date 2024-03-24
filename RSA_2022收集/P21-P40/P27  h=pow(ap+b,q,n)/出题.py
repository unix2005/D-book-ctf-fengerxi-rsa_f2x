import libnum
import gmpy2
import uuid
from Crypto.Util.number import *

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)

e = 65537
p = getPrime(1024)
q = getPrime(1024)
n = p * q
c = pow(m, e, n)
hint = pow(2020 * p + 2021, q, n)
print(f'n={n}')
print(f'c={c}')
print(f'hint={hint}')
