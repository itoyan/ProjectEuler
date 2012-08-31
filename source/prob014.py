
''' Maybe this code works more quickly by using hash
    because numbers which has already appeared appear
    many times as this code progress.
'''

def collatz(num):
    nStep = 1
    while num > 1:
        nStep += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
    return nStep

maximum = -1
ans = -1
for i in range(1, 1000001):
    if i % 100 == 0:
        print i
    if collatz(i) > maximum:
        ans = i
        maximum = collatz(i)

print maximum
