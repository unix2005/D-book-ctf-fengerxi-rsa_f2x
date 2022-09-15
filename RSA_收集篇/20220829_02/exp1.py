

p= 11820891196647569262137841192985418014377132106496147254821784946481523526822939129065042819464351666077658751406165276121125571355594004514547517855730743
q= 10450390015864176713581330969519712299844487112687677452105216477861582967322473997670559995588440097951786576039009337782247912476227937589298529580432797
r= 9484954066160968219229920429258150817546418633451929876581842443665029377287119340232501682142185708534413073877473741393278935479791561681402673403009771
c1= 69574855207460025252857869494766338442370688922127811393280455950372371842144946699073877876005649281006116543528211809466226185922844601714337317797534664683681334132261584497953105754257846471069875622054326463757746293958069752489458646460121725019594141157667480846709081917530190233900184428943585065316
c2= 66183492015178047844987766781469734325646160179923242098082430373061510938987908656007752256556018402101435698352339429316390909525615464024332856855411414576031970267795270882896721069952171988506477519737923165566896609181813523905810373359029413963666924039857159685161563252396502381297700252749204993228

n1=p*q
n2=r*q

n =2   # 同余方程个数
a = [c1,c2]  # 余数
m=[n1,n2] # 模数


"""扩展欧几里得"""
def exgcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q


"""扩展中国剩余定理"""
def CRT():
    if n == 1:
        if m[0] > a[0]:
            return a[0];
        else:
            return -1;

    for i in range(n):
        if m[i] <= a[i]:
            return -1;

        x, y, d = exgcd(m[0], m[i])
        if (a[i] - a[0]) % d != 0:
            return -1;

        t = m[i] // d;
        x = (a[i] - a[0]) // d * x % t
        a[0] = x * m[0] + a[0];
        m[0] = m[0] * m[i] // d;
        a[0] = (a[0] % m[0] + m[0]) % m[0]
        # print(a[0])
    return a[0];

ans = CRT()

print(ans)

c=1051311603595400257980451542641726560928968569258042231276292652088507209347204465348483100080899623360705698249443255030368048979130482813052608650445300611553758759647722097778171873596181791974080589234136090632966294575063306439633769753905530026312180583106024810580642209905594594119077985110929675466498207370604560182924468112540068499274911327513697378581931822685826876372554425845071592347470781982215295908151280216722253883169708944885906780090210923