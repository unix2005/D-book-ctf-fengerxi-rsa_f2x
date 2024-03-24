import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(len(flag))

print(flag)
m = libnum.s2n(flag)
print(gmpy2.bit_length(m))

p1 = libnum.generate_prime(64)
q1 = libnum.generate_prime(64)
p2 = libnum.generate_prime(64)
q2 = libnum.generate_prime(64)
p3 = libnum.generate_prime(64)
q3 = libnum.generate_prime(64)
e = 1
c1 = pow(m, e, p1 * q1)
c2 = pow(m, e, p2 * q2)
c3 = pow(m, e, p3 * q3)
print("n1=", p1 * q1)
print("c1=", c1)
print("n2=", p2 * q2)
print("c2=", c2)
print("n3=", p3 * q3)
print("c3=", c3)
print("p1=",p1)
print("q1=",q1)
print("p2=",p2)
print("q2=",q2)
print("p3=",p3)
print("q3=",q3)
n1= 197888364518838516447767353718350732583
c1= 29853588342859077144582721942190692324
n2= 230252831175337556924724125988913307893
c2= 30259253695922306448741930029843252969
n3= 189958532304109131985333023289325432483
c3= 107478873379611219579288872161450122760
p1= 11548743063004901539
q1= 17135056467984954797
p2= 14548869050594380339
q2= 15826166994466885687
p3= 15864166519886772767
q3= 11974063186110890749