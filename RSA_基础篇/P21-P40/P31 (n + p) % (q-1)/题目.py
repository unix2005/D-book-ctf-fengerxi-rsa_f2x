import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p=libnum.generate_prime(512)
q=libnum.generate_prime(512)
if p <= q:
    p, q = q, p
e = 0x10001
n = p * q
c = pow(m, e, n)
leak = (n + p) % (q-1)
print(f'{e = }')
print(f'{c = }')
print(f'{n = }')
print(f'{leak = }')
