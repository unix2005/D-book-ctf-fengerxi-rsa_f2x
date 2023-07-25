

def crypto01(n1, n2, n3):
    n4 = 1
    while n2 > 0:
        if n2 % 2:
            n4 = (n4 * n1) % n3
            print("n4",n4)
        n1 = n1 *n1 % n3
        n2 //= 2
        print("n2",n2)
    return n4
n1=3
n2=4
n3=11
c=pow(n1,n2,n3)
#print(c)
c=crypto01(n1,n2,n3)
# print(c)

# n1%3 n1*n1% n3