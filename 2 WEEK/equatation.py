a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print("INF")
elif a == 0:
    print("NO")
else:
    x = -b / a
    if str(x)[-2:] != '.0':  # если x не целое
        print('NO')
    else:
        if c * b != a * d:  # если при x=-b/a знаменатель не обращается в ноль
            print(int(x))
        else:
            print("NO")
