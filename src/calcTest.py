num1 = float(input("enter a number: "))
op = input("enter an operation: ")
num2 = float(input("enter a number: "))

if op == "+":
    print(str(num1) + " + " + str(num2) + " = " + str((num1 + num2)))
elif op == "-":
    print(str(num1) + " - " + str(num2) + " = " + str((num1 - num2)))
elif op == "*":
    print(str(num1) + " * " + str(num2) + " = " + str((num1 * num2)))
elif op == "/":
    if num2 == 0:
        print("Error: Denominator must not equal 0")
    else:
        print(str(num1) + " / " + str(num2) + " = " + str((num1 / num2)))
