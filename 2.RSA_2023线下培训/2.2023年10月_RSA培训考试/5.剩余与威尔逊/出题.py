
import libnum
import uuid
import gmpy2

flag = "flag{" + str(uuid.uuid4()) + "}"
m=libnum.s2n(flag)


x=2293
y=2999

p=libnum.generate_prime(256)
q=gmpy2.next_prime(p)
n=p*q


c1=pow(m,p,q)
c2=pow(m,q,p)

#
# m1=m*(p-x)!%p
# for i in range(1,p-x+1):
#     m=(m*i)%n
#
#c1=c1*(p-x)!%p
# for i in range(1,p-x+1):
#     c1=(c1*i)%p

# m1=m*(z-x)!%z


for i in range(p-x+1,p-1):
    c1=c1*libnum.invmod(i,p)%p

#c2=c2*(q-x)!%q
# for i in range(1,q-y+1):
#     c2=(c2*i)%q
for i in range(q-y+1,q-1):
    c2=c2*libnum.invmod(i,q)%q


print("n=",n)
print("c1=",c1)
print("c2=",c2)
n= 8973111727043835268073030786154872680698373043779309133152761408036168040324790610629878698254512273043461353358713176585944330401628782665897826660934613
c1= 64284764317119422373346563850463475291505287640187549432070954036621825864368
c2= 9536794169507209829892131704431419340244159120365249097190319866115295918289
