# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

data<- scan("/dev/stdin")
n <- data[1]
x <- data[c(2:(n+1))]
y <- data[c((n+2):length(data))]

s <- vector(mode="numeric", length=0)
for (j in 1:length(y))
{
  for (i in 1:y[j])
  {
    add <- x[j]
    s <- append(s,add)
  }
}

len <- length (s)
point1 <- floor(len/2)
point2 <- ceiling(len/2)+1
ss <- sort(s, decreasing = FALSE)
LowerHalf <- ss[c(1:point1)]
UpperHalf <- ss[c(point2:len)]

Q1 <- median(LowerHalf)
Q3 <- median(UpperHalf)
out <- Q3-Q1
#cat(round(out,1))
#print(round(out))
cat(format(round(out,1),nsmall=1))
