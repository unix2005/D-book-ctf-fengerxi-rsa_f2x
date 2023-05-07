
import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
n=p*q

t1=pow(m,n+1,n)
x=pow(m,p,n)
y=pow(m,q,n)
t2=pow(x*y,1,n)
t3=pow(m,p+q,n)

print(t2==t3)