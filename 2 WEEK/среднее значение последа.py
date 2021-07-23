n = -323
k = 0
seq_sum = 0
while n != 0:
    n = int(input())
    if n == 0:
        continue
    k += 1
    seq_sum += n
    average = seq_sum / k
print(average)
