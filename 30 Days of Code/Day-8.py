# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input().strip())
phonebook = {}
for i in range(n):
    line = input()
    k, v = line.split()
    phonebook[k] = v

while True:
    try:
        number = input()
    except EOFError:
        break
    if number in phonebook:
        print("{}={}".format(number, phonebook[number]))
    else:
        print("Not found")
