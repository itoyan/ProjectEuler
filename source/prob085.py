# -*- encoding: utf-8 -*-

def find_rectangles_in_gird(row, col):
    num_grid = 0
    return sum([(row-r+1)*(col-c+1)
               for c in range(1, col+1)
               for r in range(1, row+1)])
    '''
    for r in range(1, row+1):
        for c in range(1, col+1):
            num_grid += (row-r+1)*(col-c+1)
    return num_grid
    '''

max_value = 100000000
area = -1
for r in range(1, 400):
    print r
    for c in range(r, 400):
        value = abs(2000000 - find_rectangles_in_gird(r, c))
        if value < max_value:
            max_value = value
            print value, r, c
            area = r * c

print area
