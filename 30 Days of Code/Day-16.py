# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")
