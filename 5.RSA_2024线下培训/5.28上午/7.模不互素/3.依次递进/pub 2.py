import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q1 = libnum.generate_prime(512)
q2 = libnum.generate_prime(512)
n1=p*q1
n2=p*q2
e = 65537
c = pow(m, e, n1)
c = pow(c, e, n2)
print("n1=", n1)
print("n2=", n2)
print("c=", c)
