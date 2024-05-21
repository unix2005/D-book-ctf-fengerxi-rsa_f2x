#sage
from Crypto.Util.number import *
from Crypto.Cipher import AES

m = 88007513702424243702066490849596817304827839547007641526433597788800212065249
n = 103560843006078708944833658339172896192389513625588
enc = b'\xfc\x87\xcb\x8e\x9d\x1a\x17\x86\xd9~\x16)\xbfU\x98D\xfe\x8f\xde\x9c\xb0\xd1\x9e\xe7\xa7\xefiY\x95C\x14\x13C@j1\x9d\x08\xd9\xe7W>F2\x96cm\xeb'
iv  = b'UN\x1d\xe2r<\x1db\x00\xdb\x9a\x84\x1e\x82\xf0\x86'
tmp = m-n
data = divisors(tmp)
for i in data:
    if i.nbits()<=192 and i.nbits()>=184 and tmp%i==0:
        key = long_to_bytes(i)
        aes = AES.new(key,AES.MODE_CBC,iv)
        flag = aes.decrypt(enc)
        if b'flag' in flag:
            print(flag)
            break
#flag{cf735a4d-f9d9-5110-8a73-5017fc39b1b0}