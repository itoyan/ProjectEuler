# -*- encoding: sjis -*-
''' problem 67 also can be solved by this code :-)
    when you use this source code for problem 67,
    please replace "data018.txt" to "triangle.txt"
'''

from copy import deepcopy

f = open('data018.txt', 'r')
pyr = [] # figure is like pyramid
for line in f:
    snum = line.split()
    aLine = []
    for num in snum:
        aLine.append(int(num))
    pyr.append(aLine)

b = deepcopy(pyr) # array for memo
for i in range(1, len(pyr)):
    b[i][0] += b[i-1][0]
    b[i][i] += b[i-1][i-1]

for i in range(2, len(pyr)):
    for j in range(1, len(pyr[i])-1):
        b[i][j] += max(b[i-1][j], b[i-1][j-1])

print max(b[len(b)-1])


