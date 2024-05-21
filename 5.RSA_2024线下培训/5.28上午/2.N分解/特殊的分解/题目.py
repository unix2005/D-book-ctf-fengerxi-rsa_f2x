import gmpy2
from Crypto.Util.number import *
from flag import flag

p = getPrime(1024)
q = gmpy2.next_prime(p + 1000000)
y = gmpy2.next_prime(q + 1000000)
x = gmpy2.next_prime(y + 1000000)
n = p * q * y * x

e = 0x10001
m = bytes_to_long(flag)
c = pow(m, e, n)

# n = 108299033965406365561943421701029190713946501560891630763244580970876141418060260848778356857818721003436668631051400046179714981563966629274135856263153393451778069603328236097645480852770563989641923335589213862076364231145680800763901480686502776051597843698725745250490425410650791537590877762849466754206792810298344723222757628527518527264424314398114603721700244387477600040173682904446101720469681389347684578169792444049955729491371539347527279510563843274956478643209577823959527009597138462178858908131459847477377873722809756286442989867841939264973938882747031165883664081728483968786444940130754090961440237029991537678198779446572379955612212432298032927533340075560342822842145491942842616840755357720456094746128021240483607459457623006697140665289210877036207570817593250015026853022025281118097723071897439283253998814746302023470665795337363626017807575053924858839475153327626709665036887169655539664145700068948907541640999554647851646028559453557061575683476442175156969842706373750319278039080406149444513435322207503611280827839170184405510258770955233545645043225793645367427485248583195703459681129854324595394957504455110811076379721049379749687264501324278652077596148357272587301352719972975920356014689
# c = 66282640807724405518602152114651879396246399255101507349038984047328959352691526384322744768659223247334455265432088028572041267042739221831533163642845861607636601193315832251590920339394500463075340397307285539327999953887797257215690304189880652964252216730150032533125189722147047967308850948061617857067650084515935365816313305482220299962756712272432126983038693515098931341954074787185153265911930069239124196604571305060210229630878593348542829381366929767819633918796746367100098078605770730971792477677209132590933799007758134578199207989520721360808705952397752948494796730262506568874816001910275456823816338446048730520807309148166369726421371597405903017279967140423776263708058900596532049999358296071238547707056598409574824286805346221039445037989664132260965906540515127261405823017822082554131040927683563314789126862678639503366941046116526326931102784127218794970747035858802637234772860038892015022384208812143488934424907981571536806616031983586579576340972689776331101818627661035148519372288555606365821757056616114258213545574963383005835374672572357290479551752690678352298990065015686456011474166705064061262970654778008504711084690127162113691996060192655389528709191383408755044112132008663979770115918


