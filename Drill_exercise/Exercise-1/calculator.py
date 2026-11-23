def cal():
    a_input = int(input("Enter first number: "))
    opt = input("enter the operator")
    b_input = int(input("Enter first number: "))
    
    
    if opt == "+":
        print(a_input + b_input)
    elif opt == "-":
        print(a_input - b_input)
    elif opt == "*":
        print(a_input - b_input)
    elif opt == "/":
        if b_input == 0:
            print("Error: Cannot divide by zero!")
            return
        else:
             print(a_input / b_input)

    else:
        print("invalid operator")

cal()