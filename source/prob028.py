# -*- encoding: utf-8 -*-

# 右上が(2n-1)**2の形をしている

total = 1
origin_seq = range(1,1002)
seq = origin_seq[2:1001:2]
for n in seq:
    # val = n**2 + n**2 - (n-1) + n**2 - 2*(n-1) + n**2 - 3*(n-1)
    # total += val
    total += 4 * n**2 - 6*(n-1)

print total
