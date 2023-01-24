from Crypto.Util.number import *
import sympy
import random
import libnum
import gmpy2
# m = bytes_to_long(flag)
p = getPrime(512)
print("p=",p)
q = getPrime(512)
print("q=",q)
phi = (p-1)*(q-1)
e = 65537
n = p * q
# c = pow(m, e, n)

s = getPrime(300)
print("s=",s)
N = getPrime(2048)
print("N=",N)
g = p * inverse(s,N)**2 % (N**2)
# print(libnum.invmod(s,N))
# print(inverse(s,N))
ff=libnum.invmod(s,N)
print(libnum.invmod(ff,N**2))
print("ff=",ff)
print(ff>N)
print("g=",g)

print(gmpy2.bit_length(g))
print(gmpy2.bit_length(N**2))
print(ff*2%N**2)
k=p * ff**2 //N
print("k=",k)
print(g+k*N**2==p * inverse(s,N)**2 )
print(gmpy2.gcd(n,g+N**2))

g1=g%N
print(g1)
print(gmpy2.bit_length(g1))
print(g1==(ff*ff*p)%N)
print(g1+k*N==ff*p*ff)
print(g1*s*s//(N**2))
# *N+p==g1*s*s)