import libnum
import gmpy2

flag = 'flag{01d80670b01b654fe4831a3e81870734}'
p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
n = p * q
e = 65537
m = libnum.s2n(flag)
c = pow(m, e, n)
print("n=", n)
print("e=", e)
print("c=", c)
