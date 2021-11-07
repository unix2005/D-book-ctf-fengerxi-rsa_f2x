import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 3
n = p * q
c1 = pow(m, e, n)
c2 = pow(2022 * m + 2021, e, n)
print("n=", n)
print("c1=", c1)
print("c2=", c2)
n = 14878649872127265598577310327906463595445694442874089795687255281538461872507302213106609252847683579168034165663848207247237543878434015753285820194626800282560106819324725018489799552817816357482707023208419773917552268593373266051925536823803922433826289681775091352739327068547898980980073772614794356799549887748179096814913218045652008996246897307599980509782851636741975770977621764836822844526917297449348396463498159059942283279937461265130763691271200145989215858421263513036329692599828739213845425872881926104230192768184772597911629323901226447821509143884759631327016403851417477302786822694718560058407
c1 = 175676150266618239508960526375830661715292695339479889213804234972236462741647787911646459062650145646715037789068457022000633309221436502994229482255499464114071284485035672268297610232784725624147018434613265515082923894826193542573259322814615044856922994261638278977211750347399632281012125376134757
c2 = 1452299739943355429620598102750144850501685988709347628843015433896415487158634337543587442222354838823916396917992859098096943617196325746698151841054343769923746178474076881188330275543501263415546830735826280866312328010914970316027841516534872949166723592426026231369229170099785732462711391063503783886347563
