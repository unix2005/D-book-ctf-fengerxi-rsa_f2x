from secret import flag
from Crypto.Util.number import *

e1 = getPrime(1024)
e2 = getPrime(1024)

n=20444526417914794739360784082872441939200982094133956211507153102817479055869323669053679860865424110510092824953311985928400599461286997088502822404396017300789062987007594375148602618741642244418631261619377550358297951668009601602861785542116818520338388766842255709742242218972716486781890003898642803551669943085930388582223210579815174046735541925076810987566530334632041458542101602808091868836754630323452277908866018208929968031623847911543481257000221284470600555490823811255989837594658944507503106071303688261679225076859237943515825791272707269346679066326272083374598330556540614967430706471055962543037

a = (e1*e2)&(~(e1-e2))|(~(e1*e2))&(e1-e2) 
b = (e1*e2)&(~(e1+e2))|(~(e1*e2))&(e1+e2) 

m = bytes_to_long(flag)
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print(a,b,c1,c2)

# (-9131066806178775074563442660598579270122471400095857643975089968880095513358803336376209113517019173972336997664021862720129680033001702088798583281103386257322436407067809704169707199188262693361757960624498771560546539919964041303109668589274121413059835007927422181652046410841311719845985881235942598259017937240495607941092817366912375808129646465443258466418596593804310547378618288251440878931422244332655811541102866389859937650088634359355706712094947110223423850883236500349733830033003999507059859560156102740469007354912173866345470907796707536144405770595801959170767353383658383791919217068164646054351L, 9131066806178775074563442660598579270122471400095857643975089968880095513358803336376209113517019173972336997664021862720129680033001702088798583281103386257322436407067809704169707199188262693361757960624498771560546539919964041303109668589274121413059835007927422181652046410841311719845985881235942598258848303277164279361414761951309875063742238680941129129811749805824808431907333760264310543546833130387703469297297753959032478020487539551804667487274640374689844322770130875681452806761311358368318802963106306125760405891297737634728773313788838096754643510492527059109357180227267991404643669541760438384831L, 8608893851673072472046228842579845729341646818235733152580182188411311633961853269819484428893389605969008904017109299061947689380746335730486027117033679250784938350314939430912541736264324233314106989271704236589435136992993198612670352888372509201806880362355411951379778440656051744338111300474407116356669764254956085650213734098687208147523022381832526322950017234973224898637693221003086736698531292389048058480238987780780646638556603051156800896173178780470951540416537302988384981163586849096321026028361849997434565605437016670946445173102163274927004308929011798215587633617852224081861152816330487744111L, 17605879558855808052278371627210479166506735031968646939406943822449423454291396047083818926165679630363819723678387802776613474576715178572221443205482791814491233487589391727579965574203978783263037600528551968237409832960074042197794564506889615156748695411011886221725902629862042632703504357404835001855377855068915818194566204137394124217335212980671134477431520826634975121052006333724558153404356449696433302111020062989699139309290505351309168837253942690114623294098258408074409972895652119631697140495853076954398640453974144676680611435277499502392711183744356450520802265096721676395931541786723381466013L)