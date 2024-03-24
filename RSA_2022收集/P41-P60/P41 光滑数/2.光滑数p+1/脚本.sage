
#https://blog.csdn.net/m0_62506844/article/details/125774485
def mlucas(v, a, n):
    """ Helper function for williams_pp1().  Multiplies along a Lucas sequence modulo n. """
    v1, v2 = v, (v**2 - 2) % n
    for bit in bin(a)[3:]:
        v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n) if bit == "0" else ((v1*v2 - v) % n, (v2**2 - 2) % n)
    return v1

for v in count(1):
    for p in primegen():
        e = ilog(isqrt(n), p)
        if e == 0:
            break
        for _ in xrange(e):
            v = mlucas(v, p, n)
        g = gcd(v-2, n)
        if 1 < g < n:
            return g # g|n
        if g == n:
            break
