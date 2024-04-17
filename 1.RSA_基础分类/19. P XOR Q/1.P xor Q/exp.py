import gmpy2
import libnum

n1 = 129760065142536809806311204132351918751028992005460856468227287921282870916288856718621153143496403712311222567870977852134806106569337746575721004212669688720934096637000255747173695182744851724877533272723548422615077582025310964380370466630967534492769138475503800139599085157646896457701207621103799125719
x1 = 2535073000605892935644131126185024717717589486004324795337079143504448380472644470690389542009724270615702616436360436628913170173803134221956364909472182

x1 = bin(x1)[2:].zfill(512)


pre_sol = [(0, 0)]
for x in range(512 - 1, -1, -1):
    cur_pow = pow(2, len(x1) - x - 1)
    print(cur_pow)
    cur_sol = []
    for p, q in pre_sol:
        for i in range(2):
            for j in range(2):
                if str((i + j) % 2) == x1[x]:
                    cur_p = p + i * cur_pow
                    cur_q = q + j * cur_pow
                    if cur_p * cur_q % pow(2, len(x1) - x) == n1 % pow(2, len(x1) - x):
                        cur_sol.append((cur_p, cur_q))
    pre_sol = cur_sol

for p, q in pre_sol:
    if p * q == n1:
        print(p, q)
        break
n=n1
e=65537
c=26506766042158812153297659888261605602209965867219470797339092764667310960930283597295284822004032161597620439172538662557297590428638492713429290901250304462610596251465067375290997078433094559619684696433561726225388148663591424284892872454430710006263385391764878130290791647310468786580792375046884367243
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
print(libnum.n2s(int(m)))