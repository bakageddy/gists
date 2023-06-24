import sys


if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    exit(1)

filename = sys.argv[1]
with open(filename) as handle:
    contents = handle.read().split()
    counts = dict()
    for i in contents:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

print("Frequency count: ", counts)
