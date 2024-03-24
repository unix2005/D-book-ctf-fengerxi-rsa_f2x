

import libnum

x= -4480128578596562789310462941822791389754265318980
y= 9325158603768382769807302821801846257957239795281

d=1

a,b,d=libnum.xgcd(x,y)
for i in range(1000):
    if (libnum.xgcd(a,b)==x,y,d):
        a = abs(a)
        tmp=libnum.n2s(a)+libnum.n2s(b)
        if b"flag" in tmp:
            print(tmp)

    a+=abs(y)
    b+=abs(x)
