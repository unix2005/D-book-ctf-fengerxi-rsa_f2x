from Crypto.PublicKey import RSA
import libnum
import gmpy2
from Crypto.Cipher import PKCS1_OAEP

with open("pubckey.pem", "rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)

with open("flag.pem", "rb") as f:
    print(libnum.s2n(f.read()))
p = 157917353240612613228985721630656194311722945516308937261330498508165277310247377832703923065523175124756273573428279717864062071698000252461696489382786233332694953158705205373631757775497851090585826604684754011853843138311329884477597189128553878610236416928882938253069760930838728669670398812741008890533
q = 157917353240612613228985721630656194311722945516308937261330498508165277310247377832703923065523175124756273573428279717864062071698000252461696489382786233332694953158705205373631757775497851090585826604684754011853843138311329884477597189128553878610236416928882938253069760930838728669670398812741008890971
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)

with open("flag.pem", "rb") as f:
    c = f.read()

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum

rsakey = RSA.importKey(key)
cipher = PKCS1_OAEP.new(rsakey)
message = cipher.decrypt(c)