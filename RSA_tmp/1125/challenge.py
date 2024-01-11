from secret import flag
import os
key=[]
for _ in range(len(flag)):
    key.append(ord(os.urandom(1)))

xor=[]
C=[]
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    print()
    xor.append(k)
    C.append(flag[i] ^ v)
with open("mix", "w") as f:
    f.write(f"{xor=}\n")
    f.write(f"{C=}\n")
