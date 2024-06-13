import libnum
import gmpy2


n= 1101676297168703265566511587913652821222614528632844563918598090813090976948138058144049294690727841463413972173051671908835164088465174349647584948964206244648736138253802417241570633968307801570794459668533128958442296813160786428069813867034205462528763830205245218089660432399549540588101288362866463
e= 3
c= 175676150266622974236396526711286850987631123485212632328509227849029911058091086706143340012942548868507757097027596460222082381606490997654543157611859508598203272345044220266344322516323997126214392011463091635444512796333373451321795475333496092463760390199602320265733668648810943598505902205569125


def exp(n, e, c):
    k = 0
    while 1:
        m1 = k * n + c
        m, t = gmpy2.iroot(m1, e)
        if t:
            print(m)
            print(k)
            print(libnum.n2s(int(m)))
            break
        k += 1
exp(n, e, c)

