

n=1267823002000585646737981661823859226160068900652848264635181451467294490786177399240549134608524578470887543099089140600253518611230598280984929384757696040751410260509514630315190290618001880728253102064138202156272913558138987149446166573976023039063044035395043628257895187491104330908110843461311073733410681059016587581692213161475169348177052366664391317968573726592543717093048411293655337527351034238909747907301078831661353839587601664097368775097636934653532723015852158597471422697486486994071127859836606327205816654077053380411327469802885120376134352296189263517893135077063574563594581966548102863798253349344241268902326620790716252569946681818651557553248666003185840310275559289019428281269551043211607422640338615186576292996206918917335530961611462606986696961850590544431321622036395455871956754358220543508387404777340631810333926350401743640218233823026286454172212703691673161160655281805190925513121
d1=25511043178972272159459437353075843629368164814205947530889485463490216791891936262759336345474030234494609360936202441389686499931089246781148403452520441956352524827505025914356365261358669478189724001700518717195034868842271795888594558363919997145881569720636806636766859204500173744814042474091702844884
c=1108061892992430713591489101001357192065563625171488288086422334674337970248825349283038492696747091218163747860459525109075062531114691113320249569777175696367067582388295826711404004907105227629011626015599275868367597393667494389065246366991804962268440545998025691192050236927064090929960781145906697980617928731277860451646310662710154922071128172076224749255786194071824090005026963470579867325093389272908669835426167871127191481041504813062490959134429616654895148675915973319892446065420277625829398005921931935264469255341572444096828515761587323299151814714374339190693257136557656500267254620453148588595575785852010396446344872320102873013835292779066309205694393666160959989662133516885850706018248372212155273609938741545767642157268272234936107581122577602108022936029404554543799315587445431671988481357187456002896625905946695947734528662750263874456038864977752726542588760236063935384689308499073161274744

import libnum

p=libnum.gcd(pow(d1,4)-1,n)
print(p)
q=n//(p*p)
n1=p*q
d=libnum.invmod(n,(p-1)*(q-1))
m=pow(c,d,n1)
print(libnum.n2s(m))