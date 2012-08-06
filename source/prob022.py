
import re

def calc_order_total(word):
    total = 0
    for c in word:
        if str.isupper(c):
            total += ord(c) - ord('A') + 1
        elif str.islower(c):
            total += ord(c) - ord('a') + 1
    return total

f = open('names.txt')
line = f.readline()
f.close()

names = str(line).replace('"','').split(",")
ordered_names = sorted(names)

score = 0
for (idx, n) in enumerate(ordered_names):
    score += (idx+1) * calc_order_total(n)

print score

