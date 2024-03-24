


import libnum
import uuid

p=libnum.generate_prime(256)
q=libnum.generate_prime(256)
n=p*q
p1=pow(p,q,n)
q1=pow(q,p,n)
print(p==p1)
print(q==q1)