hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

time_in_seconds_1 = hours_1*3600 + minutes_1*60 + seconds_1
time_in_seconds_2 = hours_2*3600 + minutes_2*60 + seconds_2

print(time_in_seconds_2 - time_in_seconds_1)
