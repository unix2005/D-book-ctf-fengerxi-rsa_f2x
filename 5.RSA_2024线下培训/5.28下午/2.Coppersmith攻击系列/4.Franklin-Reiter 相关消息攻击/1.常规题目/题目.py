import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n = p * q
e = 3
c1=pow(m,e,n)
c2=pow(m+23,e,n)
print("n=",n)
print("c1=",c1)
print("c2=",c2)