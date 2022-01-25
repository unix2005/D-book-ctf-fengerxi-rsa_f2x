import sympy
import gmpy2
import libnum

p1=0x63367a2b947c21d5051144d2d40572e366e19e3539a3074a433a92161465543157854669134c03642a12d304d2d9036e6458fe4c850c772c19c4eb3f567902b3
q1=0x79388eb6c541fffefc9cfb083f3662655651502d81ccc00ecde17a75f316bc97a8d888286f21b1235bde1f35efe13f8b3edb739c8f28e6e6043cb29569aa0e7b
c=0x5a1e001edd22964dd501eac6071091027db7665e5355426e1fa0c6360accbc013c7a36da88797de1960a6e9f1cf9ad9b8fd837b76fea7e11eac30a898c7a8b6d8c8989db07c2d80b14487a167c0064442e1fb9fd657a519cac5651457d64223baa30d8b7689d22f5f3795659ba50fb808b1863b344d8a8753b60bb4188b5e386
e=0x10005
d=0xae285803302de933cfc181bd4b9ab2ae09d1991509cb165aa1650bef78a8b23548bb17175f10cddffcde1a1cf36417cc080a622a1f8c64deb6d16667851942375670c50c5a32796545784f0bbcfdf2c0629a3d4f8e1a8a683f2aa63971f8e126c2ef75e08f56d16e1ec492cf9d26e730eae4d1a3fecbbb5db81e74d5195f49f1

p = sympy.symbols('p')
q = sympy.symbols('q')
for k in range(e,1,-1):
    if (e*d-1)%k==0:
        phi=(e*d-1)//k
        f1 = (p - 1) * (q - 1) - phi
        f2 = q1 * q + p1 * p - p * q - 1
        c1 = sympy.solve([f1, f2], [p, q])
        print(c1)
        p = int(c1[1][0])
        print(p)
        q = int(c1[1][1])
        print(q)
        break

n=p*q
m=pow(c,d,n)
print(libnum.n2s(m))