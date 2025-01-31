#sage
a=1
b=23
e=3
n= 9707282140608521534597213563664893782715260149781186731553485375967064221954996829298350139968314798018284178381942220275007118714479405726997513958731781270336969570682984804304509289064604490389662873420811943298401346416863405802733285090007438244315477659519649397202552302359138760555930108515441728335367340137429696475675969560470475825268961509793587655446220632264103246117705882070495699964049531607741206990087970869961102891452578255653506178059604251931305312230652370649515170079034023689675250251084053161308943618517038440570295690711731360323639242469371943498556697872269814453467858940956177847263
c1= 175676150266641711916444091445781139277779003156556056759990312014697871894446590460729449316298376008489849677065205914793458959388232066629206406667357155787745931037869574771399224859869367943670440218253278560317330520488399820186869405944311596980008194439252102301970756589691462498043634547537253
c2= 175676150266641711916444091445781139277779003156556056759990312014697871894446590460729449316298376224923256004570408208514033791620884417984796834735275720367596862370848324295530654005254716452155315511101075351067155901490533428950707819290823018393253109305648196157485509642713358863483579848456000

import libnum
def franklinReiter(n,e,c1,c2,a,b):
    R.<X> = Zmod(n)[]
    f1 = X^e - c1
    f2 = (X*a+ b)^e - c2
    # coefficient 0 = -m, which is what we wanted!
    return Integer(n-(compositeModulusGCD(f1,f2)).coefficients()[0])

  # GCD is not implemented for rings over composite modulus in Sage
  # so we do our own implementation. Its the exact same as standard GCD, but with
  # the polynomials monic representation
def compositeModulusGCD(a, b):
    if(b == 0):
        return a.monic()
    else:
        return compositeModulusGCD(b, a % b)

m=franklinReiter(n,e,c1,c2,a,b)
print(m)
print(type(m))
print(libnum.n2s(int(m)))