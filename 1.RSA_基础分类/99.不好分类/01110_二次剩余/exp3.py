

from gmpy2 import jacobi,invert

ms = []
for tc in c:
    for bit in range(10):
        c1 = tc*invert(int(pow(z,bit,n)),n)%n
        if jacobi(c1,n)==1:  #是二次剩余
            ms.append(bit)
            break

v = ''.join([str(i) for i in ms[::-1]])
long_to_bytes(int(v,2))