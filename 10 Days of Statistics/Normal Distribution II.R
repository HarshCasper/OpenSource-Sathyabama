# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

out1 <- 100*pnorm(80, mean = 70, sd = 10, lower.tail = FALSE)
out2 <- 100*pnorm(60, mean = 70, sd = 10, lower.tail = FALSE)
out3 <- 100*pnorm(60, mean = 70, sd = 10, lower.tail = TRUE)
cat(round(out1,2),sep='\n')
cat(round(out2,2),sep='\n')
cat(round(out3,2))
