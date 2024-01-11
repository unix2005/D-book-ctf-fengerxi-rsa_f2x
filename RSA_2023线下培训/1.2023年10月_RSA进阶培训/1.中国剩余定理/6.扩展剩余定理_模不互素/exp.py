import gmpy2
import libnum

n1= 69682419484978249870940716311118334348563583323657940451827016494055516271231
n2= 59080403616358250318951962060743300665561000236470577709505394086684086715913
c1= 48897691523522542746078783065306117077299949061306270167171689861626238565452
c2= 21030111018284986454764138111848517442439856258540388982831386199144097858007
e = 65537


n =2   # 同余方程个数
a = [c1,c2]  # 余数
m=[n1,n2] # 模数

"""扩展欧几里得"""
def exgcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q
"""扩展中国剩余定理"""
def CRT(n,a,m):
    if n == 1:
        if m[0] > a[0]:
            return a[0];
        else:
            return -1;

    for i in range(n):
        if m[i] <= a[i]:
            return -1;
        x, y, d = exgcd(m[0], m[i])
        if (a[i] - a[0]) % d != 0:
            return -1;

        t = m[i] // d;
        x = (a[i] - a[0]) // d * x % t
        a[0] = x * m[0] + a[0];
        m[0] = m[0] * m[i] // d;
        a[0] = (a[0] % m[0] + m[0]) % m[0]
        # print(a[0])
    return a[0];




import libnum

n =2   # 同余方程个数
a = [c1,c2]  # 余数
m=[n1,n2] # 模数

c=CRT(n,a,m)
p=libnum.gcd(n1,n2)
q1=n1//p
q2=n2//p
phi=(p-1)*(q1-1)*(q2-1)

d=libnum.invmod(e,phi)

m=pow(c,d,p*q1*q2)
print(m)
print(libnum.n2s(int(m)))