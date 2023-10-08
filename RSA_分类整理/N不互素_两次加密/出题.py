import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"

p1=libnum.generate_prime(512)
p2=libnum.generate_prime(512)
q=libnum.generate_prime(512)
n1 = p1*q
n2 = p2*q
e = 65537

m = libnum.s2n(flag)
c = pow(m, e, n1)
c = pow(c, e, n2)
print("n1=",n1)
print("n2=",n2)
print("c = %d" % c)
