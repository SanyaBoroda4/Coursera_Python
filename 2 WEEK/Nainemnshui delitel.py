n = int(input())
x = 2
while x >= 2:
    if n % x != 0:
        x += 1
    else:
        print(x)
        break
