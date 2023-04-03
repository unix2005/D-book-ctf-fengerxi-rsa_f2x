import gmpy2
import libnum
import uuid

p=libnum.generate_prime(512)
q=libnum.generate_prime(512)
print(p)
print(q)
n=p*q
l1=p+q
print(l1)
l2=pow(q,p,p)+pow(p,q,q)+pow(q,p,p)
print(l2)
l3=pow(p,q,n)+pow(q,p,n)
print(l3)
print(l1==l2)
print(l1==l3)
import gmpy2
print(gmpy2.bit_length(l1))

print((13113+1)%(13113-1))