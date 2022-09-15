from Crypto.Util.number import *
import random
from secret import flag
table='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
pad=100-len(flag)
for i in range(pad):
    flag+=random.choice(table).encode()
e=343284449
m=bytes_to_long(flag)
assert m>(1<<512)
assert m<(1<<1024)
p=getPrime(512)
q=getPrime(512)
r=getPrime(512)
print('p=',p)
print('q=',q)
print('r=',r)
n1=p*q
n2=q*r
c1=pow(m,e,n1)
c2=pow(m,e,n2)
print('c1=',c1)
print('c2=',c2)


p= 11820891196647569262137841192985418014377132106496147254821784946481523526822939129065042819464351666077658751406165276121125571355594004514547517855730743
q= 10450390015864176713581330969519712299844487112687677452105216477861582967322473997670559995588440097951786576039009337782247912476227937589298529580432797
r= 9484954066160968219229920429258150817546418633451929876581842443665029377287119340232501682142185708534413073877473741393278935479791561681402673403009771

c1= 69574855207460025252857869494766338442370688922127811393280455950372371842144946699073877876005649281006116543528211809466226185922844601714337317797534664683681334132261584497953105754257846471069875622054326463757746293958069752489458646460121725019594141157667480846709081917530190233900184428943585065316
c2= 66183492015178047844987766781469734325646160179923242098082430373061510938987908656007752256556018402101435698352339429316390909525615464024332856855411414576031970267795270882896721069952171988506477519737923165566896609181813523905810373359029413963666924039857159685161563252396502381297700252749204993228

e是q-1的因子
