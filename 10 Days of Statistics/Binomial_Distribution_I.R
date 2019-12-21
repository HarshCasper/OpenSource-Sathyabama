# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

data <- readLines(con <- file("stdin"), warn = FALSE)
close(con)

#ratio <- as.numeric(data[[1]])
ratio <- 1.09
child_per_birth <- data[2]

p <- ratio/(ratio+1)

out1 <- sum(dbinom(3:6,size =6, prob =p))

cat(round(out1,3))
