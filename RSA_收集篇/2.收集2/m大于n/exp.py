

n= 1938198674432811161450690669878250944830265839396906617662062291196152960227589796372087441130963
c= 90170164274936424192415483102025065297184726282389841586708984518420677588910796600189918035116
e=0x10001
import libnum
import gmpy2
p1,s=gmpy2.iroot(n,2)
p=gmpy2.next_prime(p1)
q=n//p
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m1=pow(c,d,n)
print(m1)
for k in range(100000,1,-1):
    m=m1+k*n
    flag=libnum.n2s(int(m))
    print(flag)
    if  b"flag" in flag:
        print(flag)
        exit()