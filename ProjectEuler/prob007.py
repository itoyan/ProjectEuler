import math

prime = [2]
num = 3

while len(prime) <= 10000:
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print num
        prime.append(num)
    num += 2

print "result =", prime[len(prime)-1]
