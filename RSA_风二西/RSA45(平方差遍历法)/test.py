
n=35
import gmpy2
import libnum

a=gmpy2.iroot(n,2)[0]
while 1:

    b2=pow(a,2)-n

    if gmpy2.is_square(b2):
        b=gmpy2.iroot(b2,2)[0]
        print(a)
        print(b)
        print(a-b)
        print(a+b)
    a+=1

