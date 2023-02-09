import libnum
import gmpy2

# 生成随机素数
m = "flag{20d6e2da95dcc1fa5f5432a436c4be18}"
m = libnum.s2n(m)
while True:
    p = libnum.generate_prime(454)
    q = libnum.generate_prime(454)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 3
    if gmpy2.gcd(e, phi_n) == 1:
        break
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
