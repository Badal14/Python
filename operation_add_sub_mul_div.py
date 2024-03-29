num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
opr = input("Which operation do you want to perform [add, mul, div, sub]\n")

if opr == "add":
    result = num1 + num2
    print("Addition of two numbers is:", result)
elif opr == "sub":
    result = num1 - num2
    print("Subtraction of two numbers is:", result)
elif opr == "mul":
    result = num1 * num2
    print("Multiplication of two numbers is:", result)
elif opr == "div":
    if num2 != 0:  # Check if the denominator is not zero to avoid division by zero error
        result = num1 / num2
        print("Division of two numbers is:", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation. Please enter add, sub, mul, or div.")
