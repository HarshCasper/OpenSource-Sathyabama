# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
lambdas = list(map(float, input().split()))
lambda_a = lambdas[0]
lambda_b = lambdas[1]

# Gets the result and show on the screen
print (round(160 + 40 * (lambda_a + lambda_a ** 2), 3))
print (round(128 + 40 * (lambda_b + lambda_b ** 2), 3))
