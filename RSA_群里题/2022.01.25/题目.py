#coding:utf-8
import gmpy2
from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
e = getPrime(32)
n = p*q*r
phi = (p-1)*(q-1)*(r-1)
d = gmpy2.invert(e,phi)
dp = d%((q-1)*(r-1))
dq = d%((p-1)*(r-1))
dr = d%((p-1)*(q-1))
flag = 'flag{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}'+PADDING
m = bytes_to_long(flag.encode())
c = pow(m,e,n)

print(p)
print(q)
print(r)
print(dp)
print(dq)
print(dr)
print(c)

p=12922128058767029848676385650461975663483632970994721128398090402671357430399910236576943902580268365115559040908171487273491136108931171215963673857907721
q=10395910293559541454979782434227114401257890224810826672485874938639616819909368963527556812339196570118998080877100587760101646884011742783881592586607483
r=8104533688439480164488403019957173637520526666352540480766865791142556044817828133446063428255474375204188144310967625626318466189746446739697284656837499
dp=73360412924315743410612858109886169233122608813546859531995431159702281180116580962235297605024326120716590757069707814371806343766956894408106019058184354279568525768909190843389534908163730972765221403797428735591146943727032277163147380538250142612444372315262195455266292156566943804557623319253942627829
dq=40011003982913118920477233564329052389422276107266243287367766124357736739027781899850422097218506350119257015460291153483339485727984512959771805645640899525080850525273304988145509506962755664208407488807873672040970416096459662677968243781070751482234692575943914243633982505045357475070019527351586080273
dr=21504040939112983125383942214187695383459556831904800061168077060846983552476434854825475457749096404504088696171780970907072305495623953811379179449789142049817703543458498244186699984858401903729236362439659600561895931051597248170420055792553353578915848063216831827095100173180270649367917678965552672673
c=220428832901130282093087304800127910055992783874826238869471313726515822196746908777026147887315019800546695346099376727742597231512404648514329911088048902389321230640565683145565701498095660019604419213310866468276943241155853029934366950674139215056682438149221374543291202295130547776549069333898123270448986380025937093195496539532193583979030254746589985556996040224572481200667498253900563663950531345601763949337787268884688982469744380006435119997310653


