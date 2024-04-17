
from Crypto.Util.number import getPrime, getRandomRange, bytes_to_long
from random import randrange
import uuid
import libnum
flag=b'f'

p = getPrime(512)
q = getPrime(512)
n = p * (q**2)
e = 65537



while True:
    z = randrange(1, n)
    if all(pow(z, (x - 1) // 2, x) == x - 1 for x in (p, q)):
        break


def encrypt_bit(m, n, z):
    secret = getRandomRange(1, n - 1)
    return (pow(secret, 2, n) * pow(z, m, n)) % n

m = int(bin(bytes_to_long(flag))[2:])
print(m)
c = []

while m:
    bit = m % 10
    print(bit)
    c.append(encrypt_bit(bit, n, z))
    m //= 10

# print("n=", n)
# print("gift1=", pow((p + q), e, n))
# print("gift2=", pow((p - q), e, n))
# print("z=", z)
# print("c=", c)