









c = 69544098122008365404362084363106703100129828060729951875286300108187409752434091431958070449710849545293894427509731332109603391232669996343824626329922214945852346904863792615793077092573477272770896080330100575733798947163067912513775789041009052964547466568583353539184274864951400026558080635235037201971
p=9163780868330371783046823560204742650207381649001998649144074078237594022997541853040616995577439077419293518952061614558930717648995958968548958385492411
q=8370013716894660543940240406654509658721347047444446140469279948687027451068359349254746794140352451890594825470508554608349473296351748298082449565302119
n=p*q
e=65537
phi=(p-1)*(q-1)
import libnum
d=libnum.invmod(e,phi)
print(d)
m=pow(c,d,n)
print(m)
print(libnum.n2s(m))

