# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
data<- scan("/dev/stdin")

Length <- data[1]
Y <- Length +1
X <- data[c(2:Y)]

Q1 <- mean(X)
Q2 <- median(X)

getmode <- function(x)
  
{
  library('plyr')
  count<- count(x)
  max_freq <- max(count[,2])
  position <- which(count[,2]== max_freq)
  list_mode <- count[position[1]:position[length(position)],1]
  min(list_mode)
}


Q3 <- getmode(X)

cat(Q1,Q2,Q3,sep = "\n")
