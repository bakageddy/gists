import datetime


print("Date: ")
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
date1 = datetime.date(day=day, month=month, year=year)

print("Another Date: ")
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
date2 = datetime.date(day=day, month=month, year=year)

print("Difference:")
print(date2 - date1)
