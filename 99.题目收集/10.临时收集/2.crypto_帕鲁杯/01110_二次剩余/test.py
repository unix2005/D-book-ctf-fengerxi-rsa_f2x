
from random import randrange

from Crypto.Util.number import getPrime, getRandomRange, bytes_to_long

flag=b'flag{1234abcd}'

p = getPrime(512)
q = getPrime(512)
n = p * (q**2)
e = 65537

while True:
    z = randrange(1, n)
    if all(pow(z, (x - 1) // 2, x) == x - 1 for x in (p, q)):
        break

def encrypt_bit(bit, n, z):
    secret = getRandomRange(1, n - 1) #随机数
    return (pow(secret, 2, n) * pow(z, bit, n)) % n


#pow(secret, 2, n) * pow(z, bit, n)) % n
#bit=0   pow(z, bit, n)=1
# pow(s, 2, n)
#bit=1  pow(secret, 2, n) *pow(z, 1, n)

m = int(bin(bytes_to_long(flag))[2:])
print(f'm={m}')

c = []
while m:
    bit = m % 10
    print(bit)
    # time.sleep(2)
    c.append(encrypt_bit(bit, n, z))
    m //= 10

print("n=", n)
print("gift1=", pow((p + q), e, n))
print("gift2=", pow((p - q), e, n))
print("z=", z)
print("c=", c)