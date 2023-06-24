while True:
    option = int(input("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
Enter your option: """))
    if (option == 5):
        break

    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))

    if (option == 1):
        result = a + b
    elif (option == 2):
        result = a - b
    elif (option == 3):
        result = a * b
    elif (option == 4):
        result = a / b
    else:
        print("Wrong option!")
        continue
    print("Result: ", result)
