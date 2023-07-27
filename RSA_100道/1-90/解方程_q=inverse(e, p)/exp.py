
n= 151913753330829779363367789673597253978048533620182497747132604072824540323836504426239804081241567027736270622449855295828160124814438423488754623643933533204599629980943193643551097211543531050709295786991507076525522113596966181359611779370941657496310723772521162794885147507996772774824707716432570452403
c= 81337035006499494768796081417947319039576994033747417935302379695580101083380316241731843797604372408639889020709527188720865744673275465620672796534287478878369491626837235522013863942055110385349674739290041899890532139474221925394370465243005480529009377659505930236007519685951328899152586367092905739547
e=65537
import gmpy2
import libnum
for k in range(e,1,-1):
    tmp=1+4*e*n*k
    r,s=gmpy2.iroot(tmp,2)
    if s:
        p=(r-1)//(2*k)
        break
q=n//p
print(q)
print(gmpy2.is_prime(q))
assert n==p*q
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m=pow(c,d,n)
print(libnum.n2s(int(m)))