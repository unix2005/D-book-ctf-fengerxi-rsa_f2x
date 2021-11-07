import libnum
import gmpy2

n = 17329555687339057933030881774167606066714011664369940819755094697939414110116183129515036417930928381309923593306884879686961969722610261114896200690291299753284120079351636102685226435454462581742248968732979816910255384339882675593423385529925794918175056364069416358095759362865710837992174966213332948216626442765218056059227797575954980861175262821459941222980957749720949816909119263643425681517545937122980872133309062049836920463547302193585676588711888598357927574729648088370609421283416559346827315399049239357814820660913395553316721927867556418628117971385375472454118148999848258824753064992040468588511
c = 2834445728359401954509180010018035151637121735110411504246937217024301211768483790406570069340718976013805438660602396212488675995602673107853878297024467687865600759709655334014269938893756460638324659859693599161639448736859952750381592192404889795107146077421499823006298655812398359841137631684363428490100792619658995661630533920917942659455792050032138051272224911869438429703875012535681896010735974555495618216882831524578648074539796556404193333636537331833807459066576022732553707927018332334884641370339471969967359580724737784159811992637384360752274204462169330081579501038904830207691558009918736480389
h = 2528640120640884291705022551567142949735065756834488816429783990402901687493207894594113717734719036126087363828359113769238235697788243950392064194097056579105620723640796253143555383311882778423540515270957452851097267592400001145658904042191937942341842865936546187498072576943297002184798413336701918670376291021190387536660070933700475110660304652647893127663882847145502396993549034428649569475467365756381857116208029508389607872560487325166953770793357700419069480517845456083758105937644350450559733949764193599564499133714282286339445501435278957250603141596679797055178139335763901195697988437542180256184

e = 65537
p = gmpy2.gcd(pow(1011, n, n) - h, n)
q = n // p
print(n == p * q)
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(libnum.n2s(int(m)))
