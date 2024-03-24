

import gmpy2
import libnum
import sympy





p=libnum.generate_prime(6)
q=libnum.generate_prime(6)
while 1:
    p = libnum.generate_prime(6)
    q = libnum.generate_prime(6)
    p1,q1,gcd=libnum.xgcd(p,q)
    if p1*p%q1==1 and q1*q%p1==1:
        print("p",p)
        print("q",q)
        break
# p1=libnum.invmod(p,q)
# q1=libnum.invmod(q,p)
# p1,q1,gcd=libnum.xgcd(p,q)
print("p1,",p1)
print("q1,",q1)


print(p1*p%q1)
print(q1*q%p1)

p2, q2, gcd = libnum.xgcd(p1, q1)
print("p2,",p2)
print("q2,",q2)
for i in range(61):
    p2 -= q1
    q2 += p1
    # if (p-1)*(q-1)==phi:
    if p2==p and q2==q:
        print(p2)
        print(q2)

