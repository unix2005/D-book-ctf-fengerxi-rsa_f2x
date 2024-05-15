
from Crypto.Util.number import getPrime, bytes_to_long
import uuid
import libnum
flag="flag{"+str(uuid.uuid4())+"}"
def prod(lst):
	ret = 1
	for num in lst:
		ret *= num
	return ret
m = libnum.s2n(flag)
primes = [getPrime(32) for _ in range(128)]
n = prod(primes)
e = 65537
print(n)
print(pow(m, e, n))
