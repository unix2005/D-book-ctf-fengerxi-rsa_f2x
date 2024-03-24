
import libnum
import gmpy2
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)

k=512
k1=128
k2=256
p = libnum.generate_prime(k)
q = libnum.generate_prime(k)
n = p * q
tmp1 = libnum.generate_prime(k1)
tmp2 = libnum.generate_prime(k1)
tmp3 = libnum.generate_prime(k1)
e1 = libnum.generate_prime(k2) * tmp1 *tmp2
e2 = libnum.generate_prime(k2) * tmp2 *tmp3
e3 = libnum.generate_prime(k2) * tmp3 *tmp1


c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
c3 = pow(m, e3, n)

print("n=", n)
print("e1=",e1)
print("e2=",e2)
print("e3=",e3)
print("c1=", c1)
print("c2=", c2)
print("c3=",c3)
n= 144150438395840412070080025975912184442311562205553839494105094065939813034581018156534210151831377224300558290140339285030269811471122808282496313939540061269277040419891579355656091523687126488873450552563591690162463853314950340028880950648807867051124261250360285274951260465432562484325717611808477356817
e1= 8052763070065096176615795021785259160267119051864331183920581210546011798241397955800289942003058372900984635218492388052497635603044243469458638973853799
e2= 4102755033134319988845858170771061377720353811259609284220553258045989009564186805775444745207566162940194813191426362948068492475527425912743260037396973
e3= 3334300897071053413151065915233161443359776269738768473389284031124267885931531603032132543538283550994020098269611218956599872574459042007359404273338589
c1= 25291586373157432633090967145569097964173309453491833574985434431438903686633568042020815629207650781497285243095024374114105914041841272811404300589787072289986272020930243869166397722437454187919432762646271884317273335369489127485151489618651646786049005769020957827722184238424687463175722480512410930115
c2= 119738246245678286874152137710145157145522088284737430448907384458932876464788433934973971389531607501534838901336954397416648096315096484216277527852019501880686727011578546317988477803433583596177185057574165012829554299444219689797157831231273055412450496466544545112290487386926396144871990937383956128673
c3= 30068142100716345802932147015616964246308623729152951695990606972422641786662645177707915622589772458196811364545578016129948631190061890127222879596306475173628959579289101703806861154033000922998769451564402338733846400847202595130028395188652783932680359763452811804540340425527098753936801524308313075695
