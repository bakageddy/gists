def isLeap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return True
    else:
        return False


starting_year = int(input("Enter starting year: "))
ending_year = int(input("Enter ending year: "))

count = 0
for i in range(starting_year, ending_year + 1):
    if (isLeap(i)):
        count += 1
    print("Year: ", i, "Leap Year?: ", isLeap(i))

print("Leap Year count: ", count)
