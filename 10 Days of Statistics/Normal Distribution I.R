# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem


out1 <- pnorm(19.5,mean = 20,sd = 2, lower.tail = TRUE)
out2 <- 1- pnorm(20,mean = 20,sd = 2, lower.tail = TRUE) - pnorm(22,mean = 20,sd = 2, lower.tail = FALSE)

cat(round(out1,3),'\n')
cat(round(out2,3))

