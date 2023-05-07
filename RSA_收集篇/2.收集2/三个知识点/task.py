from Crypto.Util.number import *
import libnum
from secret import flag

flag = '******' 
flags = [flag[(len(flag) // 4)*i:(len(flag) // 4)*(i+1)] for i in range(4)]
#Is there something wrong with this rsa?
def section1(message):
    m = libnum.s2n(message)
    p = getPrime(512)
    q = getPrime(512)
    n = pow(p,3) * q**2
    e = 65537
    assert m < n
    c = pow(m, e, n)
    hint = pow(d, e, n)
    print(f'c = {c}')
    print(f'hint = {hint}')
    print(f'n = {n}')
def section2(message1,message2):
    m1 = libnum.s2n(message1)
    m2 = libnum.s2n(message2)
    p = getStrongPrime(2048)
    q = getStrongPrime(2048)
    n = p * q
    phi = (p-1)*(q-1)
    e1 = getPrime(16)
    e2 = getPrime(16)
    x  = d2 - d1
    c1 = pow(m1, e1, n)
    c2 = pow(m2, e2, n)
    print(f'n = {n}')
    print(f'e1 = {e1}')
    print(f'e2 = {e2}')
    print(f'c1 = {c1}')
    print(f'c2 = {c2}')
    print(f' x = {x}')
def section3(message):
    m=libnum.s2n(flag)
    p=getPrime(1024)
    q=getPrime(1024)
    e=65537  
    n=p*q
    p1=inverse(p,q)
    q1=inverse(q,p)
    phi=(p-1)*(q-1)
    c=pow(m,e,n)
    print('p1=',p1)
    print('q1=',q1)
    print('d=',d)
    print('c=',c)
    print("e=",e)
print("section1:")
section1(flags[0])
print("section2:")
section2(flags[1],flags[2])
print("section3:")
section3(flag[3])
