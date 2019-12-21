# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

p <- 12/100
N <- 10
at_most <- sum(dbinom(0:2, size = 10, prob = p))
at_least <- sum (dbinom(2:10,size=10, prob = p))
cat (round(at_most,3), '\n')
cat (round(at_least,3))
