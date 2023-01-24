import gmpy2
import libnum

n = 1337745688108544106157579826274728293001288318020558488751541
e = 2
c = 925754269128362760755388951296252440425242407040891016528411
p=1121783506288081835936544963613
q=1192516809714085486143664731257


inv_p = gmpy2.invert(p, q)
inv_q = gmpy2.invert(q, p)
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)
a = (inv_p * p * mq + inv_q * q * mp) % n
b = n - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % n
d = n - int(c)
# 因为rabin 加密有四种结果，全部列出。
aa = [a, b, c, d]
for i in aa:
    print(i)
    print(libnum.n2s(int(i)))
