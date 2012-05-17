num = 1

for i in range(2,101):
    num *= i

sum_digit = 0
for c in str(num):
    sum_digit += int(c)

print sum_digit
