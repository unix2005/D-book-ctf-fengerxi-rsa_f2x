import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)

m1=flag[:len(flag)//2]
m2=flag[len(flag)//2:]
m1=libnum.s2n(m1)
m2=libnum.s2n(m2)
x,y,d=libnum.xgcd(m1,m2)
print("d=",d)
print("m1=",m1)
print("m2=",m2)
print("x=",x)
print("y=",y)
