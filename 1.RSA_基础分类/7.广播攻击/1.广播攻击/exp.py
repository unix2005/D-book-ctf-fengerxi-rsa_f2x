

e= 17
n1= 17294107561450562952118322318188886057575513788504228361699019150925706489696163398865109975719315771865151699562080266068453559337226612911338075856636432161817265106739182332780870450414482518978501777644385117076581821904480707614821188851268008255091167425236312347681361185157924855474539824448947926014582880079510022774004891317104570541712113117347190513277469610321686016309768126530484050834305635567392935411367459669034695793329810901125805298626882846077007989116229446939110028186298285060038789229509046433953889018181211890484618381745492241389305102205024716723511913534901735738596207016940855307297
n2= 18940573476366191710822431665943331498207954050693782350180852738623237907370891669576751404695463772432598078582401167014587944427896956052024359645185057634727956429210764644304684811251340261452477241224717436151499944413902787011429996547754623732254265838673132257520363113349880681186557671819464464688539524827416562898360619155847970737567441171736502951632994400784006379776040671936142463922273139184975369929024136962458215893137820481531415046456132555836878853422538221444900766937534525749506607124115108623965525352152357060497310482449381809159552997378397938809582534656578066870810455058063748890683
n3= 21504785563143656844589867167556265861896063211850207067245554262062235858804608781117935284755347129170284626391421311569277453793440024923441127655544646688684635998848857327980727988781555029024180091175878310703835838909550754771198296629408838414601468220227649194962606946494897268411954883414507186933270311915996457492796862746543647738424128670488425733443514296529830181424630626840776908242572815256445556362713590199930576056573040377645046407377676695083279059475166512610757083914727461945391994922103530035028767924806639783562966440943362555246064462553054428779653288615879430751290119322918406180357
c1= 6480345303333451701785708195602027555404231728462939598339106126659399832216610732292182799883854946163942565738518548825775441813726668236432369474440012638791998621818067534574169013744563136561831457612634007825911783904613706600921911245208808440819864228225433394637769003564515551538729729410349447204579614267112629926421373581891946810085942326738151345618741190212648386694873868638992775587223324952542652061745575197166710939296447822303212400113460147989032648318095225819928863253970559849673977744738954073714490078174503852911370976236648570469633841936849141523504475567309248364547392656358123673761
c2= 5810262801978161880854743046488517727063034034923929107185649193530648677195366737395396051455815747431933894237040441081749157471524826739764958712838464847301378185887881671739654375002079470790951137987540768594210275997245634881467264410999680352359624718534073050318664154364825246444711358833284745853165859740722708533002527088550968352559046628140808683679568907590806646724206933271010112901283277824646194358746476986303904998755535090343654656346112624166782001890273554648177251221442001610593117504743387546342034816005552988830884204312353833500821620115604072002433849181487017183599669570247133047918
c3= 8872999883957897966095133318454460029221689708629417284231851758781216773547904898172432339448433741143946433885195288782699419510266150090000427337408984196082298158271675594553702781503122912859733270293725473797300199862576010585093581520164685519857950368426395189387703428320368886835830079454803159549159107320183938950353044115877646572710114808700799239023491551000129862713517572788007030769611878386966748251980082287257693052906578199379443645884106915009680495718545649085922025210180015871566449260555610125383486648600450803972246992042358328512693368273905269174211407729998393765876776634183425910623

import libnum

m1=libnum.solve_crt([c1,c2,c3],[n1,n2,n3])
m=libnum.nroot(m1,e)
flag=libnum.n2s(m)
print(flag)