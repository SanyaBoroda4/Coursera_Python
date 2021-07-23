k = int(input())

if k % 3 == 0 or k % 5 == 0:
    print("YES")
elif k % 3 % 5 == 0 or k % 5 % 3 == 0:
    print("YES")
else:
    print("NO")
