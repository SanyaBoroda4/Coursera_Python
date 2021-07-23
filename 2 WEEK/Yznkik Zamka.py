a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (a <= d and b <= e) or\
   (b <= d and a <= e) or\
   (c <= d and a <= e) or\
   (c <= d and b <= e) or\
   (c <= e and a <= d) or\
   (c <= e and b <= d):
    print("YES")
else:
    print("NO")
