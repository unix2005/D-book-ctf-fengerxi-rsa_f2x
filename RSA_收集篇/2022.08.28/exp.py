

c=695811613220508521533410410135903763704380792345313822348335925535019364085287973391006658091756337941388790850576390425798691514904654108730064898721482454942897809486946732327567166790987988769649339266791907850313832700513155194190805272799105846921535231183458026312210254181900390502309417588847104213793231394168583827484833346266655392107254900891316034825295594615584454126662183967495486871019315836843964142146438253642093949267821928660254775556448682535996878217802620757735862588509198138308229216540912203307177130148261480033848867147610177292359480179993393430101548639801133574244188591918478576785400355882470444135385837723688465703459098247158590332167802098779963168624783522306380012451430590453130321881597629274617390265737278952430391455292129197120724233266227673065462001473529262207830010588159156853973215615518415224386700532070174251781750417203041543631328597659473610199473825400069638203715
n=1103142672269025650462929198164640404493425942265040323371207998377200145961695641048087337404972402560194267711668479433180851107371884950953570911657090487495216386781924343363213345312692741516666557796484628501590914827387171553761258413087800091632213720047678961681727564158606220008125433169164157150198004730103285226539823741065685538894369776994256049396334124080247371292445543852118777801692107831636409684364527162627188519199064013189168290873007156380530155343171815296016451575866508168728518236121071519646489851701773457562537221387306293985011019040423572239157745630631563892081210964602524396761067561161422635793249097955070576281428534742447903449072401000345617064665752070967341863838984791405144869303448662169933201623421080650216122814985967041163663854812030159367202820911939914186148267664571396203542821594364250609009816872825447917845472311564561269905225280796615586133341770795940714518373
t=1352157133681616199949626085859887520183044653936717410198546937928330648087119395184417755928058157424764679366526294873446661771336360719004981235527982326342186212780230888122434477779310176780131887691097470115061291877918798366484343129280364265571974776435297187299058517674913907506344826320352532394679559865918025267583173757096064690288877037701829014463065076789753953054738098985305066307636180043889030783678919407771611169741555877144593927382649961986384716532446388338376466150688150609936293316903617335385558920141250240529204636396228961938978325120385146208552506658553610353813640686759609897131817533377973931149277140553678119548578402674858651748611808600372129132750796909828079961432457264127651812438564831345298563698676305419952826466259729378236885089128224289161328570151277873778313473830713469181909893871432564345696475759124658962121070495959528237764331872929513704863754771030741820729657
e=65537
import libnum

p2=libnum.gcd(n,t)
print(p2)
q=n//p2
print(q)
p=t//p2
print(p)

phi_n=p*(p-1)*(q-1)
d=libnum.invmod(e,phi_n)
m=pow(c,d,n)
print(libnum.n2s(m))

