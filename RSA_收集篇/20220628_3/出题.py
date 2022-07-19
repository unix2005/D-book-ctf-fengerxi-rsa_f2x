
import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
print(m)

p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
phi=(p-1)*(q-1)
lcm=libnum.lcm(p-1,q-1)
n = p * q
e = 65537
c = pow(m, e, n)
print("lcm=",lcm)
print("p=",p)
print("q=",q)
print("n=", n)
print("c=", c)
print("e=", e)