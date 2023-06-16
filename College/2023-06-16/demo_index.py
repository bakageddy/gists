listOfElems = list(range(0, 10))

elem = int(input("Enter a element: "))

try:
    index = listOfElems.index(elem)
    print("Index of", elem, "is:", index)
except ValueError:
    print("Element not found!")
