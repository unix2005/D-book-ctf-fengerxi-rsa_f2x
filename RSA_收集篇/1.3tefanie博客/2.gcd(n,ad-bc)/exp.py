
import gmpy2
from Crypto.Util.number import *

c= 34007465638566836660852768374211870538357285529060206826620688555044780516477877596651414637089490522614456532732711803500304737160162560168303462221485961593760966240770414498297915175227814336224871400766371471776600674705757656616409870237891336752248110367865552469248343708419900511716030176178698949179
n= 70043427687738872803871163276488213173780425282753969243938124727004843810522473265066937344440899712569316720945145873584064860810161865485251816597432836666987134938760506657782143983431621481190009008491725207321741725979791393566155990005404328775785526238494554357279069151540867533082875900530405903003
a0= 8369195163678456889416121467476480674288621867182572824570660596055739410903686466334448920102666056798356927389728982948229326705483052970212882852055482
a1= 8369195163678456889416121462308686152524805984209312455308229689034789710117101859597220211456125364647704791637845189120538925088375209397006380815921158
b0= 25500181489306553053743739056022091355379036380919737553326529889338409847082228856006303427136881468093863020843230477979
b1= 31448594528370020763962343185054872105044827103889010592635556324009793301024988530934510929565983517651356856506719032859
e = (n-pow(a0,2))//pow(b0,2)
p = gmpy2.gcd(a0*b1-a1*b0,n)
q = n//p
phi  = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
m = pow(c,d,n)
flag = long_to_bytes(m)
print(flag)
