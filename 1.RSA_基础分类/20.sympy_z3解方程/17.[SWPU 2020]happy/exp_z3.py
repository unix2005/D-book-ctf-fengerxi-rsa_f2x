
from z3 import *

a1= 1285367317452089980789441829580397855321901891350429414413655782431779727560841427444135440068248152908241981758331600586
a2= 1109691832903289208389283296592510864729403914873734836011311325874120780079555500202475594
e=0x872a335
c=0x7a7e031f14f6b6c3292d11a41161d2491ce8bcdc67ef1baa9e

import libnum

p = Int('p')
q = Int('q')
s = Solver()
s.add(q+q*p**3==a1)
s.add(q*p+q*p**2==a2)


if s.check() == sat:
    model = s.model()
    print(model)
else:
    print("No solution found")

p = int(str(model[p]))
q = int(str(model[q]))
n=p*q
phi=(p-1)*(q-1)
print(phi)
d=libnum.invmod(e,int(phi))
m=pow(c,d,n)
print(libnum.n2s(int(m)))
