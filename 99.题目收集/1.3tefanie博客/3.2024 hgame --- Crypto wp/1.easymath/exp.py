import math
from Crypto.Util.number import *
from Crypto.Cipher import AES

def pad(x):
    return x+b'\x00'*(16-len(x)%16)
def solvePell(n):
    x = int(math.sqrt(n))
    y, z, r = x, 1, x << 1
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z

        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r

        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return a, b

D = 114514

x,y = solvePell(D)
key=pad(long_to_bytes(y))[:16]
cipher= AES.new(key,AES.MODE_ECB)
enc=b"\xce\xf1\x94\x84\xe9m\x88\x04\xcb\x9ad\x9e\x08b\xbf\x8b\xd3\r\xe2\x81\x17g\x9c\xd7\x10\x19\x1a\xa6\xc3\x9d\xde\xe7\xe0h\xed/\x00\x95tz)1\\\t8:\xb1,U\xfe\xdec\xf2h\xab`\xe5'\x93\xf8\xde\xb2\x9a\x9a"
m = cipher.decrypt(enc)
print(m)
#hgame{G0od!_Yo3_k1ow_C0ntinued_Fra3ti0ns!!!!!!!}
