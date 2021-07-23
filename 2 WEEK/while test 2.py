now = int(input())
max_num = now
while max_num != 0:
    now = int(input())
    if now == 0:
        break
    if now > max_num:
        max_num = now
print(max_num)
