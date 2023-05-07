import libnum
import gmpy2
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
e = 3
while 1:
    p = libnum.generate_prime(512)
    q = libnum.generate_prime(512)
    if (p-1)%e==0 and (q-1)%e==0:
        break
n=p*q
c=pow(m,e,n)
print(flag)
print("n=", n)
print("p=", p)
print("q=", q)
print("c=", c)
print("e=", e)
