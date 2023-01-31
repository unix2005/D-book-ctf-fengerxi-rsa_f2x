from Crypto.Util.number import *
import gmpy2

p = getPrime(1024)
q = getPrime(1024)
n = p * q
print('n =',n)
e = 0x10001
M = m * e * 1 * 2022 * p
c = pow(M,e,n)
print('c =',c)

# n = 16266043783454053154037197753138388613864200794483663334493856481522764684650995230938142916968470804276539967429581472897698022852787399956166067156691430593337430691851251036378709799238876668312530223697905925939542713491015517460139150765778057817475571231361809654951289718071760502692960235551663466242938669673675870151921605230499603814070711617511206013584605131901906195136038060653121164252894949526861390984185085201067988694831398388037080993820517447099157891181179389949333832439004857436617834100885739716577641892686620423154860716308518151628754780994043553863224363539879909831811888663875989774849
# c = 12716190507848578560760116589677996073721225715245215495257947887969923319693501568134141757778665747980229898129090929698368855086594836111461700857934476682700625486249555753323344759513528101651108919161794915999809784961533946922607642974500946026677116418317599095703217004064379100607278317877894742815660315660254853364776654303066021672567442581774299847661025422994141801987588151758971034155714424052693627277202951522779716696303237915400201362585413354036973117149974017434406560929491956957193491445847385625481870256240443170803497196783872213746269940877814806857222191433079944785910813364137603874411
