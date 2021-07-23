line1 = int(input())
column1 = int(input())
line2 = int(input())
column2 = int(input())

if abs(line1 >= line2 - 1) and abs(column1 >= column2 - 1):
    print("YES")
else:
    print("NO")
