DIGITS = "149"


def countSpecificNumbers(i: int) -> bool:
    for digit in str(i):
        if digit not in DIGITS:
            return False
    return True

count = 0
for i in range(1, 100 + 1):
    if (countSpecificNumbers(i)):
        count += 1
print(count)
