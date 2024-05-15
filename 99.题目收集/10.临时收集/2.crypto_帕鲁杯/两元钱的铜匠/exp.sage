

n = 80916351132285136921336714166859402248518125673421944066690210363157948681543515675261790287954711843082802283188843248579293238274583917836325545166981149125711216316112644776403584036920878846575128588844980283888602402513345309524782526525838503856925567762860026353261868959895401646623045981393058164201
N = 175887339574643371942360396913019735118423928391339797751049049816862344090324438786194807609356902331228801731590496587951642499325571035835790931895483345540104575533781585131558026624618308795381874809845454092562340943276838942273890971498308617974682097511232721650227206585474404895053411892392799799403
leak = 161177488484579680503127298320874823539858895081858980450427298120182550612626953405092823674668208591844284619026441298155371399651438065337570099147890081125477609238234662000811899869636390550619251741676887565983189442613760093303841954633720778312454175652907352477365434215186845209831284593041581382419
a = pow(9999, 66666,N)
b = pow(66666, 9999,N)
P.<x> = PolynomialRing(Zmod(N))
f = a*x^2 - leak*x + b*n
x = f.roots()
print(x)
p=7369460226203218007291482683484122432673051660657739743165520029005169640619453357512790807095244300800591778614929551073202263581117660350621325493923101
q=n//p
c=22730301930220955810132397809406485504430998883284247476890744759811759301470013143686059878014087921084402703884898661685430889812034497050189574640139435761526983415169973791743915648508955725713703906140316772231235038110678219688469930378177132307304731532134005576976892978381999976676034083329527911241
e=65537
phi=(p-1)*(q-1)
import libnum
d=libnum.invmod(e,phi)
m=pow(c,d,n)
print(libnum.n2s(int(m)))