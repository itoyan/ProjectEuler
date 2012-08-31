
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...

def Tn(n):
    return n*(n+1)/2

def Pn(n):
    return n*(3*n-1)/2

def Hn(n):
    return n*(2*n-1)

def next_triangle_number(from_num):
    rng = 1000
    while True:
        t = set(map(Tn, range(1, rng)))
        p = set(map(Pn, range(1, rng)))
        h = set(map(Hn, range(1, rng)))
        triangle_num = list(t.intersection(p).intersection(h))
        find_min = filter(lambda x: x > from_num, triangle_num)
        if find_min:
            return find_min[0]
        rng *= 2

print next_triangle_number(40755)
