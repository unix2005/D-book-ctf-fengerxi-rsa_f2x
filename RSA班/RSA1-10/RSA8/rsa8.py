import libnum
import gmpy2
import uuid
import random

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
# 生成随机素数
p = libnum.generate_prime(1024)
# 字符串转数字
n = p
e = 65537
c = pow(m, e, n)
print("n=", n)
print("c=", c)
print("e=", e)
