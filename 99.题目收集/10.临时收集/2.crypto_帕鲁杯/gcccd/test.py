import uuid

import libnum

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n = p * q
e = 5113
c1=pow(m//2,e,n)
c2=pow(m,e,n)
print("n=",n)
print("c1=",c1)
print("c2=",c2)
