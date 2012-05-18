# Project Euler Problem 2

a <- integer(1000) # ˆê‰ž“K“–‚É‘å‚«‚ß‚Ì”z—ñ‚ð¶¬‚µ‚Ä‚¨‚­
a[1] <- 1
a[2] <- 1
idx <- 3

repeat{
	nextNum <- a[idx-1] + a[idx-2]
	if( nextNum >= 4000000 ) break
	a[idx] <- nextNum
	idx <- idx+1
}

a.even <- a[a%%2==0] # 0‚àŽc‚é‚ª˜a‚ÌŒvŽZ‚É‚ÍŠÖŒW‚È‚µ
print(sum(a.even))

