

import libnum
import uuid
import gmpy2

flag="flag{"+str(uuid.uuid4())+"}"
m=libnum.s2n(flag)
p=libnum.generate_prime(1024)
q=libnum.generate_prime(16)
n = p*q
e = 65537
#
# print("p=",p)
# print("q=",q)

m=pow(m*-1,1,p)
print(m)

for i in range(p-q,p):
    m=m*libnum.invmod(i,p)%p
c=pow(m,e,n)
print("n=",n)
print("c=",c)
