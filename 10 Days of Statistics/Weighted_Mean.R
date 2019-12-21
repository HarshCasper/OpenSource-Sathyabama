# https://www.hackerrank.com/challenges/s10-weighted-mean/copy-from/128916118

# Enter your code here. Read input from STDIN. Print output to STDOUT
data<- scan("/dev/stdin")
number <- data[1]
X <- data[2:(number+1)]
W <- data[(number+2):(number*2+1)]

sum <- 0
for (i in 1:number)
{
  XW <- X[i] * W[i]
  sum <- sum + XW 
}

weight_mean <- (sum/sum(W)) +0.01
cat(round(weight_mean,1))
