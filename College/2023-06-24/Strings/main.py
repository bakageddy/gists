STR = "Was he dead? Dead as a doornail she said. Good heavens That's right she said."
separatedWords = STR.split()
print(separatedWords)

requiredLength = int(input("Enter a number: "))

ans = [i for i in separatedWords if len(i) > requiredLength]
# Equivalent to ...
# ans = []
# for i in separatedWords:
#     if (len(i) > requiredLength):
#         ans.append(i)

print(ans)
