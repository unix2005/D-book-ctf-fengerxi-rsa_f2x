

def crypto01(n3, n1, n2):
    n4 = 1
    while n1 > 0:
        if n1 % 2: 
            n4 = (n4 * n3) % n2
        n3 = n3 *n3 % n2
        n1 //= 2
    return n4

n3=3
n1=5
n2=23
c1=crypto01(n3, n1, n2)
c2=pow(n3,n1,n2)
print(c1)
print(c2)