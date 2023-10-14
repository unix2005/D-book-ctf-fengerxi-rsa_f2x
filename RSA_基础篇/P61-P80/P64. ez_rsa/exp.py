
n=18336742329884102840711317056035829900181031899189965750167873247413394641421884268181180691799041109583073943734087501015287414276920859165536905614439348503104274176568855477810531928653188875313730773137188091767852363627844294299040337825572541798873059356845108200822470510731037280638271124446065184354506970256843543850443109120027067527858587486057498852574725176229877820581759854939710243108203113794979358592406727121602933570979025567077283555797084943162877639538993194638753216782472761922799597735864155048439702411288616956442552133534875725842240671105704465899591323469357171905274867363751281123247
h1=1252844288468503695550243404563586462617011659388394200051720305685224941345382700983943620422884153199816724972430258300696585493752549767621920218013177579388545270274165271651476390315113548267328442422574474106977637932563997285964407338258031456094851349019368799898332224311311188244366361497766384463046587873293222867629858009633119430473237720433940187260340236617618032769955951340051941330184522021650899057422413083524886548436561935912965902864883553129567889140877640756235730236555781451777917327564097797822166501516917699128045913203596851378025423122968843582012019500459385654636751599894851458351
h2=9372658757528018075585873938689688667595611219809604193505327461157355035998280991915810280916265405771187574214240041631054692961669102928657994522444766345091108534967234939998426664677001285401663303336483357351570879442640356832134635009138579833296258528994217323017074320514096232648660837631600068406083966184065417110577998050940915029262671705045930779224144859045296198979642263749762965524230417688633923218341644161771682446178771418361480575099582796449004687140222773542485353293259336292554167715336570527592523057152139234351378592121576659687826162305089129951661033393719069922214845616397228054002
s1=17818777320099743574792192230925418970926671482754544828312744472202727257835448645018760334767202416889077303681209695695290682035587819091283788021132063936245016041130858087330406977762314607779532927594642136661884057020662014838166908136272955801758615395853373735209801179864593133086396870342139104377196439253270769560518591784939535311238417144833260105578439217808679097351572822160120723200514939970978291158775940616189903650702017285483129529224465094029601386558853762398002072461400399773086518641312329962732943625997986732849428860185614698341141082088117103859616210529089454307509864015402680450752
s2=17745205434302289172261061726582183100050240183141897044263848096855882167630308048515532877655997481323723761245288228014045887243992108877003391450810596750475185980002701216964626908989995892780321114731680548218866704745495262402375566994875987528431185467498207053681256800613915643619684124264080876391321293509246814097958563460227848361224705286894656757539256222181174208198295195922613627791121199508440947265204075399845298456571326440566973078761495459203859587941942747505548405554575259340462242619380902373391926282828117922572150597961444218810254473436716053851621800718860960168746743829568608998298
y=14676659934675433661603955751496740382990867202669064009122690155916769134139120151950339948794357904401904881851648110053115995128085990258060718671821977626425000065983105892022851422498918760828228289005503521404883741095179075953432753039576791540996520575946958864925249516614587126488379696255113653340749207697415460635326152351014340634025933707226458530317971925987908263595932384913518391393147030756839110735711185994163928004373968329366175837332685509255433237813116649958641669516489845488761218066209152207152670606957483004689634829608960121659775456303608066578081850540853164967673426424626973755368
z=13885128582896542072794363253508191879378367292431924029600398585235384425347216327237889338131010415844013552482363174841951912846623522342820094091183292191001739756035479294022623368763969812749815837159138527753167744897931960376209366577118783625974089777381848422080513485849197153995253148285172127628344923042269329949437896432223854629087413499091116534404920689597857498276872587612692524326856220734655005545788687304945187863655516729659835103761614017456691957934966880321897509514662055227090804286841623317992094651126856221197518354572555663380242180525457119596217491091960723601691291778638327587479

# h1=pow((p+q),e1,n)=(p^e1+q^e1)%n
# h2=pow((p-q),e1,n)=(p^e1=q^e1)%n
# #h1+h2
# h1+h2=2.下一个素数*p^e1%n
import libnum
e=65537
p=libnum.gcd(h1+h2,n)
q=n//p

# s1=(y*c+2024*x)%n
# s2=(z*c+x*2022)%n
#
# 2022*s1=(2022y*c+2024*x*2022)%n
# 2024*s2=(2024z*c+2024*x*2022)%n
# #1-2
# 2024s1-2022s1=2024zc-2022yc+kn

a1=2024*z-2022*y
a2=2024*s2-2022*s1
# a2=a1*c+kn
# a2%n=(a1*c)%n
# a2%n*inmod(a1,n)%n=c
# c=a2%n*inmod(a1,n)%n

a1=2024*z-2022*y
a2=2024*s2-2022*s1

c=(libnum.invmod(a1,n)*a2)%n
print(c)

phi=(p-1)*(q-1)
d=libnum.invmod(e,phi)
m=pow(c,d,n)
print(libnum.n2s(m))

#b'DASCTF{fa28fe96957c7470bad4e711fbb87d0a}'

