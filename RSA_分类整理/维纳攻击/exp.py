
import gmpy2
import libnum


def continuedFra(x, y):
    """计算连分数
    :param x: 分子
    :param y: 分母
    :return: 连分数列表
    """
    cf = []
    while y:
        cf.append(x // y)
        x, y = y, x % y
    return cf


def gradualFra(cf):
    """计算传入列表最后的渐进分数
    :param cf: 连分数列表
    :return: 该列表最后的渐近分数
    """
    numerator = 0
    denominator = 1
    for x in cf[::-1]:
        # 这里的渐进分数分子分母要分开
        numerator, denominator = denominator, x * denominator + numerator
    return numerator, denominator


def solve_pq(a, b, c):
    """使用韦达定理解出pq，x^2.下一个素数−(p+q)∗x+pq=0
    :param a:x^2的系数
    :param b:x的系数
    :param c:pq
    :return:p，q
    """
    par = gmpy2.isqrt(b * b - 4 * a * c)
    return (-b + par) // (2 * a), (-b - par) // (2 * a)


def getGradualFra(cf):
    """计算列表所有的渐近分数
    :param cf: 连分数列表
    :return: 该列表所有的渐近分数
    """
    gf = []
    for i in range(1, len(cf) + 1):
        gf.append(gradualFra(cf[:i]))
    return gf


def wienerAttack(e, n):
    """
    :param e:
    :param n:
    :return: 私钥d
    """
    cf = continuedFra(e, n)
    gf = getGradualFra(cf)
    for d, k in gf:
        if k == 0: continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return d


n= 111749447895139230839559322489891344231100409579634157414462477755412375609827399472018112260324339290341823044943955176508350678014062725785913194741174512284287660355439786638026768307433208205692831534843081553639308631917818827370503712317601370805988083920092556408906177082007091662779066400976078908703
e= 4824404713353982239347483470705373140087707706686656857541884256398698831685559474171266996247533820761516873532575695632452091674897804740253757226807444666425113208739256903249342294306803684078518028723783094611419967545606759331743886443757873971368284087817112095513335582516786937242736354746287900437
c= 94596647150882401757338260921292127273369802529249057666820406423331274054309633624633515606870749126059424410586817777066639112973108706954882835882375431890860342058767504558643859117867766223734473523293930285496997197053436498595192744642935492100335444862331498717392767466750085202282045483139413182858

d = wienerAttack(e, n)
print(d)
m = pow(c, d, n)
print(libnum.n2s(m).decode())
