
max_number_of_solutions = -1
max_p = -1
for p in range(3, 1000):
    number_of_solutions = 0
    for a in range(1, p+1):
        for b in range(a, p+1):
            c = p - a - b
            if c < b:
                continue
            if c * c == (a * a + b * b):
                number_of_solutions += 1
    '''
    if p % 10 == 0:
        print "p = %d" %  p
    '''
    if number_of_solutions > max_number_of_solutions:
        max_p = p
        max_number_of_solutions = number_of_solutions

print max_p


