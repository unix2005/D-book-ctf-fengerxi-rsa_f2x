from Crypto.Util.number import *
import gmpy2
from sympy import  *

n = 20955464633057600258987829727550073699845816289000240676927869818926752810905511184835302717855745473943671910742784074561535017974853574714483642916831791020944940633062963043482236587316552330558006573820423830770910893877191630012247591380869307656539553888318621170921800017818132160253923739647771452839191101104391894609403591447166963426444018303147924843072923713248135717578047687411974516038299879758561542241544862102935741869647633013298181782208467117482306148238724598730801037692668154263059348953587766571379262442743822007387408949824805991797355089583176028081305319076896384126383926193964322235633
c = 14815997295683082265558346455845370590765145583224067337292601455640475216349267044144296003388877395546880235511728120803143112914764263292087421926972160283428440959367872665892349776616002018624301524264223581314248857537034849571849747613963209414193510408342387107662655487869098045345428379025731617851483935711671021438908270746316921057871871545763798735895118697635903815383424855759281301248295597297869474539060531099443223045844791615425429748703429968627505406271675074549912664863784774239200764403372298995457799473112713379340870305136776932539188516395526955161359417473843082895317392495109895085666
s = 14728527428626630951705148488338433865446345521255631461200851513782412494843597938863837697938230856843797646287742397249258609197032095158567448934855031190354034543862057663422053672290704598313096289223478302733688501373756860855445632789922930577582465209872782549135254792729915747104521949095814028476908208917363509089190935273004331739978623136706041729628143765893264698948654175039064609891374587695812144855411176143224066975193255513405865992328257766815240718115442741846443490733767716842367336385132648983241895710001620533668392060358573295789752856876282590472528110546264872047138094995909454134250
e = 65537
m1 = gmpy2.invert(s,n)
p,q = symbols('p q')
eq = [p*q-n,900*p - 218*q-m1]
result = nonlinsolve(eq,[p,q])
result = list(result)
p,q = int(result[1][0]),int(result[1][1])
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
lost_n = pow(c,d,n)
print(lost_n)