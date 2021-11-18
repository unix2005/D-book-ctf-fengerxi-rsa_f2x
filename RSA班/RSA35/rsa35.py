import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(512)
q = gmpy2.next_prime(p)
n = p * q
e = 65537
c = pow(m, e, n)
c1=c%p
c2=c%q
print("n=", n)
print("e=", e)
print("c1=", c1)
print("c2=", c2)
n= 90394529689913839765205300528110803141279090399860596367870949697496324820998337961985425034620508191655615991982040913558977176983944906780042242192358436166631765017209547263534670341784872178736298551048416053460818373354869470751267394134834866841904586214217784621108471976779832089947742368306315682507
e= 65537
c1= 5447082481186117365672329735877037332776187251773044306359866400835596309056514390380452696154541891064307149942765410614648089004258436764622084019531505
c2= 4535381939284330664634047480806575197107605565999599820054310863529808067307369482944090975014544449155425493695649786450241696037762855154686295855813941


