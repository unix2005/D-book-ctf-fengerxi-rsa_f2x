
import libnum
import gmpy2


c= 110529037403457010976226680228015853681747082298049971277864723725003290263121993249901746108064910538219056566054434964752554464076788576969420195833066780032521421693370829430794829520809208371861674386624296250550029664837604012247019944404589941948639334516981017574704294281416080581914051559281376725552
n= 118816369182219711551736875622148948376274930097622029542291351942110204065005093752267272235864774888160522170555189015695148555668006209122716634896476014952586332120668094812890443697140874554631953248467119041951362983074748376348829077644413780641030688747863975973112631445365138922148115802917498155841
e=65537
p1=gmpy2.iroot(n,2)[0]
q=gmpy2.next_prime(p1)
p=n//q
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m=pow(c,d,n)
#根据威尔逊定理  （p-1)！%p=-1  （p-2)！%p=1
# m=m1*（p-1)！%p
# m=m1*(-1)%p
m=m*libnum.invmod(-1,p)%p
print(m)
print(libnum.n2s(int(m)))






