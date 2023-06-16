import random as r


listOfElems = list(range(0, 10))
r.shuffle(listOfElems)

print("Before sorting: ")
print(listOfElems)

listOfElems.sort()
print("After Sorting: ")
print(listOfElems)

listOfElems.sort(reverse=True)
print("After Sorting by Reverse: ")
print(listOfElems)
