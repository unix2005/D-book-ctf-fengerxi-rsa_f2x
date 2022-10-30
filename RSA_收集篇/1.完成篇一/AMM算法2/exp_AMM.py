import random
import math
import libnum
import time
from Crypto.Util.number import bytes_to_long,long_to_bytes
p = 0
#设置模数
def GF(a):
    global p
    p = a
#乘法取模
def g(a,b):
    global p
    return pow(a,b,p)


def AMM(x,e,p):
    GF(p)
    y = random.randint(1, p-1)
    while g(y, (p-1)//e) == 1:
        y = random.randint(1, p-1)
        print(y)
    print("find")
    #p-1 = e^t*s
    t = 1
    s = 0
    while p % e == 0:
        t += 1
        print(t)
    s = p // (e**t)
    print('e',e)
    print('p',p)
    print('s',s)
    print('t',t)
    # s|ralpha-1
    k = 1
    while((s * k + 1) % e != 0):
        k += 1
    alpha = (s * k + 1) // e
    #计算a = y^s b = x^s h =1
    #h为e次非剩余部分的积
    a = g(y, (e ** (t - 1) ) * s)
    b = g(x, e * alpha - 1)
    c = g(y, s)
    h = 1
    #
    for i in range(1, t-1):
        d = g(b,e**(t-1-i))
        if d == 1:
            j = 0
        else:
            j = -math.log(d,a)
        b = b * (g(g(c, e), j))
        h = h * g(c, j)
        c = g(c, e)
    #return (g(x, alpha * h)) % p
    root = (g(x, alpha * h)) % p
    roots = set()
    for i in range(e):
        mp2 = root * g(a,i) %p
        #assert(g(mp2, e) == x)
        roots.add(mp2)
    return roots

e=65537
p= 12408795636519868275579286477747181009018504169827579387457997229774738126230652970860811085539129972962189443268046963335610845404214331426857155412988073
q= 12190036856294802286447270376342375357864587534233715766210874702670724440751066267168907565322961270655972226761426182258587581206888580394726683112820379
c= 68960610962019321576894097705679955071402844421318149418040507036722717269530195000135979777852568744281930839319120003106023209276898286482202725287026853925179071583797231099755287410760748104635674307266042492611618076506037004587354018148812584502385622631122387857218023049204722123597067641896169655595

import re


mps = AMM(c,e,q)
# print(mps)
for mpp in mps:
        solution = long_to_bytes(mpp)
        if b"moectf{" in solution:
            print(solution)