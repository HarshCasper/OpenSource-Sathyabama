# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

# Set data
mean = float(input())
k = float(input())
e = 2.71828

# Gets the result and show on the screen
result = ((mean ** k) * (e ** -mean)) /  factorial(k)
print(round(result, 3))
