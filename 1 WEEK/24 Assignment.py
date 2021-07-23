from math import ceil

h = int(input())
a = int(input())
b = int(input())
delta = a - b
n = ceil((h-a) / delta) + 1

print(n)
