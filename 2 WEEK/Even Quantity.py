element = 3423
k = 0
while element != 0:
    element = int(input())
    if element == 0:
        continue
    if element % 2 == 0:
        k += 1
print(k)
