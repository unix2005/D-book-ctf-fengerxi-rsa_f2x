
from pwn import *
from hashlib import sha256
import random
import sympy

sh = remote("hnctf.imxbt.cn",20432)
context.log_level ='debug'

def p_js(n,phi):
    n=int(n)
    phi=int(phi)
    p = sympy.symbols('p')
    q = sympy.symbols('q')
    f1 = p * q - n
    f2 = (p - 1) * (q - 1) - phi
    s = sympy.solve([f1, f2], [p, q])
    return s[0][0]


s=sh.recvuntil(b"n= ")
n1=sh.recvuntil(b"\n")
print(n1)
s=sh.recvuntil(b"phin= ")
phi1=sh.recvuntil(b"\n")
print(phi1)
p=p_js(n1, phi1)
p=str(p).encode()
print(p)
sh.sendline(p)
sh.interactive()