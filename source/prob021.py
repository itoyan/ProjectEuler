
def d(num):
    return sum(n for n in range(1,num/2+1) if num%n == 0)

target = range(2,10000)
dnum = [d(n) for n in target]
dic = {}
for (key, value) in zip(target, dnum):
    dic[key] = value

total = 0
for (key, value) in dic.iteritems():
    if value in dic:
        if dic[key] == value and dic[value] == key and key < value:
            total += (key + value)

print total
