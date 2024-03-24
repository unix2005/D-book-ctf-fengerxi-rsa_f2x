import libnum
import gmpy2
import uuid

k = 512
while 1:
    flag = "flag{" + str(uuid.uuid4()) + "}"
    m = libnum.s2n(flag)
    p = libnum.generate_prime(k)
    q = libnum.generate_prime(k)
    n = p * q
    tmp = libnum.generate_prime(4)
    e1 = libnum.generate_prime(5) * tmp
    e2 = libnum.generate_prime(5) * tmp
    tmp2 = gmpy2.bit_length(m ** tmp) - gmpy2.bit_length(n)
    if e1 != e2 and tmp2 < 5:
        break
    k += tmp2 // 2
print(flag)
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print("e1=", e1)
print("e2=", e2)
print("n=", n)
print("c1=", c1)
print("c2=", c2)
