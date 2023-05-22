import gmpy2
import libnum
import sympy


e= 65537
phi= 153526208973286457920479376447622546334064100044507994947932972947056601063592943200823498761273906685365632931851181655405163001559274037884326450823919640514634182433839200397012200852498394907718538509040702321554785017853186412670980153149366201235845635320919980848682144430326738538775142630420821822960
c= 45404866893480020010799585996788902747901025575540655893265307771493992595444010006643443639614244962689890716458286889196613281948316354607540970243071548624687668875908716690311985915197944902857988253464493234021796216923039652003206533181461815990153623141243415592031190212825941414063970906141991979873
p1= -11065332660497699825690181811194036599102527446002445107664152730915570503984416572510322521934240155183790860963748546243230674204488210677533190963726687
q1= -1516147835082043403956384639695921948575165356837676821387726774997348251688472575043896909177257102383857065378906848506987546488480618072779943395893217

p = sympy.symbols('p')
q = sympy.symbols('q')
f1 = p1 * p + q1 * q - 1 +p * q
f2 = (p - 1) * (q - 1) - phi
pq = sympy.solve([f1, f2], [p, q])
p = (pq[1][0])
q = (pq[1][1])
n = p * q
d = gmpy2.invert(e, phi)
m = pow(c, int(d), int(n))
print(libnum.n2s(int(m)))
