
import libnum
#生成素数
p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
#字节、数字转换
flag="flag"
a=libnum.s2n(flag)
b=libnum.n2s(a)
print(a)
print(b)
#二进制、数字转换
flag="flag"
a=libnum.s2b(flag)
b=libnum.b2s(a)
print(a)
print(b)
#求逆元
libnum.invmod(e,phi)
#求最大公约数
libnum.gcd(a,b)
#求最小公倍数
libnum.lcm(a,b)
#开方
libnum.nroot(a,b)
#中国剩余定理
libnum.solve_crt()
#扩展欧几里得算法
libnum.xgcd(a,b)

import gmpy2
#判断是否为素数
gmpy2.is_prime()
#判断是否为完全平方数
gmpy2.is_square()
#生成下一个素数
gmpy2.next_prime()
#求逆元
gmpy2.invert()
#开方
gmpy2.iroot()
#返回数字二进制的长度
gmpy2.bit_length()
#扩展欧几里得算法
gmpy2.gcdext()
#
import sympy
#返回上一个素数
sympy.prevprime()


