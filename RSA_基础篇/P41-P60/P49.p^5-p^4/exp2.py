
from Crypto.Util.number import *
import gmpy2

#因为p和q都是512bit长度，且已知hint=p**5 - q**4，p**5远大于q**4。由此我们可以直接对hint开5次方得到near_p，
# 此时near_p<p我们再循环取near_p的下一个素数，直至n可以整除near_p为止,此时p=near_p，则q=n//p。

n = 76236418318712173274495941060488893810931309177217802334230599201457092723011685048556311576262486371987147895332408646920500226769161418792142565209634495797142268681403865426056588605013602625268553194169434049817172340173907696496945054049859221379092764811535206778031226535614731731322630330166833765943
e = 65537
c = 7207616060389865156270906240837846478541820008527247539698331406253371238674590766101711421196342768182325013873320402422918804780590951789425587131632422554819735000106070325708057225062376701298825910565526713270553888227235612227223162695870584803109353377288421750982913226189395526612487664144379690552
h = 130285072635228037239175162118613869214302695058325046962039091162567931492116336918638092534964417960274466351834311039222269165021532950982276262717322395682559639859781516047319178212473103057947426886870612637975024605166325017663998263834789814181250953051730859433354534450232382414565421858172075431133498326501045697132640582932453817599366612200146802110424409285814189125929844293789544163802323048780585398714263586547670912817768592459281775837372982750626103047573532664320692775783627129463700810934670066747044799514243631607384814191188276380589420289084574680852618867732847029105400406874790675559126905078326495799755425006555539699119063191489852930421412630857588890593040420277938268954008973405431053073576987401154763326417551463323055736754390446
near_p = gmpy2.iroot(h,5)[0]
while n%near_p !=0:
    near_p =gmpy2.next_prime(near_p)
p = near_p
q = n//p
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))
