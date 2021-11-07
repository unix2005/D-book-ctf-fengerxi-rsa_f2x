from Crypto.PublicKey import RSA
import libnum
import gmpy2

with open("pubckey.pem", "rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)

with open("private.pem", "rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)
    print('d = %d' % key.d)
    print('p = %d' % key.p)
    print('q = %d' % key.q)
