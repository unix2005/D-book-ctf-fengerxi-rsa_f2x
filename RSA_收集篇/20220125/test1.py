import base64

def decode3(ans):
    s = ''
    for i in ans:
        x = ord(i) - 25
        x = x ^ 36
        s += chr(x)

    return s

def decode2(ans):
    s = ''
    for i in ans:
        x = i ^ 36  # 异或36, i为字符串，要ord转换成ASCII码数字
        x = x - 36
        s += chr(x)
    return s

def decode1(ans):
    return base64.b32decode(ans)

final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='

a1=decode1(final)
print(a1)
a2=decode2(a1)
print(a2)
a3=decode3(a2)
print(a3)