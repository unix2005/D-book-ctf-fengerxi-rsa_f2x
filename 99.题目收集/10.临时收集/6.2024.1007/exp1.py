


n1=9993095174491861722136903748298297709412902279302520139233078581728955341092359812576382945917721030218891721862866727091533422540383093057822489980507850401035624139838801700503555063600665154749088425482688189748265222941861354594269322865779044794362726063016847670325638897242582767816160447735248702211385253328830024633364023243711204481171987244862131950207806849919784142585009984248253708502464629068311983990934631001376844711337084543784145584247535612255122616680834143198711074949565393352718402194083696074632410955065738514371934182994346662524587105003492788531230255604154146997461875549449435352613
c1=6491645795573717294817971718119197425888563460820052740042921250836387737541767330028774831922632421591644289695852367880360345021855890270818764603553059175778082898940349441767306666270179299410995824536010640225877826068254687357489965894361406719928580541539474658009461746707109054905195663038248896454574912330193397108400150873415269829088168747464920289541648618753195863950514346080764233087980073988745755744014193366652973830004993794412657941051163712910568005366724882942741839047940165371669483394624453374613262475711525946466493513267914409465206131976599259672108557387739801639544073866274784356977
h=7529903766593789743203875105811805590623403238134744358069916057185419385329205467611860033764294674989772542073704729511422796271394307069883815525621236738350503410660419587759413356127716975834456703488074104519089921283629702825586315080664842218066710642563785449929868455613767740965885508578869787571827611317007683871913598070468433776708525736366268459334720410018972959397204686070137997198646315659212528936425343257899533854439580019931764644057337591761642720389438391799239426602950793694656030045650827200916728845532896403874871702260897080640969380062568182811783431664452646773160530412795171867089
n2=48896533771865940172408482269495841213573804280667769321916763781170714489171413360830436903902514764894457203162974796537361136022041750488725760741233431888006422130065207427205955432477233464492319581924197421892619323245763188452030765972686031120042342088391557818361164377353080215440224398615708457979
c2=27761925140718394623677431041293505328490905505559515102893219919578636302158822719530123006546241820313512673447588589579358875282500865927759284093905467144664009117201326815763043390222260499908901633928587645583844675618927963145554745146887296951205970215420052456076089002696712924617638209737744510870
c3=43715978264074536089998502714696599120075311927007160736414403690767258228182302094211457982694002328282904586924034286237416150152638683498883249396452385100627664897623012777387817004904719999424014002347489403727189155676320600693899241470529282521488819279690007581921187455397776348749923718168574660987
e = 65537
import libnum
import sympy
# hint*(1024*p1 - 197*q1)%n1=1
# 逆元的方式 求出 1024*p1 - 197*q1

h1=libnum.invmod(h,n1)

p1 = sympy.symbols('p1')
q1= sympy.symbols('q1')
f1=p1*q1-n1
f2=1024*p1-197*q1-h1
p1,q1=sympy.solve([f1,f2],[p1,q1])
print(p1,q1)
print(q1[0])
q1=97081990903922528963749496431449712257081844320970002991593538599949332716969875293145807478280197620783288413338790111837983722113525778267222924551475232766278239674233668750436961825666257483368142977765157841046703358501945482720203786590201484402305481506472206452311762557161027699985792370618868662411
p1=n1//q1

phi1=(p1-1)*(q1-1)
d=libnum.invmod(e,phi1)
m=pow(c1,d,n1)
print(libnum.n2s(m))


p2=libnum.gcd(pow(c2,n2,n2)-c3,n2)
print(p2)
q2=n2//p2
phi2=(p2-1)*(q2-1)
d=libnum.invmod(p2,phi2)
m=pow(c2,d,n2)
print(libnum.n2s(m))