
import re

f = open('words42.txt', 'r')
line = f.readline().split(',')
# remove double quotation
words = [re.sub(r'"', r'', elem) for elem in line]
triangle_num = [n*(n+1)/2 for n in range(1, 100)]

triangle_str = []
for word in words:
    if sum(ord(c)-ord('A')+1 for c in word) in triangle_num:
        triangle_str.append(word)
print len(triangle_str)
