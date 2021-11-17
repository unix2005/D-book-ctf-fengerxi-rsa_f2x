from Crypto.Util.number import *
import libnum
import os
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
g = n+1
m = bytes_to_long(flag.encode()+os.urandom(80))
assert m < n
c=(pow(g,p,n*n)*pow(m,n,n*n))%(n*n)
print("c="+str(c))
print("n="+str(n))
print("hint="+str(pow(m,n,n*n)))