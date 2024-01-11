
import random
from Crypto.Util.number import long_to_bytes

def AMM(o, r, q):

    g = GF(q)
    o = g(o)
    p = g(random.randint(1, q))
    while p ^ ((q-1) // r) == 1:
        p = g(random.randint(1, q))

    t = 0
    s = q - 1
    while s % r == 0:
        t += 1
        s = s // r
    k = 1
    while (k * s + 1) % r != 0:
        k += 1
    alp = (k * s + 1) // r
    a = p ^ (r**(t-1) * s)
    b = o ^ (r*alp - 1)
    c = p ^ s
    h = 1
    for i in range(1, t):
        d = b ^ (r^(t-1-i))
        if d == 1:
            j = 0
        else:
            j = - discrete_log(d, a)
        b = b * (c^r)^j
        h = h * c^j
        c = c^r
    result = o^alp * h
    return result

def findAllPRoot(p, e):
    proot = set()
    while len(proot) < e:
        proot.add(pow(random.randint(2, p-1), (p-1)//e, p))
    return proot

def findAllSolutions(mp, proot, cp, p):
    all_mp = set()
    for root in proot:
        mp2 = mp * root % p
        assert(pow(mp2, e, p) == cp)
        all_mp.add(mp2)
    return all_mp


c = 15433214846771804225704093824935372144929516863829752998270111032551363583267576397009018518790803908369965458162930857063271509296349091229352855725285388975497906340053281554202527432848881160125418406408621879995822551367228501163128699032015069585502994319524445505522625561831240862136447585120010288772692097621553249775117843166714346924868089146429002417223863834435968726551668931140147337199939823985783939085842479154589529244209712172799274024573845157268545992888944742377166586536479490962335287124809557709167220756920767331929168230518135523463578566851417486746667008938122693256033127001185017237773
p = 0xa892eb59b175bcf896be2176598f278437fe10ef032279f06e1092143acfb3c16b31811cca5286699595c2720c652ee64f8adc92c8b16a5601dd981d6f839ce9c0513db30de88c2ec6cae1a726acbd235ea946631bde633707d766287a2f075e9aace1606bd8b4f52d4f5b87dfb81f14fbc5338004575e9430257e180a169eff
q = 0xe3d47225b77e56129dc3fed716181845f89fa15b2eb35453ffdc0f05cdf57c0d90410911d209818e886b202bc4893ebe85a07ef670122f0e70092de1b7963c3b24a58c6a9ec9ed677db3473b1882d10d550e45c18fd57b85a70a5401a074d36760e85c7e6258f0ab08fa69cd433709910fad6e145f7b85f589e83d61d3baf6ad
n = p * q
e = 0x3
cp = c % p
cq = c % q
mp = AMM(cp, e, p)
mq = AMM(cq, e, q)
p_proot = findAllPRoot(p, e)
q_proot = findAllPRoot(q, e)
mps = findAllSolutions(mp, p_proot, cp, p)
mqs = findAllSolutions(mq, q_proot, cq, q)
print("mps=",mps)
print("mqs=",mqs)


flag = []
for mpp in mps:
    for mqq in mqs:
        solution = CRT_list([int(mpp), int(mqq)], [p, q])
        flag.append(solution)
print("flag=",flag)

for i in range(len(flag)):
    assert (((flag[i] ** 3)) % n == c)
    f = long_to_bytes(flag[i] - p)
    if b"DAS" in f:
        print(f)
        break
    else:
        print("No flag.")
        continue
