
import libnum
#
# p=libnum.generate_prime(256)
# q=libnum.generate_prime(256)
# n=p*q
# e=65537
# c=pow(p+q,e,n)
# c2=(pow(p,e,n)+pow(q,e,n))%n
# print(c==c2)


p=3
q=2
e=3
n=6
c=pow(p-q,e,n)
c1=pow(p+q,e,n)
print(c1)
print(c)

