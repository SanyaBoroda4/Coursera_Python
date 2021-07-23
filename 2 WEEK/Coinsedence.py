a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)

# or like this

num = set([int(input()) for i in range(3)])
if len(num) == 3:
    print(0)
if len(num) == 2:
    print(2)
if len(num) == 1:
    print(3)
