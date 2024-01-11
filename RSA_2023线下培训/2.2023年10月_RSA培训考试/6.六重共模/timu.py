import libnum
import gmpy2
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

k=256
k1=32
num=6
p = libnum.generate_prime(k)
q = libnum.generate_prime(k)
n = p * q
print("n=",n)
tmp=[]
for i in range(0,num):
    tmp.append(libnum.generate_prime(k1))
e=[]
for j in range(0,num):
    tmp1 = 1
    for i in range(0,num):
        if i !=j :
            tmp1=tmp1*libnum.generate_prime(k1)
            tmp1=tmp1*tmp[i]
    e.append(tmp1)

for i in range(0,num):
    print("e"+str(i+1)+"=",e[i])
    c=pow(m,e[i],n)
    print("c"+str(i+1)+"=",c)


