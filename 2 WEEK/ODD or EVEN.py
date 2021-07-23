a = int(input())
b = int(input())
c = int(input())

if a % 2 == b % 2 == c % 2 == 0 or a % 2 == b % 2 == c % 2 != 0:
    print("NO")
else:
    print("YES")
