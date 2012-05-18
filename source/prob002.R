a <- integer(1000) # array size is decided by estimation
a[1] <- 1
a[2] <- 1
idx <- 3

repeat{
	nextNum <- a[idx-1] + a[idx-2]
	if( nextNum >= 4000000 ) break
	a[idx] <- nextNum
	idx <- idx+1
}

a.even <- a[a%%2==0] # 0 is no relationship for result
print(sum(a.even))

