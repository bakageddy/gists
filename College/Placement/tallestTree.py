class Tree:
    def __init__(self, feets, inches):
        self.feets = feets
        self.inches = inches
    
    def height(self):
        return self.feets * 12 + self.inches

values = [(10, 4), (23, 5), (21, 2), (27, 7)]
result = 0
for feet, inches in values:
    result = max(result, Tree(feet, inches).height())
print(result)
