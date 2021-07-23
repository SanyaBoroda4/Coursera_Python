n = int(input())
if n in range(5, 20):
        print(n, "korov")
else:
    temp = n % 10
    if temp == 1:
        print(n, "korova")
    elif temp in range(2, 5):
        print(n, "korovy")
    else:
        print(n, "korov")
