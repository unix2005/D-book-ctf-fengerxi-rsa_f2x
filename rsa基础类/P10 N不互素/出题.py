import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q1 = libnum.generate_prime(1024)
q2 = libnum.generate_prime(1024)
n1 = p * q1
n2 = p * q2
e = 65537
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
print("n1=", n1)
print("n2=", n2)
print("c1=", c1)
print("c2=", c2)
