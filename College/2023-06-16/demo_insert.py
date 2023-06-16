import random as r


listOfElems = list(range(0, 10))

listOfElems.insert(r.randrange(0, len(listOfElems)), "Hello")
listOfElems.insert(r.randrange(0, len(listOfElems)), "There")

print(listOfElems)
