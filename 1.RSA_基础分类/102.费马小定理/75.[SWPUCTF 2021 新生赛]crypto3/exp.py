
flag1= 17893542812755845772427795161304049467610774531005620109503081344099161906017295486868699578946474114607624347167976713200068059018517606363517478396368430072890681401898145302336139240273132723451063402106360810413024642916851746118524166947301681245568333254648265529408446609050354235727237078987509705857
flag2= 95580409405085606847879727622943874726633827220524165744517624606566789614499137069562997931972825651309707390763700301965277040876322904891716953565845966918293178547100704981251056401939781365264616997055296773593435626490578886752446381493929807909671245959154990639046333135728431707979143972145708806954
n= 140457323583824160338989317689698102738341061967768153879646505422358544720607476140977064053629005764551339082120337223672330979298373653766782620973454095507484118565884885623328751648660379894592063436924903894986994746394508539721459355200184089470977772075720319482839923856979166319700474349042326898971

import libnum

p=libnum.gcd(pow(flag1,n,n)-flag2,n)
q=n//p
print(n==p*q)
phi=(p-1)*(q-1)
d=libnum.invmod(p,phi)
m=pow(flag1,d,n)
print(libnum.n2s(m))

m=libnum.solve_crt([flag1%p,flag2%q],[p,q])
print(libnum.n2s(m))