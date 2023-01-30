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
n1= 148940337131589571956546000093283178449
c1= 37661829633479650123965286422613768806
n2= 194545959106983958495796913611226256697
c2= 136557714345886330223035822589488157230
n3= 159675071780718021961142743321726109279
c3= 120830575737154793687705030754292986572
