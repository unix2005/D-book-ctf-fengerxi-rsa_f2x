import libnum
import gmpy2
import random
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n1 = p * q
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n2 = p * q
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n3 = p * q
while 1:
    e = random.randint(10, 20)
    print(e)
    if gmpy2.is_prime(e):
        break
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)

print("n1=", n1)
print("n2=", n2)
print("n3=", n3)

print("c1=", c1)
print("c2=", c2)
print("c3=", c3)
