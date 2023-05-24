import libnum
from Crypto.Util.number import getPrime
from flag import flag, e

p = getPrime(1024)
q = getPrime(1024)
n = p * q
assert e <= 500000
c = pow(libnum.s2n(flag), e, n)
leak1 = c % q
leak2 = c % p
leak3 = p + q
print("n =", n)
print("leak1 =", leak1)
print("leak2 =", leak2)
print("leak3 =", leak3)
n = 21256406304024147327122699985764737895162788854942201173538004689536569610046157311527715126074775927977409773971656249943602454790380966869525211733301201659688694473703188427037879868522859419364680904585572399937639393418586498509580133474303442722716959873727260844993296681950092753897902540593927952622713860163782763263944291810729056735965535138964485886748344167499818148134252327820007439830749462775149754781930983094046362696040641091039506998835624218220892441813224657845627120344960554424765109502415773475619490661527184126374299883610442465428985757004551740482644952396990065188807827114495184096249
leak1 = 8842431959638543756327530752221031675897458993985909403335303147413741167900365489182674478419510549838159493192002672500346433589707076289344572454304647803237654059883974235710442126617587691632375039292283285577033977676131772115877520248352227419433136507412485140428972344000541898060766721412300525883
leak2 = 127414092867622693231378230621806169422569654246682818498761930473755998913688181327473434110121174292309611256339271412324673262030535400937563769685033472683498585742711576446343086462569783541192470920638935990937187809422965809986860709074542257475025562691683977493260026623616012846939417988284096473040
leak3 = 293130152177150437492580785085598394773458388719469800871702200331766258900690595210759869625006484354799804558552583572062231998451041105464048317708732987121458633718573774164071597186461239762511364549980544029915308083867329707804739776241438307060614946195675715671343671137725809499387682363101164970886
