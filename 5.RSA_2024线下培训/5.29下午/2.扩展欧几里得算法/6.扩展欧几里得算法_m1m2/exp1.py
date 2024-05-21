
x= 6298879290960904165363623168765864051745030711468
y= -12085239051824524017287389520592994282786541210367
import libnum
##扩展欧几里得定理
y1,x1,gcd1=libnum.xgcd(x,y)
print(x1)
print(y1)
# m1=x1+k1y
# m2=y1+k2x
m1=0
m2=0
while 1:
    if libnum.xgcd(m1,m2)==(x,y,1):
        break
    m1=x1+y
    m2=y1-x
    x1=m1
    y1=m2

print(m1)
print(m2)
print(libnum.n2s(m1)+libnum.n2s(m2))







