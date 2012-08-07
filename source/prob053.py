# -*- encoding: utf-8 -*-

import math

def ncr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

num = range(1, 101)

total = 0
for n in num:
    for r in range(n): # n+1は考慮の必要なし
        if ncr(n, r) >= 1000000:
            total += 1

print total
