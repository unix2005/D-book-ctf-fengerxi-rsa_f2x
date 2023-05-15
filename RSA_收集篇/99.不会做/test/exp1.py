from gmpy2 import *
from Crypto.Util.number import *
import random

p=getPrime(512)
q=getPrime(512)
n=p**2+q**2
print(n)