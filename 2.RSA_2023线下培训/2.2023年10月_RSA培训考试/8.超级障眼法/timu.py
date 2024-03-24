

import uuid
import libnum
import gmpy2
import os
flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
flag = flag.encode()
m = libnum.s2n(flag)


p = libnum.generate_prime(256)
q = libnum.generate_prime(256)
e = 65537

n=p*q
print("n=",n)
p1=pow(p,q,n)
q1=pow(q,p,n)
print("p1=",p)
print("q1=",q)

# for i in range(1,p1-1):
#     m=m*i%p1
# for i in range(1,q1-1):
#     m=m*i%q1

c=pow(m+n,e,n)
print("c=",c)

