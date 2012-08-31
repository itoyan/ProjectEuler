
def contain_same_digits_first():
    num = 1
    while True:
        seq = [num * n for n in range(1, 7)]
        count = map(count_digits_num, seq)
        s = set()
        for elem in count:
            s.add(frozenset(elem))
        if len(s) == 1:
            return num
        num += 1

def count_digits_num(num):
    snum = str(num)
    dic = {}
    for c in snum:
        dic[c] = dic.get(c, 0) + 1
    return dic

print contain_same_digits_first()
