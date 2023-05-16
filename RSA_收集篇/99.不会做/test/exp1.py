from gmpy2 import *
from Crypto.Util.number import *
import random

p=getPrime(512)
q=getPrime(512)
n=p*q

print(p==pow(p,q,n))
print(q==pow(q,p,n))