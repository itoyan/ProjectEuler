# -*- encoding: sjis -*-

def findMax(matrix, size):
    ''' matrix �̏c���΂߂̕����ŘA������size�̐ς�
        �ő�l�����߂�'''
    maxNum = 1
    nRow = len(matrix)
    nCol = len(matrix[0])
    # ������
    for i in range(nRow):
        for j in range(nCol-size):
            num = 1
            for n in range(size):
                num *= matrix[i][j+n]
            if num > maxNum:
                maxNum = num
    # �c����
    for j in range(nCol):
        for i in range(nRow-size):
            num = 1
            for n in range(size):
                num *= matrix[i+n][j]
            if num > maxNum:
                maxNum = num
    # �΂ߕ���(��������E���)
    for i in range(nRow):
        for j in range(nCol):
            if i + 1 < size or j + 1 > nCol - size:
                continue
            '''
            if (i + 1 < size) or (j + 1 < size):
                continue
            if (i + 1 > nRow - size) or (j + 1 > nCol - size):
                continue
            '''
            num = 1
            for n in range(size):
                num *= matrix[i-n][j+n]
            if num > maxNum:
                print i, j
                maxNum = num

    # �΂ߕ���(���ォ��E����)
    for i in range(nRow):
        for j in range(nCol):
            if i + 1 > nRow - size or j + 1 > nCol - size:
                continue
            num = 1
            for n in range(size):
                num *= matrix[i+n][j-n]
            if num > maxNum:
                maxNum = num

    return maxNum

f = open('data11.txt', 'r')
grid = []
for line in f:
    tmp = line.split()
    toInt = [int(d) for d in tmp]
    grid.append(toInt)

print grid
print findMax(grid, 4)

f.close()
