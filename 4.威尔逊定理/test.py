
#验证威尔逊定理
import libnum

a=libnum.generate_prime(1024)
b=libnum.generate_prime(1024)
print(a)
print(b)
a=521
b=3137

a1=1
for i in range(1,a):
    a1=(a1*i)%a
print(a1)
#(p-1)!%p=p-1=-1
#(p-2)!%p= 1
a1=1
for i in range(1,a-1):
    a1=(a1*i)%a
print(a1)