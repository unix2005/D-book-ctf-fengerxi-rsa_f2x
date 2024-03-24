from Crypto.Util.number import *
import gmpy2 as gp
import uuid
flag="flag{"+str(uuid.uuid4())+"}"
print(len(flag))
e=0x10001
m=bytes_to_long(flag.encode())
p=getPrime(160)
q=gp.next_prime(p)
phi=(p-1)*(q-1)
d=gp.invert(e,phi)
n=p*q
c=pow(m,e,n)
print("q=",q)
print("p=",p)
print("m=",m)
print('n=',n)
print('c=',c)
print('d=',d)

