
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 测试用密钥加密
public_key = RSA.importKey(public_key)
msg = 'flag'
pk = PKCS1_v1_5.new(public_key)
encrypt_text = pk.encrypt(msg.encode())
print(encrypt_text)

# 测试密钥解密
private_key = RSA.importKey(private_key)
pk = PKCS1_v1_5.new(private_key)
msg = pk.decrypt(encrypt_text, 0)
print(msg)

# 两种标准
rsa_components = (n, e, int(d), p, q)
arsa = RSA.construct(rsa_components)
rsakey = RSA.importKey(arsa.exportKey())
rsakey = PKCS1_OAEP.new(rsakey)
decrypted = rsakey.decrypt(c)
print(decrypted)
with open("flag.pem", "wb") as f:
    f.write(c1)
