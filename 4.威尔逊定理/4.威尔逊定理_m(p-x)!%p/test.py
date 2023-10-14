

import libnum

#m=m*(p-x)!%p

x=181
m=359
p=673
for i in range(1,p-x+1):
    m=(m*i)%p
print(m)
x=181
m=359
p=673

for i in range(p-x+1,p-1):
    m=m*libnum.invmod(i,p)%p
print(m)

