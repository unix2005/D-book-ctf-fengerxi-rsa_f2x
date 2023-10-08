
n= 49134891668897345591333219711303339144007670596441894829337290952093400283298630665826095289165809681961208520996265436195389904640720636719133734406693433810554096598929737422594980883724481297143537076662178576926253446582535294294231165454562659420944920445437433494540727083960515996626310138062984512331
x= 24898114380189083075249478644617176345363769858290571489415603903447660857572376734333314388004344067870622511211551400003900882292855408080408530612898712604821849194436116203045876702326786310101264912258598823736415425063797050123512802647807994402065186878212852202204820369988512984137386942003350601013
y= 16329839654620902472571665649919967371160409036961382290481165859731193710305989211665714814452109039568075053785039634104665516076749524765980529291699849764465433749870986860914147427598112865371747917109336808548762214669827404524571735460653099723747061723390924856171469660835909151652929700638010039801


import libnum
import gmpy2

p=libnum.gcd(pow(x,n,n)-y,n)
p=gmpy2.gcd(pow(x,n,n)-y,n)
print(p)
q=n//p
print(n==p*q)
phi=(p-1)*(q-1)
d=libnum.invmod(p,phi)
d=gmpy2.invert(p,phi)
print(d)
m=pow(x,d,n)
flag=libnum.n2s(int())
print(flag)