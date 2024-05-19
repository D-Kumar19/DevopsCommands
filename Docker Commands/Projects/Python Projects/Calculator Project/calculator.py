def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Enter operation (a for addition, s for subtraction, m for multiplication, d for division, r for remainder, x to exit): ").strip().lower()
        if operation in ['a', 's', 'm', 'd', 'r', 'x']:
            return operation
        else:
            print("Invalid operation. Please enter a valid operation.")

def perform_operation(num1, num2, operation):
    if operation == 'a':
        return num1 + num2
    elif operation == 's':
        return num1 - num2
    elif operation == 'm':
        return num1 * num2
    elif operation == 'd':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operation == 'r':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 % num2

def main():
    print("Welcome to the custom calculator!")
    print("You can perform operations using the following symbols:")
    print("a for addition, s for subtraction, m for multiplication, d for division, r for remainder, x to exit")

    while True:
        try:
            operation = get_operation()
            if operation == 'x':
                print("Exiting the calculator. Goodbye!")
                break

            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            result = perform_operation(num1, num2, operation)
            print(f"The result of the operation is: {result}\n")

        except KeyboardInterrupt:
            print("\nKeyboard interrupt received. Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
