
from Crypto.Util.number import *
import gmpy2
import time
import random
from tqdm import tqdm
e = 65537
q= 12408795636519868275579286477747181009018504169827579387457997229774738126230652970860811085539129972962189443268046963335610845404214331426857155412988073
p= 12190036856294802286447270376342375357864587534233715766210874702670724440751066267168907565322961270655972226761426182258587581206888580394726683112820379
c= 68960610962019321576894097705679955071402844421318149418040507036722717269530195000135979777852568744281930839319120003106023209276898286482202725287026853925179071583797231099755287410760748104635674307266042492611618076506037004587354018148812584502385622631122387857218023049204722123597067641896169655595
n = p*q
def AMM(o, r, q):
    start = time.time()

    g = GF(q)
    o = g(o)
    p = g(random.randint(1, q))
    while p ^ ((q-1) // r) == 1:
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
    a = p ^ (r**(t-1) * s)
    b = o ^ (r*alp - 1)
    c = p ^ s
    h = 1
    for i in range(1, t):
        d = b ^ (r^(t-1-i))
        if d == 1:
            j = 0
        else:
            print('[+] Calculating DLP...')
            j = - discrete_log(d, a)
            print('[+] Finish DLP...')
        b = b * (c^r)^j
        h = h * c^j
        c = c^r
    result = o^alp * h
    end = time.time()
    print("Finished in {} seconds.".format(end - start))
    print('Find one solution: {}'.format(result))
    return result

def onemod(p,r):
    t=p-2
    while pow(t,(p-1) // r,p)==1:
        t -= 1
    return pow(t,(p-1) // r,p)

def solution(p,root,e):
    g = onemod(p,e)
    may = set()
    for i in range(e):
        may.add(root * pow(g,i,p)%p)
    return may

cp = c % p
mp = AMM(cp,e,p)
print('-------',mp)

mps = solution(p,mp,e)
for mpp in tqdm(mps):
     ai = [int(mpp)]
     mi = [p]
     m = CRT_list(ai,mi)
     flag = long_to_bytes(m)
     if b'moectf' in flag:
         print(flag)
         exit(0)

# moectf{Oh~Now_Y0u_Kn0W_HoW_RsA_W0rkS!}
