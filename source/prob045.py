
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n1)	 	1, 6, 15, 28, 45, ...

def findSmallest(T, P, H):
    if T <= P and T <= H:
        return 'T'
    elif P <= T and P <= H:
        return 'P'
    else:
        return 'H'

T = 1
Tval = 1
P = 1
Pval = 1
H = 1
Hval = 1
# nTry = 1
# maxTry = 5000

while True:
    #if nTry >= maxTry:
    #    break
    if Tval == Pval and Pval == Hval and Tval > 40755:
        break
    c = findSmallest(Tval, Pval, Hval)
    if c == 'T':
        T += 1
        Tval = T * (T+1) / 2
    elif c == 'P':
        P += 1
        Pval = P * (3 * P - 1) / 2
    else:
        H += 1
        Hval = H * (2 * H) / 2
    # print Tval, Pval, Hval
    # nTry += 1

print T, Tval, P, Pval, H, Hval


