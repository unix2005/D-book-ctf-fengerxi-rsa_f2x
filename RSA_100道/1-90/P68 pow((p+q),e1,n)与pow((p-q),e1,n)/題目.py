

import libnum
import gmpy2
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = libnum.generate_prime(16)
print(e)
e1 = 2023
n = p*q
h1=pow((p+q),e1,n)
h2=pow((p-q),e1,n)
c=pow(m,e,n)
print(n)
print(h1)
print(h2)
print(c)