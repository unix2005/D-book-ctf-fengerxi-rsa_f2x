import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
e = 65537
n = p * p * q
d=libnum.invmod(e,p*(p-1)*(q-1))
m=libnum.s2n(flag)
c=pow(m,e,n)
h=pow(d,e,n)
print("n=",n)
print("e=",e)
print("c=",c)
print("d=",d)
print("h=",h)

