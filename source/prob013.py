f = open('data013.txt', 'r')
total = 0
for line in f:
    total += int(line)

sTotal = str(total)
print sTotal[:10]
