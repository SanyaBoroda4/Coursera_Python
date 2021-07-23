a = int(input())
b = int(input())
if a == 1:
    print("YES")
elif b % (b - a + 1) == 0:
    print("YES")
else:
    print("NO")
