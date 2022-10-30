import random
a=[]
for i in range(1000):
    e=random.getrandbits(3)
    if e not in a:
        a.append(e)
print(a)