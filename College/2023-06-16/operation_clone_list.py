listOfElems = list(range(0, 10))
anotherList = list()

# listOfElems.copy() works too
for i in listOfElems:
    anotherList.append(i)

print("Original: ")
print(listOfElems, end="\n\n")

print("Clone: ")
print(anotherList, end="\n\n")

print("Modifying original list: ")
listOfElems[3] = 69
print(listOfElems, end="\n\n")

print("Cloned list: ")
print(anotherList, end="\n\n")
