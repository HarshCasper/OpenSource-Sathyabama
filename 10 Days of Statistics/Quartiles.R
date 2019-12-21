# https://www.hackerrank.com/challenges/s10-quartiles/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

data<- scan("/dev/stdin")
Length <- data[1]
Y <- Length +1
X <- data[c(2:Y)]

X_length <- length(X)

X <- sort(X, decreasing = FALSE)
Point1<- floor(Length/2)
Point2<- ceiling(Length/2)+1
LowerHalf<- X[c(1:Point1)]
UpperHalf<- X[c(Point2:Length)]

Q1 <- median(LowerHalf)
Q2 <- median(X)
Q3 <- median(UpperHalf)
cat(Q1,Q2,Q3,sep = "\n")
