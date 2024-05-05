p = ''
with open('file1.txt', "r") as f:
    for i in f.readlines():
        if '-01' in i.strip():
            p += "1"
        else:
            p += "0"
print(p)
q = ''
with open('file2.txt', "r") as f:
    for i in f.readlines():
        if '-01' in i.strip():
            q += "1"
        else:
            q += "0"
print(q)

import base64

import libnum

c = 've9MPTSrRrq89z+I5EMXZg1uBvHoFWBGuzxhSpIwu9XMxE4H2f2O3l+VBt4wR+MmPJlS9axvH9dCn1KqFUgOIzf4gbMq0MPtRRp+PvfUZWGrJLpxcTjsdml2SS5+My4NIY/VbvqgeH2qVA=='
c = base64.b64decode(c)
c = libnum.s2n(c)

p = int(p, 2)
q = int(q, 2)
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = libnum.invmod(e, phi)
m = pow(c, d, n)
print(m)
print(libnum.n2s(m))
