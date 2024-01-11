import gmpy2
import libnum
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 65537
n=p*q
p1=libnum.invmod(p,q)
q1=libnum.invmod(q,p)
phi=(p-1)*(q-1)
print(phi)
d=libnum.invmod(e,phi)

c=pow(m,e,n)
print("p1=",p1)
print("q1=",q1)
print("d=",d)
print("e=",e)
print("c=",c)