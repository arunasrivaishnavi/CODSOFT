def calculator():
    N=float(input("Enter first number "))
    M=float(input("Enter second number "))
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice:1/2/3/4 "))
    if choice == 1:
        result = N + M
        print(f"{N} + {M} = {result}")
    elif choice == 2:
        result = N - M
        print(f"{N} - {M} = {result}")
    elif choice == 3:
        result = N * M
        print(f"{N} * {M} = {result}")
    elif choice == 4:
        if M != 0:
            result = N / M
            print(f"{N} / {M} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please choose a valid operation.")   
calculator()