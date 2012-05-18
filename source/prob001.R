array <- 1:999
three <- array[array%%3==0]
five <- array[array%%5==0]
fifteen <- array[array%%3==0 & array%%5==0]
print(sum(three)+sum(five)-sum(fifteen))
