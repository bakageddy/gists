def newton_sqrt(number) -> float:
    guess = 1
    guess = 0.5 * (guess + (number / guess))
    while True:
        guess = 0.5 * (guess + (number / guess))
        squared = guess * guess
        diff = squared - number
        if diff < 0:
            diff = -diff

        if diff < 0.1:
            break
    return guess


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b * b) - (4 * a * c)
if (d < 0):
    print("Complex roots...")
    exit(1)

x1 = ((-b) + newton_sqrt(d))/(2 * a)
x2 = ((-b) - newton_sqrt(d))/(2 * a)
print("Roots: ")
print(x1, x2)
