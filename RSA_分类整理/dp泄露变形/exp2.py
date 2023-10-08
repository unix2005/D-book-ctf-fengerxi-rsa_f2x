import gmpy2
import libnum

e = 65537
c= 32461937291123838150015437738232132778136420835501172981733602990740273486953741568090810560778161966164945158511260774070358644248232323420087723385263256644196533073406984717180336745536558689984942092573081904079903490501386556080018394074410235002595317034773282955985118051270196236522237314803148550104312339887381647416993827777740145028707473690705297024951376596720342536992121548930518678367840538408090222135227089379157055839665026501357827048478457911999587594147965082828271987647298414995124826623670109344083974284447663062399760045862177923687178825610208304215451278227328518587611057109711358853294506221375136820608279989589848521299683305678250602533798187554673551619882364862267158445783085217884637473353723296775978631814700691324134568859907895
h1= 6468066142812037811245811431029822620718431256172659827318030980766740646875043754362691871361354796260760544851348386608059020178469741472552508428173289



for k in range(65537,1,-1):
    aa=e*h1-1
    if aa%k==0:
        p=aa//k+1
        if gmpy2.is_prime(p) and gmpy2.bit_length(p)==512:
            print(p)
            break
m=pow(c,h1,p)
print(libnum.n2s(int(m)))

