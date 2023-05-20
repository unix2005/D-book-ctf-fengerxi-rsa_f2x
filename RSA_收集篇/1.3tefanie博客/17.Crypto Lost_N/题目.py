import gmpy2
from Crypto.Util.number import *
# part1
flag = b'SangFor{}'
d = getPrime(435)
count = 5
while count > 0:
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi = (p-1) * (q-1)
    e = gmpy2.invert(d, phi)
    print('c =', pow(bytes_to_long(flag), e, n))
    print('n =', n)
    print('e =', e)
    count -= 1

# part2
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 0x10001
s = pow(900*p - 218*q, n-p-q, n)

c = pow(last_n, e, n)
print('n =', n)
print('c =', c)
print('s =', s)


c = 13007070082982086015048648249698272815655157209727275797297990841215796701955079738986996208838342773211678208282162295881823413924960399315068498509939876883297864092435101096694113071462267388158595518905101264654742860199638059278239359756219217345342001728599121265614144789005805619626458575126846199823
n = 145575036089862184772968012014750816659166028840828357885024516131565102712346345625910708214596157522939248398359985832422106056149116726640753670919394145037581595172384392223713667048639158944450925280598688178812170253438103664700756173806183649477673497327790421063029596049211220930285435947389700047717
e = 6104905725583061487097813130111812725712623687061285535333592835899028572315489283518324105546236465450024687400996793197533588656449965379858202658832799573292015786259804984314040621630959455897094519928941186899832366216111359619637121411868069759469878142871432060850651758192209783752650530390826992241
c = 59089700172263364510471541430195724136973801897202789650586019199451669728729101831161257990233999290546484165767660146638244043033774379664984894178111808280076960669616271416462197675878517863817855762681885790347812435849975072020273928469523961698304409181769820692602979823921421820511589311465948726144
n = 171055961405321566289532118753767563629109197214150143506779656820887080836894368955104877312070939117885512468517951216152955714212079279910802095156350517032659766690101321767892798466184405283403136505441356956934759143173462058806620784497304916652269667097971495139608875846338091109621496242787157524093
e = 30639328953696065722075015079387560065304228779854040351182305267894609577068955234152835797506237100956072519388029280776532681675227753068574540049244778077615881093270476533536257809592871380358708151151683035275615961208943826349952952069226829397420921321531951316523368786223865432179572145636266109841
c = 24257648301491609274972482189063774024772127961295257418254600487615473027418329077996964279110710299066082437371516700591657843057597234861450272363240630164504734590903528165056021531272324846249133757036680429476939369309982196345252669711604534774523215422683385359295249160897422071732828044179085194829
n = 99735998821682404719682435155046621256882035421263371444758755082217342389922499214602126376005623406797486880520535486455942687180959663032781490782870080236095770591995437146834606144553095293546973559144743704707021952152013362323293717685161426469215016058837362232410103330238322051089471439573994907641
e = 81580834845272005549352820344384188734735397414102222005750919291263464191246301214086773744759605577533897859454210564034313392997143493147211816886655474145064723790935089304983994174659126346174766206623180477360887938029897557683160392738708450965784921553806400996559956745732829531154835363767773681061
c = 105310270039347542993580213074911114373638987155564864341577443142664062749969114572669295115218200093381519732560445712425129105002834596010587656544575627162469582470245756143405705971157024449801127133755773536097173259762599166367688198314997549663330392481942723997656023552049910279885657664434799986156
n = 118810172988175650374012494943583618875926370822995080847518376655089884052560062524542984436965153851285471302754389325839857100631601002627184437173686224779115595776898914116490948408328080895524604124937295381872443370706017215743101755848741173976351916104362193751372512936063892260855907424754174906407
e = 57970672598245590037421993575987847127437841761387257183798066822318596392918179916711068560675528926294272336883938499809087281773070750919594701600347605662910664129043903749270935721912605279738208730075557097647316659218872977257614306133047318781156168440924237849014715453590776000659069078250493480521
c = 50430341205487530895874157969557709374947862873979946417751686643857339147558892228311050765271667685452170747716439387141655285820549605442067496018168606163031122498272292974227360674531814593351170403519198099247839499352696883293133549658442172721339510734646474794377043195182186423251146266787514560008
n = 80837118813383038376595037732171926303253457956240963765871280771175535050976501573174357090322706934194338649978803681581485022992041019276854467388155755920855237665754031077890133388056350355753218650482718197635332681450734918373003830855184694566883308495322647552169761087814135330222306083205629967447
e = 51172856769626923894369204019063376718507295306271724506808987836327051371415876890252665691760404489737902233106400428873399230724307065583727090788789453353097657968301923726049631007431604461521879288667433292135840271678776989737261214286587609316530839676362375173635542358540766454865624476392874630929
c = 24533435736573623334539431528997922833496063510219641412038735658846891237553927656156039267456590702682308774830590768888594750053426705504840854071081487058180327084899496154314864910274839867793265086899109787190447838634454294468362549369144295591261617705578124672391399319219038350878856530074063011081

?
?
?
?
?

e = 71905546659735491498365580186225996341462093571074706903142472266442052559638067842283521897292088493599089076218507596455101425837547743511983105386966540811629138324774640350969049873787070380161376295760563611617178869788237730560614549740931199083194226891873779907795120035746039593933256380499568775673







n = 20955464633057600258987829727550073699845816289000240676927869818926752810905511184835302717855745473943671910742784074561535017974853574714483642916831791020944940633062963043482236587316552330558006573820423830770910893877191630012247591380869307656539553888318621170921800017818132160253923739647771452839191101104391894609403591447166963426444018303147924843072923713248135717578047687411974516038299879758561542241544862102935741869647633013298181782208467117482306148238724598730801037692668154263059348953587766571379262442743822007387408949824805991797355089583176028081305319076896384126383926193964322235633
c = 14815997295683082265558346455845370590765145583224067337292601455640475216349267044144296003388877395546880235511728120803143112914764263292087421926972160283428440959367872665892349776616002018624301524264223581314248857537034849571849747613963209414193510408342387107662655487869098045345428379025731617851483935711671021438908270746316921057871871545763798735895118697635903815383424855759281301248295597297869474539060531099443223045844791615425429748703429968627505406271675074549912664863784774239200764403372298995457799473112713379340870305136776932539188516395526955161359417473843082895317392495109895085666
s = 14728527428626630951705148488338433865446345521255631461200851513782412494843597938863837697938230856843797646287742397249258609197032095158567448934855031190354034543862057663422053672290704598313096289223478302733688501373756860855445632789922930577582465209872782549135254792729915747104521949095814028476908208917363509089190935273004331739978623136706041729628143765893264698948654175039064609891374587695812144855411176143224066975193255513405865992328257766815240718115442741846443490733767716842367336385132648983241895710001620533668392060358573295789752856876282590472528110546264872047138094995909454134250



