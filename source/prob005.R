ret <- 2520
num <- 11:20

euclid <- function(m, n)
{
 limit <- 2^52
 stopifnot(is.numeric(m) && is.numeric(n) && m == floor(m) && n == floor(n) && m < limit && n < limit)
 m0 <- m <- abs(m)
 n0 <- n <- abs(n)
 while ((temp <- n %% m) != 0) {
  n <- m
  m <- temp
 }
 lcm <- (m0/m)*n0
 return(list(GCM=m, quotient=c(m0/m, n0/m), LCM=ifelse(lcm > limit, NA, lcm)))
}

for( n in num ){
 if( ret %% n != 0 ){
  ret <- euclid(ret,n)$LCM
 }
}
print(ret)
