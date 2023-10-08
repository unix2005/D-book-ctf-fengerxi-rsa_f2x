
n= 911844398111317507568030211586272743559642810803818787914331663929079738528202627822846667662251048042030041470033935664573209369674069523268965737987152526613582183128946606997514072807267986386234735641297355401187247104176554195444054327215371387504430247738514902782779769145341252266429046148517286484851345996337158809383287951151995318833800589048288823347779441389456557817841392926908394599075303380247202305746236213108516365664213381514378206796072503
e= 65537
c= 300080339924368504847999292463017220267952096084441625317459410915167415566239223145483756851374412939603387751934997080135516712082849953085909813367521641463035016978607599067098400749542472669548410227775371907737990831693441893484347549180549797195969845699789670645284724239717707715961085798385861633577513423200868155711392384499868756505186628808335033565935730117671093529418407528298958373955412302769520447097674721470752291661705398421117193503368958
h= 809884123954977744065991060215047261767907810988513481933765255539447865171596804277438503645581843691338334721140948219772473169011209351279569779556323540372837600764584903095004505497930920117960656845231928439961247952623622357635558582989910678652444601766003645438665672155014313626630150843461032702317194331434897461512019950454176827728954669061745699105242051645684116201591222084764721911139049565331397190517268202553536034521089862673238646017020273

import libnum

p=libnum.gcd(e**e*h-1,n)
print(p)
q=n//(p*p)
d=libnum.invmod(e,p*(p-1)*(q-1))
m=pow(c,d,n)
print(libnum.n2s(m))

d=libnum.invmod(e,p-1)
m=pow(c,d,p)
print(libnum.n2s(m))
