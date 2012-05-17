
size = 20
numerator = 1
denominator = 1
for i in range(1, size*2+1):
    numerator *= i

for i in range(1, size+1):
    denominator *= i
print numerator / (denominator*denominator)

