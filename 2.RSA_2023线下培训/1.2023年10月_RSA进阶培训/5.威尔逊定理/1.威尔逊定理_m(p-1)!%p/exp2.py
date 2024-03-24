
c= 100880077483974518070020226792238689645677862033522450715261848027546618540644659738527895867527436839886345509134257213671633986662129354067693965909065866173114504374829870400427758436473495433141638760812912607448971535963230009805296251071473946320359274234775126871358339803330015215380471097628227155935
n= 161859084801511574091834914378984703437066356981023167878767033300173756456393696027251640802459178756644519705527642727297076670209865635717366593011702815448639471875476962605041537876758601265624237184358125882580980255766547159262005154294045655748037941867326930070665819600262876696368427460397987212693
e=65537

import libnum
import gmpy2
p1,s=gmpy2.iroot(n,2)
q=gmpy2.next_prime(p1)
p=n//q
print(n==p*q)
phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m1=pow(c,d,n)
print(m1)
#m1=m*(p-1)!%p
#m=m1*inmod(-1,p)%p
m=m1*libnum.invmod(-1,p)%p
print(libnum.n2s(int(m)))