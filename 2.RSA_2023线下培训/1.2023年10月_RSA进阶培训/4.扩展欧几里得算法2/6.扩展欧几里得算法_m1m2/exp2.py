
m1= 149691910197838710952131726661246283540836232541283
m2= 78020076320062211440531721750073204083582073058429
y= 6298879290960904165363623168765864051745030711468
x= -12085239051824524017287389520592994282786541210367
import libnum



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