database = dict()

entries = int(input("Enter the number of entries: "))

for _ in range(entries):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    database[name] = age


name = input("Enter name to delete: ")
print("Before delete: ", database)
del database[name]

print("After delete: ", database)
