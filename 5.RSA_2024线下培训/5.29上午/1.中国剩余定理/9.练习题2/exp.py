

import uuid
import libnum
import gmpy2
import os
flag = "flag{" + str(uuid.uuid4()) + "}"
flag = flag.encode()+os.urandom(35)
m = libnum.s2n(flag)
print(gmpy2.bit_length(m))
print(flag)
e = 65537

p1 = libnum.generate_prime(128)
q1 = libnum.generate_prime(128)
p2 = libnum.generate_prime(128)
q2 = libnum.generate_prime(128)
p3 = libnum.generate_prime(128)
q3 = libnum.generate_prime(128)
p4 = libnum.generate_prime(128)
q4 = libnum.generate_prime(128)
print("p1=", p1)
print("q1=", q1)
print("p2=", p2)
print("q2=", q2)
print("p3=", p4)
print("q3=", q4)
print("p4=", p4)
print("q4=", q4)
n1 = p1 * q1
n2 = p2 * q2
n3 = p3 * q3
n4 = p4 * q4

c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)
c4 = pow(m, e, n4)
print("c1=", c1)
print("c2=", c2)
print("c3=", c3)
print("c4=", c4)

p1= 267068906346996635058112308004303365143
q1= 312892712931394823523111853201838090243
p2= 243645301525076764506499470648939441839
q2= 234375057481137694798316001722036308591
p3= 320361581120248621370146815107344973461
q3= 180548856642891546868372944568819426831
p4= 171625301263879308394472554887818026187
q4= 175947975522911573908623351162001500521
c1= 17861451761590047573537194694446804283340702050324362419594175861606626616785
c2= 11731606250453067037475524032445755604965876532867027754259173673200987267573
c3= 8317396164831283086205464759567945075179692608404698509073605293594364020168
c4= 6035065716903970657341663928071849957866823578477405959462019393386497201443
e=65537

import libnum

n1=p1*q1
n2=p2*q2
n3=p3*q3
n4=p4*q4
phi1=(p1-1)*(q1-1)
phi2=(p2-1)*(q2-1)
phi3=(p3-1)*(q3-1)
phi4=(p4-1)*(q4-1)
d1=libnum.invmod(e,phi1)
d2=libnum.invmod(e,phi2)
d3=libnum.invmod(e,phi3)
d4=libnum.invmod(e,phi4)
m1=pow(c1,d1,n1)
m2=pow(c2,d2,n2)
m3=pow(c3,d3,n3)
m4=pow(c4,d4,n4)

mm=[m1,m2,m3,m4]
nn=[n1,n2,n3,n4]

m=libnum.solve_crt(mm,nn)
print(libnum.n2s(m))

