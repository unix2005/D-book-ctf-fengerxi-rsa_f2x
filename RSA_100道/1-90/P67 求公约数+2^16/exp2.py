
n1= 83758575069905304067768481601753574998130100929563488113032489538841228437614038849648582947130531285620158614235448872871127520586959431556641650448541549150788998002451811261912231543271446644060890282133258667768706029719891178262570370575285298224152119578339390800107889334951078164762184333747467380888
n2= 9831276541826816789368451633385540087371496489313852209076031193730848235018296111252032115432949863700248359574145846899107616306788202793767305144740541785563939136198331219646159758474239920030391929508514991198073422146216586741498057527918329570942088288077450777684683107307014975767032857456318358064
n= 140856289298906159437739029545347610108994755491239167745641832705764858521348872395929019274279252591208014041777481788324765489375807836151544773947219166392455703715770608717639845195855883468725012423798709748849187737712690267229995903190368828458681379150127037925721096918609588453047678178189307880401
c= 53100585481275556435409181501721693813984862333551455563238323458270043603912938367431862281708352595284147129805506010649262433103290734582315903650224375708892586331205036195752388648357117325957081723405359096400361691896699396085109653734337210068638841322039054338712409255759760189138139488615812969337

import libnum
p=libnum.gcd(n1+n2,n)
q=n//p
print(n==p*q)

inv_p = libnum.invmod(p, q)
inv_q = libnum.invmod(q, p)


c1=[c]
for i in range(16):
    tmp=[]
    for c in c1:
        mp = pow(c, (p + 1) // 4, p)
        mq = pow(c, (q + 1) // 4, q)

        a = (inv_p * p * mq + inv_q * q * mp) % n
        if a not in tmp:
            tmp.append(a)
        b = n - int(a)
        if b not in tmp:
            tmp.append(b)
        c = (inv_p * p * mq - inv_q * q * mp) % n
        if c not in tmp:
            tmp.append(c)
        d = n - int(c)
        if d not in tmp:
            tmp.append(d)
    c1=tmp



for i in c1:
    print(i)
    print(libnum.n2s(int(i)))