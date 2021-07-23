N = int(input())
hours = N // 3600 % 24
minutes = str(N // 60 % 60 // 10) + str(N // 60 % 60 % 10)
seconds = str(N % 3600 % 60 // 10) + str(N % 3600 % 60 % 10)
print(hours, minutes, seconds, sep=":")

