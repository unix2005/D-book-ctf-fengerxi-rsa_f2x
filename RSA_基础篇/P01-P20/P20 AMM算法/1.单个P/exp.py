import random
import math
import libnum
import time
from Crypto.Util.number import bytes_to_long,long_to_bytes
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
    #p-1 = e^t*s
    t = 1
    s = 0
    while p % e == 0:
        t += 1
        print(t)
    s = p // (e**t)
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
def check(m):
    if 'flag' in m:
        return True
    else:
        return False
e = 997

p = 169192804045017094881483391290948160084538928031716323749363864952453968973507689162051165395748104110078160856791051809212190939432475142974911541618441458487669050818296365973889691415623806933502603345031427784795571665740530721508383685794846991682950112717404480456329219127191697671498037366841158723543
q = 107516396467746261711633898678341416690878446946218041251896502835689317784482747676107795221812916591321630759086326505565275611515776242892889358779953138176525964380991025435521861396436904104071935067377647496422254521013295763929078451759522826104921925202219553793049032407587608850233803508977340633609
c = 7296955328866123806615327249732627185102404227332181196296735121223965109231156544280256472492779759505533523060928048594910557437933201943976173955148680274140829916070075759044441331615135242760488256932238858269529909634447825461421412145996149026770528870738269768868586920051310346790350630656242240675615378779267818783700730455951708072880647986805110335263926177449091704517836266354071222826319675028232152825498040408774211261689801412297908590166114832939080331783731498956480608994534272354837899909567113733994622681549792329747132730450648055557829163328285671440063040320192447007187073122676185153708


mps = AMM(c,e,q)
# print(mps)
for mpp in mps:
        solution = str(long_to_bytes(mpp))
        if check(solution):
            print(solution)