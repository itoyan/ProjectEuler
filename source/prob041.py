
import itertools, math

def is_prime(num, dic={1:False, 2:True}):
    if num in dic:
        return dic[num]
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            dic[num] = False
            return False
    dic[num] = True
    return True

digit = 1
dic={1:False, 2:True}
max_number = -1
while digit < 10:
    x = itertools.permutations(range(1, digit+1), digit)
    for elem in x:
        num = elem[0]
        for integer in elem[1:]:
            num = 10 * num + integer
        if is_prime(num, dic) and (num > max_number):
            max_number = num
    digit += 1

print max_number



