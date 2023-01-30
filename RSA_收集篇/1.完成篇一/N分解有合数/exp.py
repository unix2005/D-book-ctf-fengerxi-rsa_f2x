

#利用在线网站分解N，把分解结果中的非素数去掉。
#重新计算N,计算私钥,求出明文

e=65537
c=76196483810925191371357319946893762223027002702624516192769497540954799651198719100683206759706879828894501526423422596543748404479640715319801018211652987852179907519286760601944889601355220646374788026632971331786307898234821477134265724962397355614076896148563340833323366935479885600112872998594315513803419069126624158092821269145991266528158747750965226483644012365861166608598063649804899693010576080857540523307078138634628539419178875838147396170651777949577793359622498517581948006585916952705460782942977789615065947303447566918741750017127110484065354974088489869377128636357092420660532261674969708694


p=5
q=29
r3=31
r4=197
r5=12541
r6=4811988280952344246576937
r7=304081130082418831034791698146581643331044047712028910273173568327362370621651464924047927850720915897334538205155796477275515888954493777509372421863858817079340724222044305450451984754173948523380921443850440010226012354226083642718433164324022575599948330147718863789069
r8=16249579302136675275737472669394168521026727339712083110552530420348131906271518040549529167354613121510156841352658645018277766962773342379074137176993546193979134201416444089373463960664685121485689105129185197998903479181913613273443541075619342246119648308939006396145123630152777688592984718084919469059

phi=(r8-1)
n=r8
import libnum
d=libnum.invmod(e,phi)
c=pow(c,d,n)
print(libnum.n2s(c))