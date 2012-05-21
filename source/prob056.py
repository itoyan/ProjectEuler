
def digital_sum(snum):
    ''' input number but its type is string'''
    ret = 0
    for c in snum:
        ret += int(c)
    return ret

max_digit = -1
for a in range(1, 101):
    for b in range(1, 101):
        max_digit = max(max_digit, digital_sum(str(a**b)))

print max_digit
