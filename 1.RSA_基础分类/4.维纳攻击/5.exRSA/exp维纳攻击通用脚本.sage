

#扩展维纳攻击，给定3组
#直接用xenny的通用脚本

from Crypto.Util.number import *

isdigit = lambda x: ord('0') <= ord(x) <= ord('9')
def my_permutations(g, n):
    sub = []
    res = []
    def dfs(s, prev):
        if len(s) == n:
            res.append(s[::])
        for i in g:
            if i in s or i < prev:
                continue
            s.append(i)
            dfs(s, max(prev, i))
            s.remove(i)
    dfs(sub, 0)
    return res

class X3NNY(object):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def __mul__(self, b):
        return X3NNY(self.exp1 * b.exp1, self.exp2 * b.exp2)

    def __repr__(self):
        return '%s = %s' % (self.exp1.expand().collect_common_factors(), self.exp2)

class X_Complex(object):
    def __init__(self, exp):
        i = 0
        s = '%s' % exp
        while i < len(s):
            if isdigit(s[i]):
                num = 0
                while i < len(s) and isdigit(s[i]):
                    num = num *10 + int(s[i])
                    i += 1
                if i >= len(s):
                    self.b = num
                elif s[i] == '*':
                    self.a = num
                    i += 2
                elif s[i] == '/':
                    i += 1
                    r = 0
                    while i < len(s) and isdigit(s[i]):
                        r = r* 10 + int(s[i])
                        i += 1
                    self.b = num / r
            else:
                i += 1
        if not hasattr(self, 'a'):
            self.a = 1
        if not hasattr(self, 'b'):
            self.b = 0


def WW(e, d, k, g, N, s):
    return X3NNY(e * d * g - k * N, g + k * s)


def GG(e1, e2, d1, d2, k1, k2):
    return X3NNY(e1 * d1 * k2 - e2 * d2 * k1, k2 - k1)


def W(i):
    e = eval("e%d" % i)
    d = eval("d%d" % i)
    k = eval("k%d" % i)
    return WW(e, d, k, g, N, s)


def G(i, j):
    e1 = eval("e%d" % i)
    d1 = eval("d%d" % i)
    k1 = eval("k%d" % i)

    e2 = eval("e%d" % j)
    d2 = eval("d%d" % j)
    k2 = eval("k%d" % j)

    return GG(e1, e2, d1, d2, k1, k2)


def R(e, sn):  # min u max v
    ret = X3NNY(1, 1)
    n = max(e)
    nn = len(e)
    l = set(i for i in range(1, n + 1))
    debug = ''
    u, v = 0, 0
    for i in e:
        if i == 1:
            ret *= W(1)
            debug += 'W(%d)' % i
            nn -= 1
            l.remove(1)
            u += 1
        elif i > min(l) and len(l) >= 2 * nn:
            ret *= G(min(l), i)
            nn -= 1
            debug += 'G(%d, %d)' % (min(l), i)
            l.remove(min(l))
            l.remove(i)
            v += 1
        else:
            ret *= W(i)
            l.remove(i)
            debug += 'W(%d)' % i
            nn -= 1
            u += 1
    # print(debug, end = ' ')
    return ret, u / 2 + (sn - v) * a


def H(n):
    if n == 0:
        return [0]
    if n == 2:
        return [(), (1,), (2,), (1, 2)]
    ret = []
    for i in range(3, n + 1):
        ret.append((i,))
        for j in range(1, i):
            for k in my_permutations(range(1, i), j):
                ret.append(tuple(k + [i]))
    return H(2) + ret


def CC(exp, n):
    cols = [0 for i in range(1 << n)]

    # split exp
    texps = ('%s' % exp.exp1.expand()).strip().split(' - ')
    ops = []
    exps = []
    for i in range(len(texps)):
        if texps[i].find(' + ') != -1:
            tmp = texps[i].split(' + ')
            ops.append(0)
            exps.append(tmp[0])
            for i in range(1, len(tmp)):
                ops.append(1)
                exps.append(tmp[i])
        else:
            ops.append(0)
            exps.append(texps[i])
    if exps[0][0] == '-':
        for i in range(len(exps)):
            ops[i] = 1 - ops[i]
        exps[0] = exps[0][1:]
    else:
        ops[0] = 1
    # find e and N
    l = []
    for i in range(len(exps)):
        tmp = 1 if ops[i] else -1
        en = []
        j = 0
        while j < len(exps[i]):
            if exps[i][j] == 'e':
                num = 0
                j += 1
                while isdigit(exps[i][j]):
                    num = num * 10 + int(exps[i][j])
                    j += 1
                tmp *= eval('e%d' % num)
                en.append(num)
            elif exps[i][j] == 'N':
                j += 1
                num = 0
                if exps[i][j] == '^':
                    j += 1
                    while isdigit(exps[i][j]):
                        num = num * 10 + int(exps[i][j])
                        j += 1
                if num == 0:
                    num = 1
                tmp *= eval('N**%d' % num)
            else:
                j += 1
        if tmp == 1 or tmp == -1:
            l.append((0, ()))
        else:
            l.append((tmp, tuple(sorted(en))))

    # construct h
    mp = H(n)
    for val, en in l:
        cols[mp.index(en)] = val
    # print(cols)
    return cols


