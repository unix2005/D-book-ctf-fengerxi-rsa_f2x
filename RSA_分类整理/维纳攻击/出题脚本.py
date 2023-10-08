import libnum
import random
import gmpy2
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
# 生成随机素数
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
# 字符串转数字
m = libnum.s2n(flag)
n = p * q
phi_n = (p - 1) * (q - 1)

# 计算d
while True:
    nbits = 1024
    d = random.getrandbits(nbits // 4)
    if (libnum.gcd(d, phi_n) == 1 and 36 * pow(d, 4) < n):
        break
# 计算e
e = libnum.invmod(d, phi_n)

c = pow(m, e, n)

print("n=", n)
print("e=", e)
print("c=", c)
