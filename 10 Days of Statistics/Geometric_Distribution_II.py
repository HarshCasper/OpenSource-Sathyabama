# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

# Show the final result
print(round(result, 3))
