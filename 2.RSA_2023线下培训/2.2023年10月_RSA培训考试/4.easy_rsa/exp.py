

h= 16904376071225597675197046556944410427582609796207492373518528626957886374105299061973369114441826844127206588131953364491440310404702816318850400638779060
n= 8928709480734490378901429516141532345710427175648697814723019235038750146335545167143398406879489617199302770305131758872937018859200835014885553932404971
c1= 40111430243445517546476026768678676282033271794242287126004764317624932615254
c2= 68736583928047139307802590417766680081908585504953855176387428170956251384990
x=2293
y=2999

import gmpy2
import libnum

p=libnum.gcd(h,n)
q=n//p

for i in range(p-x+1,p-1):
    c1=(c1*i)%p
for i in range(q-y+1,q-1):
    c2=(c2*i)%q

dp=libnum.invmod(p,q-1)
dq=libnum.invmod(q,p-1)
m1=pow(c1,dp,q)
m2=pow(c2,dq,p)
m=libnum.solve_crt([m1,m2],[q,p])
print(libnum.n2s(int(m)))