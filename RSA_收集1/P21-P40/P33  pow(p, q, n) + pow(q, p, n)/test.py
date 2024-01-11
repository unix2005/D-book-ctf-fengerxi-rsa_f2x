import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)
p=libnum.generate_prime(512)
q=libnum.generate_prime(512)
n=p*q
print(p)
print(q)
l1=pow(p,q,n)
l2=pow(q,p,n)
print(l1==p)
print(l2==q)

aa=pow(pow(p,n,n),1//p,n)
print(aa)