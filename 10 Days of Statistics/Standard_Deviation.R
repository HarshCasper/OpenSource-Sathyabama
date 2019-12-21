# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

data<- scan("/dev/stdin")
number <- data[1]
X <- data[2:(number+1)]

u <- mean(X)
sum <- 0
for (i in 1:number)
{
  w <- (X[i] - u)^2
  sum <- sum + w
}

std <- sqrt(sum/number)
cat(round(std, digits = 1))
