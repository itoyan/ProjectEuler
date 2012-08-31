# -*- encoding: utf-8 -*-

f = open('matrix81.txt','r')
matrix = []
for line in f:
    row = map(int, line.split(','))
    matrix.append(row)
f.close()

size = 80

cost_table = [[0 for i in range(size)] for j in range(size)]
cost_table[0][0] = matrix[0][0]
for idx in range(1, size):
    cost_table[0][idx] = cost_table[0][idx-1] + matrix[0][idx]
    cost_table[idx][0] = cost_table[idx-1][0] + matrix[idx][0]

for i in range(1, size):
    for j in range(1, size):
        cost_table[i][j] = min(cost_table[i-1][j], cost_table[i][j-1]) \
                           + matrix[i][j]

print cost_table[size-1][size-1]
