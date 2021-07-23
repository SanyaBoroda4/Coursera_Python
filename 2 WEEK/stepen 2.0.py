n = int(input())
i = 1
while i <= n:
    if n == 1:
        print("YES")
        break
    i *= 2
    if i == n:
        print("YES")
        break
else:
    print("NO")
