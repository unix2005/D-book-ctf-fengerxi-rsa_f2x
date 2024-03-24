
import libnum
import gmpy2
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

k=512
k1=128
k2=256
p = libnum.generate_prime(k)
q = libnum.generate_prime(k)
n = p * q
tmp1 = libnum.generate_prime(k1)
tmp2 = libnum.generate_prime(k1)
tmp3 = libnum.generate_prime(k1)
tmp4 = libnum.generate_prime(k1)

e1 = libnum.generate_prime(k2) * tmp1 *tmp2*tmp3
e2 = libnum.generate_prime(k2) * tmp2 *tmp3*tmp4
e3 = libnum.generate_prime(k2) * tmp3 *tmp4*tmp1
e4 = libnum.generate_prime(k2) * tmp4 *tmp1*tmp2

c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
c3 = pow(m, e3, n)
c4 = pow(m, e4, n)

print("n=", n)
print("e1=",e1)
print("e2=",e2)
print("e3=",e3)
print("e4=",e4)
print("c1=", c1)
print("c2=", c2)
print("c3=", c3)
print("c4=", c4)