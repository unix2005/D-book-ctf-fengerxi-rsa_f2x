from Crypto.Util.number import *
import uuid
flag = 'flag{'+str(uuid.uuid4())+"}"
flag=flag.encode()
import gmpy2

p = getPrime(2048)
q = gmpy2.next_prime(p)
for i in range(3600):
    if i%100 ==0:
        #print(i)
        q = gmpy2.next_prime(q)

n = p * q
e = 0x10001
m = bytes_to_long(flag)
c = pow(m,e,n)
print("c=",c)
print("n=",n)

c= 672211618947965669743140453815925311571913536792006320455451623329504768032653294195423386000169883889423130760702613901378226812991253672513808102582219125394975375184975680670477893616071731840578283372003364948041569480819988957797304000908767353945393438677325246806404776535366574244075168385686413998057429677446479345637389931707590541292174569539214514406772616679574446429577154994658300264395963743399028585579405127133850937684035755385536903177249615680095525438385801267848518932540742850864828339907387436386589615141301315094268048540705754105909152114279580297245086066527476038499949395262133426884691004953583259542925926790804058362169131721101062567084072161757158556850613589003126629288335943625835227353239228779420777075183829735033060565964497198340990191457681711972006273381600852029426480042505732976038791175365941723190939561137761147915067500934001302644947570092730510410631121938241136026914524548262047531029183007578603005500736114268512900086177419819102734670936080786880709408049475188517563383396936699006425388577265810859020768191320288121742321413664684223757832512232195144286087827718142083017087556701405737637649721698260338198824299502881114161665693663517201464044647997804424204974158
n= 720239742676276892125180297266754203107040753393792061819109788620051632698640388878164710563582551395398417339060158866293057237682628696160289176629921331485290769277668335946098043360398735897380648863281934217401247716885835600015902679721336644611726200751169780657177537142181503044265719975692160293076414714427014863104317576606190229434103615882007838099640939570363751985038883738622768287033043747426059699658000045440922380571398371705698665874788485742224933932126886052739997477581453575568873105033061557099207861338425715849944147722082093066073450898210944979122392845654525731562948599513722685350626329020621203929679566003766926450933409172107168029480058053562850582746440505733686649603099598891890233020681944859657534362524449703843503708875743380789764830334189231182948902486001101574574542624002055351308194659501208428214278013747062791484983332159726081847473539435746845527406013789541657402799211822281010775911725885529125479685615597338584834382753602860489834851310346307067835494249861848527198787408591551265511901573927692939919503175252790601381174213220684859419625471536435635703766410175026305548524401754345447084444023478365533640647989603192253820896160603674343007718854266899300948742261
