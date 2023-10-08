import libnum
import uuid
flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
#生成随机素数
p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
e=65537
n=p*q
phi_n=(p-1)*(q-1)
#求逆元
d=libnum.invmod(e,phi_n)
c=pow(m,e,n)


print ("n=",n)
print("d=",d)
print ("e=",e)
print ("c=",c)