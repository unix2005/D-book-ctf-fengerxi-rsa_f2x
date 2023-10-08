import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
e = 65537


while 1:
    p = libnum.generate_prime(512)
    q = libnum.invmod(e, p)
    if gmpy2.is_prime(q):
        break
n=p*q
c=pow(m,e,n)
print("n=",n)
print("c=",c)