a = int(input())
b = int(input())
c = int(input())

h = max(a, b, c)
j = min(a, b, c)
k = (a + b + c) - (h + j)

if a > (b + c) or b > (a + c) or c > (a + b) or a < 0 or b < 0 or c < 0:
    print('impossible')
elif h**2 == j**2 + k**2:
    print('rectangular')
elif h**2 > j**2 + k**2:
    print('obtuse')
elif h**2 < j**2 + k**2:
    print('acute')
