# -*- encoding: utf-8 -*-

num = range(1000000)

snum = ''
for n in num:
    snum += str(n)

pos = [10**n for n in range(7)]
result = 1
for p in pos:
    result *= int(snum[p])

print result

