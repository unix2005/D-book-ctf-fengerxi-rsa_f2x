
import libnum
import gmpy2
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = libnum.generate_prime(512)
assert p > q
n = p*q
e = 65536  #2**16
num1 = (pow(p,e,n)-pow(q,e,n)) % n
num2 = pow(p-q,e,n)
c = pow(m,e,n)

print("num1=",num1)
print("num2=",num2)
print("n=",n)
print("c=",c)


