
from Crypto.Util.number import *
import gmpy2

num1= 83413293264298100290007834084433692854270412681202773024273842573136997582589263543893853366720551623188777071724079912751679832973122236526911613882334924195879779962851135970422720680221537506695901383761090577177644454813087561487015428557312866315722344225684336110171051601689068295048655026623613551112
num2= 68121484580290588837600302713628097373076989525156902378532939378721674752494884361402195720530549863792884724656657371344013924998683787257843755183199255473710469545685960064805882904496027636030511656594413107139898832891344111507565738699829707090333696608499697657498320409797448809736070418609961691119
n= 100989645852086142818281049692718690161357415303787625696968064918686669384942606305289515100850442865554199328082549677962178096174143082148689820899890773783455576524226104264177831856105373348877967808526686661863305191302760728055881133116690039529116215874211616245058967397264700384645835467665386887357
c= 89290723349280998320244014872072233529247821682314660471097184761940168879573971872442268621393725731711839930377215085435680151795101104480340779678137649274814543331376440268466746093499651453578303880006032018608700327010817712613195148869384412497811263021834730492989325593155128355041396670059585579605

p = gmpy2.gcd(num1+num2,n)
q = n//p
print(n==p*q)
x0=gmpy2.invert(p,q)
x1=gmpy2.invert(q,p)


cs = [c]
for i in range(16):
    ps = []
    for c2 in cs:
        r = pow(c2, (p + 1) // 4, p)
        s = pow(c2, (q + 1) // 4, q)

        x = (r * x1 * q + s * x0 * p) % n
        y = (r * x1 * q - s * x0 * p) % n
        if x not in ps:
            ps.append(x)
        if n - x not in ps:
            ps.append(n - x)
        if y not in ps:
            ps.append(y)
        if n - y not in ps:
            ps.append(n - y)
    cs = ps

for m in ps:
    print(m)
    flag = long_to_bytes(m)
    if b"flag" in flag:
        print(flag)
        break

