from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from secret import flag


with open("flag.txt",'r') as f:
    flag = f.read().strip()

p = getPrime(128)
q = getPrime(128)

while p % e != 1:
    p = getPrime(128)
while q % e != 1:
    q = getPrime(128)

n = p * q
m = bytes_to_long(flag.encode())
c = pow(m, e, n)
print(f"Ciphertext: {hex(c)}")

with open("pubkey.pem",'w') as f:
    pk = RSA.construct([n, e])
    f.write(pk.exportKey('PEM').decode('utf-8'))

# Ciphertext: 0x459cc234f24a2fb115ff10e272130048d996f5b562964ee6138442a4429af847

52419317100235286358057114349639882093779997394202082664044401328860087685103

P39 = 283378097758180413812138939650885549231
P39 = 184980129074643957218827272858529362113