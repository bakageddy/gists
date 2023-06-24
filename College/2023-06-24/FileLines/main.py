filename = input("Enter file: ")
try:
    with open(filename) as handle:
        lines = len(handle.read().splitlines())
        print("Lines: ", lines)
except FileNotFoundError:
    print("File not found!")
