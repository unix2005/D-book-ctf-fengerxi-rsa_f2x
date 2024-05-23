from Crypto.Util.number import *
import gmpy2
import time
import random
from tqdm import tqdm

e = 1801
p = 49610229352589717245227429186510630298995334563536199979797365135356894947505595171590737127611751124743823204969291853243936699113293137172961540731655194113111189561603261168928406442577570919901769348742992633428864861175880441682752947688509869668929473479230018031647980097396415380123118521799468844841
q = 21081926656979729045764441706195868361643779935106260715219328461497406780587336009385210898093496090213306812904410650499587043699660339207567766840318127296396962037273317168795761421233687815992929975284592353117739413561939283754964442896468496199833988666060155459156116345763999855126020972915904618043
c = 601596145172542477058917394071994325109856881057412872218601643742101914635753765731910337249806643258952637146341530783703613931109366648847232809553067941206928974141651198815184695746636818122414926015513095322872645068410957200062317958684872682628646759817233433643987003499153702624673493727886566639667597997520471371146056861227114668317633291934130573158877960548655006208725827943739971068608175370661619328559766977175575896437656636083179668805135271793023165492681941002853661303072959879197775224449456951125268328000206540965011249895216257583247180682482954741912101069920760903900864428405997751199
n = p * q


def AMM(o, r, q):
    start = time.time()
    print('\n----------------------------------------------------------------------------------')
    print('Start to run Adleman-Manders-Miller Root Extraction Method')
    print('Try to find one {:#x}th root of {} modulo {}'.format(r, o, q))
    g = GF(q)
    o = g(o)
    p = g(random.randint(1, q))
    while p ^ ((q - 1) // r) == 1:
        p = g(random.randint(1, q))
    print('[+] Find p:{}'.format(p))
    t = 0
    s = q - 1
    while s % r == 0:
        t += 1
        s = s // r
    print('[+] Find s:{}, t:{}'.format(s, t))
    k = 1
    while (k * s + 1) % r != 0:
        k += 1
    alp = (k * s + 1) // r
    print('[+] Find alp:{}'.format(alp))
    a = p ^ (r ** (t - 1) * s)
    b = o ^ (r * alp - 1)
    c = p ^ s
    h = 1
    for i in range(1, t):
        d = b ^ (r ^ (t - 1 - i))
        if d == 1:
            j = 0
        else:
            print('[+] Calculating DLP...')
            j = - discrete_log(d, a)
            print('[+] Finish DLP...')
        b = b * (c ^ r) ^ j
        h = h * c ^ j
        c = c ^ r
    result = o ^ alp * h
    end = time.time()
    print("Finished in {} seconds.".format(end - start))
    print('Find one solution: {}'.format(result))
    return result


def onemod(p, r):
    t = p - 2
    while pow(t, (p - 1) // r, p) == 1:
        t -= 1
    return pow(t, (p - 1) // r, p)


def solution(p, root, e):
    g = onemod(p, e)
    may = set()
    for i in range(e):
        may.add(root * pow(g, i, p) % p)
    return may


cp = c % p
cq = c % q
mp = AMM(cp, e, p)
mq = AMM(cq, e, q)
mps = solution(p, mp, e)
mqs = solution(q, mq, e)
for mpp in tqdm(mps):
    for mqq in mqs:
        ai = [int(mpp), int(mqq)]
        mi = [p, q]
        m = CRT_list(ai, mi)
        flag = long_to_bytes(m)
        if b'NSSCTF' in flag:
            print(flag)
            exit(0)