x1 = int(input())  # начальная точка по вертикали
y1 = int(input())  # начальная точка по горизонтали
x2 = int(input())  # ход по вертикали
y2 = int(input())  # ход по горизонтали

if x2 > x1 and y2 > y1 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    if (x1 + x2) % 2 == (y1 + y2) % 2:
        print('YES')
    else:
        print("NO")
else:
    print("NO")
