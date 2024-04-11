import libnum

r = 7996728164495259362822258548434922741290100998149465194487628664864256950051236186227986990712837371289585870678059397413537714250530572338774305952904473
M = 4159518144549137412048572485195536187606187833861349516326031843059872501654790226936115271091120509781872925030241137272462161485445491493686121954785558
n = 131552964273731742744001439326470035414270864348139594004117959631286500198956302913377947920677525319260242121507196043323292374736595943942956194902814842206268870941485429339132421676367167621812260482624743821671183297023718573293452354284932348802548838847981916748951828826237112194142035380559020560287
e = 3
c = 46794664006708417132147941918719938365671485176293172014575392203162005813544444720181151046818648417346292288656741056411780813044749520725718927535262618317679844671500204720286218754536643881483749892207516758305694529993542296670281548111692443639662220578293714396224325591697834572209746048616144307282

PR.<x> = PolynomialRing(Zmod(n))
f = (M + x*r)**e - c
f = f.monic()
k = f.small_roots()
m = M + k[0]*r
print(libnum.n2s(int(m)))