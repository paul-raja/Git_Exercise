def perform_operation(number1, number2, operation):
    if operation == "sum":
        return number1 + number2
    elif operation == "multiplication":
        return number1 * number2
    elif operation == "subtraction":
        return number1 - number2
    elif operation == "division":
        if number2 != 0:
            return number1 / number2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation"

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (sum, multiplication, subtraction, division): ").lower()
    
    result = perform_operation(number1, number2, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()