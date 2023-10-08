
import hashlib
import gmpy2
import math
def  merge(a1,n1,a2,n2):
    d = math.gcd(n1,n2)
    c = a2-a1
    if c%d!=0:
        return 0
    c = (c%n2+n2)%n2
    c = c//d
    n1 = n1//d
    n2 = n2//d
    c *= gmpy2.invert(n1,n2)
    c %= n2
    c *= n1*d
    c += a1
    global n3
    global a3
    n3 = n1*n2*d
    a3 = (c%n3+n3)%n3
    return 1
def exCRT(a,n):
    a1=a[0]
    n1=n[0]
    le= len(a)
    for i in range(1,le):
        a2 = a[i]
        n2=n[i]
        if not merge(a1,n1,a2,n2):
            return -1
        a1 = a3
        n1 = n3
    global mod
    mod=n1
    return (a1%n1+n1)%n1

ms=  [317373385442325309490126978143569357540, 221713642615900754871455583169037656558, 196289364596638326277049734802446938300, 247061551433347435409823882059850553282, 323402141217785400810426086286247835137, 170316516030765512154283308705681130889, 238260825445985150121803064547287309573, 235008724579872652181722663904131823600]
cs=  [33294675495512365447936819977488986114,  167059006172538583650602409582350531874, 84260142588215759449080942199098236294, 187781777288843675003677762868332719566, 224545029830266627271846651706154185491, 90061147984988321355376057818169226157, 66745850796226643295313002664544925074, 71379202331049671317043059637642201894]

x=exCRT(cs,ms)
flag=hashlib.sha256(str(x).encode()).hexdigest()
while "4b93deeb" not in flag:
    x=x+mod
    #print(x)
    flag = hashlib.sha256(str(x).encode()).hexdigest()
    #print(type(flag))
print(flag)



