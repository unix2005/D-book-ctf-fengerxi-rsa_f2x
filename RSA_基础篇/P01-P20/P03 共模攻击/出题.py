import libnum
import gmpy2
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n1 = p * q
n2 = p * q
e1 = 2333
e2 = 23333
m = libnum.s2n(flag)
c1 = pow(m, e1, n1)
c2 = pow(m, e2, n2)
print("n1=", n1)
print("n2=", n2)
print("e1=", e1)
print("e2=", e2)
print("c1=", c1)
print("c2=", c2)
