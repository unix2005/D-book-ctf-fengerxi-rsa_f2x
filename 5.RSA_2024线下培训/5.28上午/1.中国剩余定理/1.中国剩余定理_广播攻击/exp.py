import libnum
import gmpy2


n = [n1, n2, n3]
c = [c1, c2, c3]
mm = libnum.solve_crt(c, n)

#print(mm)
for e in range(7, 20):
    m, t = gmpy2.iroot(mm, e)
    if t:
        print(m)
        print(libnum.n2s(int(m)))

