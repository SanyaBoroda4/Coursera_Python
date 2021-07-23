password = "1234"
count = 1
quess = input("Please, enter password: ")
while quess != password:
    count += 1
    print("Wrong password")
    quess = input("Please, enter password: ")
print("You have used", count, "attempts")
