import gmpy2
import libnum
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
# print(flag)
m = libnum.s2n(flag)

p = libnum.generate_prime(1024)
q = libnum.generate_prime(200)
a = p**2+q**2

e1=libnum.generate_prime(16)
e2=gmpy2.next_prime(e1)
n=p*q
c1=pow(m,e1,n)
c2=pow(m**3,e2,3*n)

print("a=",a)
print("c1=",c1)
print("c2=",c2)