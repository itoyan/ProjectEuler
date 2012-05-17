
import math

res = 0
for i in range(10, 500000):
    snum = str(i)
    total = 0
    for j in snum:
        total += int(math.pow(int(j), 5))
    if i == total:
        print i
        res += i

print res

