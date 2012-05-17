import math

num = 0

for i in range(1,1001):
    num += (i ** i)


print num % (10**10)
snum = str(num)
print snum[len(snum)-10:]

