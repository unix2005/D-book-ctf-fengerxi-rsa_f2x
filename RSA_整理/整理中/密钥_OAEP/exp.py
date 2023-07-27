from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import libnum
with open("flag2.pem", 'rb') as f:
    ciphertext = f.read()
with open("prikey2.pem", 'rb') as f:
    key = f.read()

rsakey = RSA.importKey(key)
cipher = PKCS1_OAEP.new(rsakey)
message = cipher.decrypt(ciphertext)
print(message)
# b'flag{e5dca96d-f0cb-4bde-b657-2e2589958557}'