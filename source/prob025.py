
fib = [1, 1]

while True:
    var = fib[len(fib)-2] + fib[len(fib)-1]
    fib.append(var)
    if len(str(var)) >= 1000:
        break

print len(fib)



