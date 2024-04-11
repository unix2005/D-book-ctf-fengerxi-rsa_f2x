
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
import gmpy2
import sympy
import base64

c1="""BhUXO8RZzppFl7Fw72jbGkEIaH/6/D5c00bYx1HEAPfN5+BeRII=
BSiVik1bo999kG2eHzZaVt056rh74oRbbU99OrIE48ds9kQ6AR4=
BbGPmOvTr8OYCIgwyEpu5b26jGUY2EHZRu2FUSK/cdUmK0Wqkhc=
Axun6PS3aheoX8o3G8e3mtAxHC+C6r95oV84OQ8dxsFsxnYcfo0="""
c2=c1.split("\n")
print(c2)
with open("key.pem", 'rb') as f:
    key = f.read()
rsakey = RSA.importKey(key)
n= rsakey.n
e= rsakey.e
print(n)
print(e)
p=948539437740472240970258995719507356652939947
q=1033916782753483187367063564275935620987269651
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)

m1=b''
import re
for i in c2:
    tmp1=base64.b64decode(i)
    tmp2=libnum.s2n(tmp1)
    m=pow(tmp2,d,n)
    tmp3=(libnum.n2s(int(m)))
    print(tmp3)
    tmp4=re.search(rb'\x00([a-f0-9]+)',tmp3)[1]
    print(tmp4)
    m1+=tmp4
print(base64.b16decode(m1.upper()))