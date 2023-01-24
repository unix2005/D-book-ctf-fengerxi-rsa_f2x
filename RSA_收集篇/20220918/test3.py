
import libnum
import base64

a=b"Lf512alKZ84flUk6g+u7Kw=="
c=(base64.b64decode(a))
print(base64.b16encode(c))

