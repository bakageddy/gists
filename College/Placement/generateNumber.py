def generate(a, b, c) -> int:
    nums = [a, b, c]
    nums.sort()
    result = ""
    for i in nums:
        result += str(i)
    return int(result)

print(generate(1, 2, 3))
print(generate(0, 0, 0))
