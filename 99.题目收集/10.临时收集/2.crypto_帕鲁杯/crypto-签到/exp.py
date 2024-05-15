


import libnum

c=55383075134473500553308930745424133667000437939780337988059882643620873296564359798922243970320028523748249850182085152126769674675738969552183526592923530533052864281476942425294435783567823099475819812168007734077764669314454406675324218066424692270907580997478702668419895945205466852642780725082255387731
p=11394071795977146304722408479861290344829267572110699253703185344850398223003218449302187871522873227718468043094549558974536022996082088376885156882522769
e=65537
n=129824872091881872326406954430545365629321274065806402944636887849058938296551776291523344564565786894295335548139064138478970274200569879248864792480990278485554760246559782622671497535186685560196740518108898969633852155786198851709390536824182950802450469452227331308377400913958384487143715080365803427361


print(n==p**2)
phi_n=p*(p-1)
#求逆元
d=libnum.invmod(e,phi_n)
m=pow(c,d,n)
print(m)
#数字转字节，转字符串
print(libnum.n2s(int(m)))
