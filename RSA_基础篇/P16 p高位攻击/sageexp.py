# sage
import libnum

n = 13825843519571710873428859414579672354315071659439820628244472999485866649052110805457869338590187514116602837815124140432484262117371676976267721436244227104792863856722306533085878006249426437815405943285837409223882200429650139498565410193518318609186404321541002818447049590702693207093178119976930306188313389812258040902404991392273477524090663507230185854302508398487606160947861933574298409247029121725657976002346558116475950788745748638760678901488207720494815927253554983917627634826826305748104732049673766438361103134678640861807396808490547480920918122602522866517282598354247700246018620827186407222291
c = 8069176849119953284725698979637300857649466313773809113683642222085416457809259502704557882469560357376639733126836429991182536164084894508162647211766121557706947090701813794460382373772210944822854491223080171468124365453829931994686613388386398672952889685840411999135073540598959537338763755743580187011320135902778073983544957246842281172553032459418474893043913045926987625022043858637785478142565769241237336503137679001977264793413893322859182579535729775068010748011003277877267258462798570180414065271758061734676359804300115257687481351307213343011733330342628658103765597956044989311340712232509671201918
e = 65537
p1 = 109808212971964883545767217899164260396892558575747412957992952622503445366463665637485518479176308697194263286931473866511191437500214960131113514969332424915850812713465121027047280080223105730986925447033745115390014601545111178800361343308690136190170861353596131750311275899169955729432487964244199866368
kbits = 256


def phase3(high_p, n):
    R. < x > = PolynomialRing(Zmod(n), implementation='NTL')
    p = high_p + x
    x0 = p.small_roots(X=2 ^ kbits, beta=0.1)[0]

    P = int(p(x0))
    Q = n // P
    assert n == P * Q
    return P, Q


p, q = phase3(p1, n)
print(p)
print(q)
phi = (p - 1) * (q - 1)
d = libnum.invmod(e, phi)
m = pow(c, d, n)
print(libnum.n2s(int(m)))