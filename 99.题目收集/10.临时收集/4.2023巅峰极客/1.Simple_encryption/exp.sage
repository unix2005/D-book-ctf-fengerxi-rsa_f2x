
# sage
A=[16384, 16641, 16900]
B=[1024, 1025, 1026]
C=[512, 513, 514]
M=[70105864201789081448341323173168814626290331977226399010985718339864141790250496, 295174996474963104919770605739942482686775346823742034261282804762108447183558389, 21938794596119327323920598114656453572273597393994712550717124961084111931664796]
S= 234626762558445335519229319778735528295
n=28053749721930780797243137464055357921262616541619976645795810707701031602793034889886420385567169222962145128498131170577184276590698976531070900776293344109534005057067680663813430093397821366071365221453788763262381958185404224319153945950416725302184077952893435265051402645871699132910860011753502307815457636525137171681463817731190311682277171396235160056504317959832747279317829283601814707551094074778796108136141845755357784361312469124392408642823375413433759572121658646203123677327551421440655322226192031542368496829102050186550793124020718643243789525477209493783347317576783265671566724068427349961101
x, y, z = var('x y z')
equation1 = A[0]*x**2+B[0]*x+C[0]==M[0]
equation2 = A[1]*y**2+B[1]*y+C[1]==M[1]
equation3 = A[2]*z**2+B[2]*z+C[2]==M[2]
equation4=x+y+z==S
solutions = solve((equation1, equation2, equation3), x, y, z)
for solution in solutions:
    print(solution)


import gmpy2
from Crypto.Util.number import *
c1= 19024563955839349902897822692180949371550067644378624199902067434708278125346234824900117853598997270022872667319428613147809325929092749312310446754419305096891122211944442338664613779595641268298482084259741784281927857614814220279055840825157115551456554287395502655358453270843601870807174309121367449335110327991187235786798374254470758957844690258594070043388827157981964323699747450405814713722613265012947852856714100237325256114904705539465145676960232769502207049858752573601516773952294218843901330100257234517481221811887136295727396712894842769582824157206825592614684804626241036297918244781918275524254
c2= 11387447548457075057390997630590504043679006922775566653728699416828036980076318372839900947303061300878930517069527835771992393657157069014534366482903388936689298175411163666849237525549902527846826224853407226289495201341719277080550962118551001246017511651688883675152554449310329664415179464488725227120033786305900106544217117526923607211746947511746335071162308591288281572603417532523345271340113176743703809868369623401559713179927002634217140206608963086656140258643119596968929437114459557916757824682496866029297120246221557017875892921591955181714167913310050483382235498906247018171409256534124073270350
N= 21831630625212912450058787218272832615084640356500740162478776482071876178684642739065105728423872548532056206845637492058465613779973193354996353323494373418215019445325632104575415991984764454753263189235376127871742444636236132111097548997063091478794422370043984009615893441148901566420508196170556189546911391716595983110030778046242014896752388438535131806524968952947016059907135882390507706966746973544598457963945671064540465259211834751973065197550500334726779434679470160463944292619173904064826217284899341554269864669620477774678605962276256707036721407638013951236957603286867871199275024050690034901963
g1= 20303501619435729000675510820217420636246553663472832286487504757515586157679361170332171306491820918722752848685645096611030558245362578422584797889428493611704976472409942840368080016946977234874471779189922713887914075985648876516896823599078349725871578446532134614410886658001724864915073768678394238725788245439086601955497248593286832679485832319756671985505398841701463782272300202981842733576006152153012355980197830911700112001441621619417349747262257225469106511527467526286661082010163334100555372381681421874165851063816598907314117035131618062582953512203870615406642787786668571083042463072230605649134
p = (gmpy2.gcd(g1-1,N))
q=N//p
def decrypt(c1, c2):
    xp = c1 % p
    xq = c2 % q
    m = (xp*inverse(q, p)*q + xq*inverse(p, q)*p) % N
    return m
m = decrypt(c1,c2)
m=long_to_bytes(m)

N= 28053749721930780797243137464055357921262616541619976645795810707701031602793034889886420385567169222962145128498131170577184276590698976531070900776293344109534005057067680663813430093397821366071365221453788763262381958185404224319153945950416725302184077952893435265051402645871699132910860011753502307815457636525137171681463817731190311682277171396235160056504317959832747279317829283601814707551094074778796108136141845755357784361312469124392408642823375413433759572121658646203123677327551421440655322226192031542368496829102050186550793124020718643243789525477209493783347317576783265671566724068427349961101
e= 5
Cs= [1693447496400753735762426750097282582203894511485112615865753001679557182840033040705025720548835476996498244081423052953952745813186793687790496086492136043098444304128963237489862776988389256298142843070384268907160020751319313970887199939345096232529143204442168808703063568295924663998456534264361495136412078324133263733409362366768460625508816378362979251599475109499727808021609000751360638976, 2240772849203381534975484679127982642973364801722576637731411892969654368457130801503103210570803728830063876118483596474389109772469014349453490395147031665061733965097301661933389406031214242680246638201663845183194937353509302694926811282026475913703306789097162693368337210584494881249909346643289510493724709324540062077619696056842225526183938442535866325407085768724148771697260859350213678910949, 5082341111246153817896279104775187112534431783418388292800705085458704665057344175657566751627976149342406406594179073777431676597641200321859622633948317181914562670909686170531929552301852027606377778515019377168677204310642500744387041601260593120417053741977533047412729373182842984761689443959266049421034949822673159561609487404082536872314636928727833394518122974630386280495027169465342976]

M=[]

for i in range(len(Cs)):
    k = 0
    while True:
        m1=Cs[i]+k*N
        flag=gmpy2.iroot(m1,5)
        if flag[1]:
            M.append(int(flag[0]))
            break
        else:
            k+=1

x =65413472431888815878902893901773169457
y =133183392452574799979498526266539842331
z =36029897673981719660827899610422516507
x=long_to_bytes(x)
y=long_to_bytes(y)
z=long_to_bytes(z)
print(m+x+y+z)
# b'flag{f561fafb-32ce-9d16-18fa-ec795fc1d208}'