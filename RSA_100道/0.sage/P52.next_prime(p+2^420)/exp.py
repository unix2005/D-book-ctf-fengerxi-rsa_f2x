

#
# e = 101684733522589049376051051576215902510166244234370429058800153902445053536138419222096346715560283781778705047246555278271919928248836576236044123786248907522717751222608113597458768397652361813688176017155353220911686089871315647328303370846954697334521948003485878793121446614220897034652783771882675756065
# n = 106490064297459077911162044548396107234298314288687868971249318200714506925762583340058042587392504450330878677254698499363515259785914237880057943786202091010532603853142050802310895234445611880617572636397946757345480447391544962796834842717321639098108976593541239044249391398321435940436125823407760564233
# c = 92367575354201067679929326801477992215675304496512806779109227230237905402825022908214026985431756172011616861246881703226244396008088878308925377019775353026444957454196182919500667632574210469783704454438904889268692709062013797002819384105191802781841741128273810101308641357704215204494382259638905571144
#
#
# import gmpy2
# import libnum
# import sympy
# x=2**420
# tmp = n - x
# p, s = gmpy2.iroot(tmp, 2)
# while 1:
#     print(p)
#     p=sympy.prevprime(p)
#     if n%p==0:
#         print(p)
#         break
#     if p*p>n:
#         break

from Crypto.Util.number import *
from gmpy2 import *
p = getPrime(512)
print(p)
q = next_prime(p + 2 ** 420)
#print(q)
n=p*q
tmp = n - 2**420
p1, s = iroot(tmp, 2)
print(p1)
print(p1-p)