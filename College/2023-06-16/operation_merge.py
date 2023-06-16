list1 = list(range(0, 10))
list2 = list(range(10, 20))

print("Before merging: ")
print(list1, list2, end="\n")

list1.extend(list2)
print("After merging: ")
print(list1)
