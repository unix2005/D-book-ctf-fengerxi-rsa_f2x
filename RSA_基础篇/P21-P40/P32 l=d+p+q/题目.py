import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p=libnum.generate_prime(512)
q=libnum.generate_prime(512)

e = 0x10001
n = p * q
c = pow(m, e, n)
d=libnum.invmod(e,(p-1)*(q-1))
leak = d+p+q
print(f'{e = }')
print(f'{c = }')
print(f'{n = }')
print(f'{leak = }')
