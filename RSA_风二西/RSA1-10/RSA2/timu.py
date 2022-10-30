import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

p1 = libnum.generate_prime(64)
q1 = libnum.generate_prime(64)
p2 = libnum.generate_prime(64)
q2 = libnum.generate_prime(64)
p3 = libnum.generate_prime(64)
q3 = libnum.generate_prime(64)
e = 1
c1 = pow(m, e, p1 * q1)
c2 = pow(m, e, p2 * q2)
c3 = pow(m, e, p3 * q3)
print("n1=", p1 * q1)
print("c1=", c1)
print("n2=", p2 * q2)
print("c2=", c2)
print("n3=", p3 * q3)
print("c3=", c3)
n1 = 172774622114813683746188230007837413819
c1 = 170260248491697016437095929037490480036
n2 = 160333927436069409658483084503168246581
c2 = 45134242975344810542214361639231372051
n3 = 170109598387116572557100744899522621873
c3 = 47903985600747367026642413789127948969
