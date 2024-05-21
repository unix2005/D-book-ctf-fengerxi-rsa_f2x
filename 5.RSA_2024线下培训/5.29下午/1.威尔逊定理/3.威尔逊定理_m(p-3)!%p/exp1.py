
c= 22219928299372260303655946559885951550620479014115912692545351849498149094354399406766412146571432195725125119882812530194135514779495666898422127298168690508294852801961904907007748812604428424233234863981121121489200394503743257554092555588372782706740735142827826707907712656940402348625207073061579543002
n= 90558277155533977169882209234227094428247558122982187839122901919219671061329135567913069238047661927241286071604141240008120303039031815327301321660159681010922313055273646323615753870659114536126702399667940852570492550972098755078424535896306404968698258361484621611114494790056011128479559627454277222011


import gmpy2
import libnum
e=65537
p1=gmpy2.iroot(n,2)[0]
q=gmpy2.next_prime(p1)
p=n//q
print(n==p*q)
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m1=pow(c,d,n)
#m=m1(p-2)%p
m=(m1*(p-2))%p
print(libnum.n2s(int(m)))


