import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p=libnum.generate_prime(512)
q=libnum.generate_prime(512)

e = 0x10001
n = p * q
c = pow(m, e, n)
leak = (pow(p, q, n) + pow(q, p, n)) % n
print(f'{e = }')
print(f'{c = }')
print(f'{n = }')
print(f'{leak = }')
