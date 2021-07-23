a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    a, b, c = c, b, a
if b > a > c:
    a, b, c = c, a, b
if c > a > b:
    a, b, c = b, a, c
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a > b:
#     a, b = b, a
print(a, b, c)