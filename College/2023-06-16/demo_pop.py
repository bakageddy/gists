listOfElems = list(range(0, 10))

for i in range(0, 10):
    value = listOfElems.pop()
    print("-" * 20)
    print("Deleted Value: ", value)
    print("List: ", listOfElems)
