example_list = list(range(1, 10))
print(example_list)

reference_to_list = example_list.copy()

print("Before modifying: ")
print(reference_to_list)
reference_to_list[1] = 69
print("After modifying: ")
print(reference_to_list)
