

import libnum

cc=[c1,c2,c3]
nn=[n1,n2,n3]

mm=libnum.solve_crt(cc,nn)
print(mm)

for e in range(7,20):
    m=libnum.nroot(mm,e)
    flag=libnum.n2s(m)
    if b"flag" in flag:
        print(flag)

