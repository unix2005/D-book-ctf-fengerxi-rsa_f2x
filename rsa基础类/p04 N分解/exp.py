import libnum
import gmpy2
#11

n = 12627644643778588563638920097915399454513514338804142285365906525498881036764131263143503359846189659273574532609463345820199502529021505655249992763681092637840409087205147095497477412031460598408163901210084467516709264700724398765301043908384308244747517893224665577128486689416162459250095126318456522046726204794830519283112518017007468770465828497144764208737754275011224549145753948172880930824906241704072415618131966725150546352452195727712056875106693907690990407658130836472884891082069644890044024145259903993177177196801509187283280149791400422260709944706691099262186583269852628892867781015062638406807
e = 65537
c = 3591154430994525075059034292233285219547469362782194889629270181283842636528606554393490851841066761509914849524082427752928544931823147005056532710833510595339404286404496491815089547021604266428940702481584786412593056050015881926826382036205406303525545716475450640777471292475111436226636460600345957363695624982558394414290121846251722500596533341384706714159205414604934501768918663557451374023537565102442827170460775303421150229829840660742855663501969208548706192593969737261023358057081741247088819534013372830024084918363322257487890942468889177188305118367719047889896681307253995123323963920988776643105

q = 112372793165332455233644051831703093065233917285171435667727396467617869514267375433546885241603527682450490525106056020927668059639131922631965832681267028908272712604839741417231722918220018271377173404939261706593582911881852334650278053606220270970895872789340580971511712537114765669110273199402053063417
p = 112372793165332455233644051831703093065233917285171435667727396467617869514267375433546885241603527682450490525106056020927668059639131922631965832681267028908272712604839741417231722918220018271377173404939261706593582911881852334650278053606220270970895872789340580971511712537114765669110273199402053062671
assert n == p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(libnum.n2s(int(m)))
