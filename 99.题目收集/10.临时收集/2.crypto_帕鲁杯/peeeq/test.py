import libnum

p = libnum.generate_prime(128)
q = libnum.generate_prime(128)


def check(m, p, q):
    if m == 0: return True
    if m >= p and check(m - p, p, q): return True
    if m >= q and check(m - q, p, q): return True
    return False


l = libnum.lcm(p, q) - max(p, q) - 1

while True:
    assert m <= l or check(m, p, q)
    m += 1
