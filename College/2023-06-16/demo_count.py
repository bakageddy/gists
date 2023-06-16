listOfElems = list(range(0, 10))
listOfElems.extend(range(0, 10))


for i in listOfElems:
    # Should print 2 for every element
    print("Count of ", i, " is: ", listOfElems.count(i))
