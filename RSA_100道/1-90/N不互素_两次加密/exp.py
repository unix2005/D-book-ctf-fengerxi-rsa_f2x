
import libnum
e = 65537
n1= 150385265883022810920531550970630108400430543818471500891590140199707649995501117348066774775184165792224937991344433983957573653027874840489304848195497009423451167471760779377182089223798345066725118315308855105107141561304474307498166446141583179467605566320989536938720233358985573268575155276402991154317
n2= 106498882115557018189370273061316655460477950197978282009613026952684980916076348240470149979526496634980863495388879465301117930724847841296622956930409511935157610009638964532186481476533717433545160920482713004034351440256533377478069533597494614250846195509814711493490656049090557995367091398042847809291
c = 34561944952062850364382557830751736854391559039860664899222552151184701276317668701704663262936204576039631410697930325961372518855538296824868114627687821333101614460575579760886055584340850598581117306570532634571689119867984167113417965053197028139669757572272462186421257144438230028016380359716460402816

p=libnum.gcd(n2,n1)
q2=n2//p
phi2=(p-1)*(q2-1)
d2=libnum.invmod(e,phi2)
c=pow(c,d2,n2)

q1=n1//p
phi1=(p-1)*(q1-1)
d1=libnum.invmod(e,phi1)
m=pow(c,d1,n1)
print(libnum.n2s(m))


