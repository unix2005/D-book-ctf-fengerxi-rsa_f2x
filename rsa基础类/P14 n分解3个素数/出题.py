import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = gmpy2.next_prime(p)
r = libnum.generate_prime(512)
n = p * q * r
e = 65537
c = pow(m, e, n)
print("r=", r)
print("n=", n)
print("e=", e)
print("c=", c)
r = 12328943069972158868300333965019293732240349172933398867374450193780676916633106046545397891902123683693837126404908611670219604587587151306224914062663729
n = 928445951911850156618541782850215900925329423880533465612155142015978599609287623859912813317551629221695490535012732781489396534420011145723987610606038091488823086647363964394753700158320900867101659445170118179077194271099520502633316318889163873291574934282498061117736456183503867870294570083013883365868242889035609602940685335912371326827533418614992221705810476710807373254363162373986374486325350746366851935451369892949745302442034805629514003196071631
e = 65537
c = 327716655224470059950709685055600963837116578216483343492948888372401723689223347212508532985781828794786448842515029515358422017875793926582832247025212149474404973170422295165602666360784347416812528617973764432916955654602356835327769633635513894485943553309743509322858937973710628023758816806471875016815994664897320150855163109437521642800230902661034555151514311149333258071668655344069451897282357234220538922127548822361859943829665459953651351620958628
