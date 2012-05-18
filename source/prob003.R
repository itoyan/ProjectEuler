num <- 600851475143
num.sqrt <- 2:sqrt(num)
for( i in num.sqrt ){
	if( num%%i == 0 ){
		ret <- num
		num <- num/i
	}
	if( num == 1 ) break
}
print(ret) # 6857

