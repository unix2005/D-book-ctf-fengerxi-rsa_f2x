


n= 107366276602616707754580391591537722557421717489842819364351127019156194234516408108111844324846304641011651177883687858178447229664330716648601261742427270034310789718462990551384358927704870802859039340232173504878713938386394557511167645621954856707686086564909865285525642757208401083478235811276261392217
phi= 107366276602616707754580391591537722557421717489842819364351127019156194234516408108111844324846304641011651177883687858178447229664330716648601261742427249024627824668418652258118002883912611815471866762122714568613387189130415960927159477061138096503546223858648929821797830125483025034816025464143422905600


import sympy
p= sympy.symbols('p')
q= sympy.symbols('q')
f1=p*q-n
f2=(p-1)*(q-1)-phi
s=sympy.solve([f1,f2],[p,q])
print(s)
