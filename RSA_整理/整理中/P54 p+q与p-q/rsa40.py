import gmpy2
import libnum
import uuid


flag = "flag{" + str(uuid.uuid4()) + "}"
print(flag)
m = libnum.s2n(flag)
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 65537
while 1:
    if p > q:
        a = p + q
        b = p - q
        break
n=p*q
c=pow(m,e,n)
print("a=",a)
print("b=",b)
print("c=",c)
a= 287545392132610911896032301251492356608434869325178383079452776672304825621024356929204908229777063772812677052770521870142986331205612566509656360799795299160512935307982752776256741158204379729521311070578351291236115651942393357036037779538454749993862014627012421787422257644519119355494004580692964370616
b= 9800757947868665387927705308310135911210323857869445860428869945362460155083166164016916655867108626617763579665005881815004597815234238370308616712812035919814088879935564327814824084885577417245295642656610293081865206195247187247343566255846165207319739422930196791107362128531965375617861513278641827442
c= 15839173264849808198739152568223724742273019986823742354823095371882306430323084067153292787790089295341617296970607091953451733721012305407762682470727208666727864664720743712412760845080324417410047852951324609092375710400535672002097799988493248356090335327600622180221525559366045379438966174713173925329443702721341478918976401800574930032980037034935480395666859952625575408326830502879455697099798385060536431378515908973467201078984785919883717575355829153460516665818805117275521445062292119110114251112960077421417851281194366453517173539331287730012775440117855282547884453581641781483672203505172252674082
