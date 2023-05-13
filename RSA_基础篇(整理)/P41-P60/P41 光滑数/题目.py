from random import choice
from Crypto.Util.number import isPrime, sieve_base as primes
import uuid
flag="flag{"+str(uuid.uuid4())+"}"

def getPrime(bits):
    while True:
      n = 2
      while n.bit_length() < bits:
          n *= choice(primes)	#primes为前10000个素数的列表
      if isPrime(n + 1):
          return n + 1

e = 0x10001
m = int.from_bytes(flag.encode(), 'big')
p, q = [getPrime(2048) for _ in range(2)]
n = p * q
c = pow(m, e, n)


print("n=",n)
print("c=",c)