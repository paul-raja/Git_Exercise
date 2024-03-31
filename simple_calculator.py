# Define a function to perform the selected calculation on two numbers.
def perform_calculation(number1, number2, calculation):
    # Check which calculation was chosen and return the appropriate result.
    if calculation == "sum":
        return number1 + number2
    elif calculation == "multiplication":
        return number1 * number2
    elif calculation == "subtraction":
        return number1 - number2
    elif calculation == "division":
        # Ensure the second number is not zero to avoid division by zero error.
        if number2 != 0:
            return number1 / number2
        else:
            return "Cannot divide by zero."
    else:
        # Return an error message if an invalid calculation was selected.
        return "Invalid calculation"

# Main function to interact with the user and utilize the calculation function.
def main():
    # Prompt the user for the first number and convert it to a float for mathematical operations.
    number1 = float(input("Enter the first number: "))
    # Prompt the user for the second number and convert it to a float.
    number2 = float(input("Enter the second number: "))
    # Ask the user to choose a calculation.
    calculation = input("Choose the calculation (sum, multiplication, subtraction, division): ").lower()
    
    # Call the perform_calculation function with the user's input and store the result.
    result = perform_calculation(number1, number2, calculation)
    # Print the result of the calculation to the user.
    print(f"The result is: {result}")

# Check if this script is the main program and not being imported by another script.
if __name__ == "__main__":
    main()