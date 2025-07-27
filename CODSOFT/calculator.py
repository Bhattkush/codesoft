def calculator():
    print("Simple Calculator")
    print("------------------------")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    print("Choice an Opration")
    print("+ for Addtition")
    print("- for Substraction")
    print("/ for Division")
    print("* for Multiplication")

    opr = input("Enter your opration choice(+,-,/,*):")
    
    if opr == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif opr == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    
    elif opr == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif opr == '/':
        if num2 == 0:
            print("Math error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

    else:
        print("Invalid operation selected.")


calculator()
        
        
