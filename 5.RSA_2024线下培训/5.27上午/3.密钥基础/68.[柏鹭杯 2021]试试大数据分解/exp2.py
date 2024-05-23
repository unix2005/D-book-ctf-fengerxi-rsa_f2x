from Crypto.PublicKey import RSA
import gmpy2
from Crypto.Util.number import *
import base64
import io
with open('key.pem','rb') as f:
    key=RSA.import_key(f.read())
    n=key.n
    e=key.e
p=948539437740472240970258995719507356652939947
q=1033916782753483187367063564275935620987269651
phi_n=(p-1)*(q-1)
d=gmpy2.invert(e,phi_n)

c='BhUXO8RZzppFl7Fw72jbGkEIaH/6/D5c00bYx1HEAPfN5+BeRII='
c=bytes_to_long(base64.b64decode(c))
m=pow(c,d,n)
print(long_to_bytes(m))

with open('D://Environment/Pythoncode/Crypto-tmpfile/flag.enc2','rb') as f:
    c1=f.read()
    c1=bytes_to_long(base64.b64decode(c1))
    m=pow(c1,d,n)
    print(long_to_bytes(m))

with open('D://Environment/Pythoncode/Crypto-tmpfile/flag.enc3','rb') as f:
    c2=f.read()
    c2=bytes_to_long(base64.b64decode(c2))
    m=pow(c2,d,n)
    print(long_to_bytes(m))

with open('D://Environment/Pythoncode/Crypto-tmpfile/flag.enc4','rb') as f:
    c3=f.read()
    c3=bytes_to_long(base64.b64decode(c3))
    m=pow(c3,d,n)
    print(long_to_bytes(m))
