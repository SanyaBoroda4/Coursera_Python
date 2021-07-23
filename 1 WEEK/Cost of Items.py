
a = int(input("Please input how much dollars Item 1 costs: "))
b = int(input("Please input how much cents Item 1 costs: "))
c = int(input("Please input how much dollars Item 2 costs: "))
d = int(input("Please input how much cents Item 2 costs: "))


item1_Cost = a * 100 + b
item2_Cost = c * 100 + d
total_Cost = item1_Cost + item2_Cost

print(total_Cost // 100, "Dollars", total_Cost % 10, "Cents")
