import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
n=p*q
print(p)
print(q)
l1=pow(p,q,n)
l2=pow(q,p,n)
print(l1==p)
print(l2==q)