def EWA(n, elist, NN, alpha):
    mp = H(n)
    var('a')
    S = [X_Complex(n * a)]
    cols = [[1 if i == 0 else 0 for i in range(2 ^ n)]]
    for i in mp[1:]:
        eL, s = R(i, n)
        cols.append(CC(eL, n))
        S.append(X_Complex(s))

    alphaA, alphaB = 0, 0
    for i in S:
        alphaA = max(i.a, alphaA)
        alphaB = max(i.b, alphaB)
    # print(alphaA, alphaB)
    D = [int(NN ^ ((alphaA - S[i].a) * alpha + (alphaB - S[i].b))) for i in range(len(S))]
    # print(D)
    kw = {'N': NN}
    for i in range(len(elist)):
        kw['e%d' % (i + 1)] = elist[i]
    print(cols)
    B = Matrix(ZZ, Matrix(cols).T(**kw)) * diagonal_matrix(ZZ, D)
    L = B.LLL(0.5)
    v = Matrix(ZZ, L[0])
    x = v * B ** (-1)
    phi = int(x[0, 1] / x[0, 0] * elist[0])
    return phi


def attack(NN, elist, alpha):
    phi = EWA(len(elist), elist, NN, alpha)
    return phi


elist = [
    5077048237811969427473111225370876122528967447056551899123613461792688002896788394304192917610564149766252232281576990293485239684145310876930997918960070816968829150376875953405420809586267153171717496198336861089523701832098322284501931142889817575816761705044951705530849327928849848158643030693363143757063220584714925893965587967042137557807261154117916358519477964645293471975063362050690306353627492980861008439765365837622657977958069853288056307253167509883258122949882277021665317807253308906355670472172346171177267688064959397186926103987259551586627965406979118193485527520976748490728460167949055289539,
    12526848298349005390520276923929132463459152574998625757208259297891115133654117648215782945332529081365273860316201130793306570777735076534772168999705895641207535303839455074003057687810381110978320988976011326106919940799160974228311824760046370273505511065619268557697182586259234379239410482784449815732335294395676302226416863709340032987612715151916084291821095462625821023133560415325824885347221391496937213246361736361270846741128557595603052713612528453709948403100711277679641218520429878897565655482086410576379971404789212297697553748292438183065500993375040031733825496692797699362421010271599510269401,
    12985940757578530810519370332063658344046688856605967474941014436872720360444040464644790980976991393970947023398357422203873284294843401144065013911463670501559888601145108651961098348250824166697665528417668374408814572959722789020110396245076275553505878565603509466220710219260037783849276475397283421068716088638186994778153542817681963059581651103563578804145156157584336712678882995685632615686853980176047683326974283896343322981521150211317597571554542488921290158122634140571148036732893808064119048328855134054709120877895941670166421664806186710346824494054783025733475898081247824887967550418509038276279]
NN = 17853303733838066173110417890593704464146824886316456780873352559969742615755294466664439529352718434399552818635352768033531948009737170697566286848710832800426311328560924133698481653594007727877031506265706341560810588064209681809146597572126173303463125668183837840427667101827234752823747483792944536893070188010357644478512143332014786539698535220139784440314481371464053954769822738407808161946943216714729685820896972467020893493349051243983390018762076812868678098172416465691550285372846402991995794349015838868221686216396597327273110165922789814315858462049706255254066724012925815100434953821856854529753
c = 1414176060152301842110497098024597189246259172019335414900127452098233943041825926028517437075316294943355323947458928010556912909139739282924255506647305696872907898950473108556417350199783145349691087255926287363286922011841143339530863300198239231490707393383076174791818994158815857391930802936280447588808440607415377391336604533440099793849237857247557582307391329320515996021820000355560514217505643587026994918588311127143566858036653315985177551963836429728515745646807123637193259859856630452155138986610272067480257330592146135108190083578873094133114440050860844192259441093236787002715737932342847147399
alpha = 768. / 2048
for i in range(1, len(elist) + 1):
    var("e%d" % i)
    var("d%d" % i)
    var("k%d" % i)
g, N, s = var('g'), var('N'), var('s')

for i in range(len(elist)):
    elist[i] = Integer(elist[i])
phi = attack(NN, elist, alpha)
d = inverse(65537, int(phi))
m = pow(c, d, NN)
print(long_to_bytes(int(m)))
# hgame{Ext3ndin9_W1en3r's_att@ck_1s_so0o0o_ea3y}
