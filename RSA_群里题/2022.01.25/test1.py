#coding:utf-8
import gmpy2
from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
e = getPrime(32)
print("e=",e)
n = p*q*r
phi = (p-1)*(q-1)*(r-1)
d = gmpy2.invert(e,phi)
print("d=",d)
dp = d%((q-1)*(r-1))
dq = d%((p-1)*(r-1))
dr = d%((p-1)*(q-1))
flag = 'flag{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
m = bytes_to_long(flag.encode())
c = pow(m,e,n)

print("p=",p)
print("q=",q)
print("r=",r)
print("dp=",dp)
print("dq=",dq)
print("dr=",dr)
print("c=",c)