# -*- encoding: sjis -*-

def findMax(matrix, size):
    ''' matrix の縦横斜めの方向で連続するsize個の積の
        最大値を求める'''
    maxNum = 1
    nRow = len(matrix)
    nCol = len(matrix[0])
    # 横方向
    for i in range(nRow):
        for j in range(nCol-size):
            num = 1
            for n in range(size):
                num *= matrix[i][j+n]
            if num > maxNum:
                maxNum = num
    # 縦方向
    for j in range(nCol):
        for i in range(nRow-size):
            num = 1
            for n in range(size):
                num *= matrix[i+n][j]
            if num > maxNum:
                maxNum = num
    # 斜め方向(左下から右上へ)
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

    # 斜め方向(左上から右下へ)
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
