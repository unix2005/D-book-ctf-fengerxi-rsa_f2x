
n =8783117353228609820060025773720048836109116296720444291318682193328216575376903671782151675801584925066872219021319381163804239505579013818679255656402117567158378369967703317919205364480806143209934093723468591544792794708122025724968669241594029740047941933910596214170603520800531302474255823072859735679699558933009869241259760910402379740926512037606096020308081609477145816657118917642443176163860564823645522254412566891344745856141731910712040298787696382973824645074768059896153817964229975814742137600918515702471008251376697190058997187350022140633621955761877009643524289144711721902192261617574896449017
flagenc =1832021020586052459314800741399454951500982061634041208695770794636942946870944684781204845687614819955481692885982545657535952608100558061853098768890990198808258902800083671402999197944855469054517686346352932015639347886120547093778527571008483890754044661117042113616196224634409728684137167049242919543742476300792865668127981523314258326046469003175979484948578219765126696355000799390683333335678236115175267218556919253045561467791607635318317825080003594243366362225620291777807071774013296604063473075790067769213249767073197915283384750139985842145668772180552896467043807903712438253502782564391233381742
c1 =7501185876834032332235110133210399479682524972321262801050956129090974843598848916000280794969942298848478394986779571489577405391165372124215072990382219817624500948789393550575823082225944683449240150364401487955484843961943987266467050723988657081468393104862383181698999645914573683498375228946881234015678337769955671069215094086232377038727627179660862997067062391991524231807127953937881102711759932207432989764529075450526104070640765094626829603546052250863300827172150912585791552174463067989228539713261075253602907390439036055716154404417991482262846355144755622306307102084492476950657455416297047328320
N =29956031606905964747690208452463077877156885038545111351508842927295510069375356079358289621922278316223452695576175299757472345749152582617292471487006177231261463793638998998552474423214925625798531662484883149899251884707864709821973208465998076621327151198438158796296778838657562126343551661323471767755161686549607991960624754677443327266743771304424298446433734879681913848286620429175461870451099771965936783237191184798864363652633155779478727580408625494617809961465590055999661472563150275608218351797354628429061984878432442357241449134341597647749840966740944318445550768334070331490455379767889443973947
E =3527492693
c2 =11237333233288323887902003767693284822911839921763421974808265907264411495367936669799604082222415065052099486867383635886650443299459413288200494593477575168578514325691333043832168789236017314435940348619410775859032696755081680003338452277759483862961120696587307757666691557048088894021864124052243936836752825473836552342254367444581003605318145868368417247224184184040226260236268012375524575700053732026218766291274077482132408824236096242385408780811520890742688121731805867574680433796282417791570436991022839930635640379142355212121030479526679958801911687722402447690578345774902440346290388183936888977900

import libnum
import gmpy2
#c1 = pow(e2, 17, n)
def exp(n, e, c):
    k = 0
    while 1:
        m1 = k * n + c
        m, t = gmpy2.iroot(m1, e)
        if t:
            return m
            break
        k += 1
e2=exp(n, 17, c1)
print(e2)

#c2 = pow(d2, E, N)

p2 = 173078108398797693665135881829236075381385640386270681597614075449385160047192826549689858183180936639070064309925929218966667262650552855318783567546131862440848767306600252044834602371191453881522882233745590790067041490962165388372445595736465527512700919336312857203007896777270237470242797091626699715021
q2 = 173078108398797693665135881829236075381385640386270681597614075449385160047192826549689858183180936639070064309925929218966667262650552855318783567546131862440848767306600252044834602371191453881522882233745590790067041490962165388372445595736465527512700919336312857203007896777270237470242797091626699712807
phi2=(p2-1)*(q2-1)
D=libnum.invmod(E,phi2)
d2=pow(c2,D,N)
print(d2)

#已知e,d,n,分解n
import random
def divide_pq(e, d, n):
    k = e * d - 1
    while True:
        g = random.randint(2, n - 1)
        t = k
        while True:
            if t % 2 != 0:
                break
            t //= 2
            x = pow(g, t, n)
            if x > 1 and gmpy2.gcd(x - 1, n) > 1:
                p = gmpy2.gcd(x - 1, n)
                return (p, n // p)

p,q=divide_pq(e2, d2, n)
print(p,q)

phi_n=(p-1)*(q-1)
#求逆元
d=libnum.invmod(65537,phi_n)
m=pow(flagenc,d,n)
print(m)
#数字转字节，转字符串
print(libnum.n2s(int(m)).decode())