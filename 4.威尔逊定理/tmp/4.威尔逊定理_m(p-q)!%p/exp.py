

e=65537
n= 5239578896950249587571476516930072230747171489381019891554658022901447378216174337235234778137680100470506032375981536984218354658712273754146472767889207559660800142235832994281526140023554859177060113288499924899984959122963996947448728424904952225067613573651612073698230312600370437798423114516689551910573311
c= 1992092274194224304191826048708529533082880529666079613526373688358413222163288832361625526134530551203132486864248717420235821860493128739219935367725055598576635217293013370049266870855314196148201054124768947776465796165924241824005892572590232627752888080845913197523641452306017363540471953939886149751861491

#pq经过分解

q = 34649
p = 151218762358228219791955800078792237315569612092153305767977662353933659794400252164138496872570062641649283741983362780577169749739163431964745671387030146891996887131975901015369163324296656734020032707682759239804466481657883256297403342806573125488978428631464459975705801396876401564213198491058603478039


phi=(p-1)*(q-1)
import libnum
d=libnum.invmod(e,phi)
m=pow(c,d,n)


for i in range(p-q,p):
    m=pow(m*i,1,p)
m=m*libnum.invmod(-1,p)%p
print(libnum.n2s(m))
