
def next_number(num):
    nn = 0
    while num > 0:
        nn += (num % 10)**2
        num /= 10
    return nn

def arrive_number(num, dic):
    key = num
    if num % 10000 == 0:
        print num
    while True:
        num = next_number(num)
        if num in dic:
            dic[key] = dic[num]
            return dic[num]
        if num in (1, 89):
            dic[key] = num
            return num

seq = range(1, 10000000)
dic = {}
print len([n for n in seq if arrive_number(n, dic) == 89])
