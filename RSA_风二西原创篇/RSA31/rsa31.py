import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
e = 65537
n = p * q
m=""
for i in flag:
    m+=str(ord(i))
m=int(m)
c=pow(m,e,n)
print("n=",n)
print("e=",e)
print("c=",c)
