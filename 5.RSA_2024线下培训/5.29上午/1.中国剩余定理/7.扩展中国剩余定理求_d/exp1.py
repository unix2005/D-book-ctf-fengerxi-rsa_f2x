

p= 9358552784366265801179621198769977438088825686405824106679491286961358676156355523648254343850726381579355456536508040331535453079221369805588099767437047
q= 11125532612834741593025119653320189302840134890958215188404898060348683748015315027755917438834208563942076814120076597682040760723591458327217300634372233
r= 10117098640720072821086133424035495034867887407951798854216097301183457170091107182890030142770998556462838323214043952066607285463452487518562252711419057
dp= 3603587559113379745087726376361774146986877153228255527834238410473004757236910031557614454414742039038664854232988302847191881149652496214208215773950668186794892721522634946315572298999116121283265669494970880173423893797513355151254194552399321572658931444325713992781299498978984998523246384567896769191
dq= 51891186386434023095317551955709328782509821154452797482898119271178636977834234296505539212968051385478377746818706031021847768855456826898833792938380014721465934733764227811791849763891486035894218997854875568421430506648406506511271640718239357684330899901970896372716173323547592000305529835081810016391
dr= 89424216203530555822375060818538345648610654734944882421805016324902080824568090828552095321330666879157854247613433008580207470632702290599060986278779830042297015976413235252940840914651884804627980344374298325791647330484595397567842777444233210231966476555423164864806038911035146362630196483093710746007
c= 503531286877523709156249669210398056523200188321072294543849896899711010117561239887693799560912703733652706641241763238313022024976749194394073956944785985695729614919957546552045117399908276014984316157920427758746963829586271665433573236413833404474860648256920282323143053976868314274191839878624578287753232623608121961997284847074429778593314787196730662929693789275502670569503384319299362748083634080827252879056964647628833731563459719408741917611291137

"""扩展欧几里得"""
def exgcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q
"""扩展中国剩余定理"""
def CRT(n,a,m):
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

n2 = 3  # 同余方程个数
d1 = [dp,dq,dr]  # 余数
n1=[(q-1)*(r-1),(p-1)*(r-1),(p-1)*(q-1)] # 模数
d = CRT(n2,d1,n1)
print(d)
import libnum
m=pow(c,d,p*q*r)
print(m)
print(libnum.n2s(m))