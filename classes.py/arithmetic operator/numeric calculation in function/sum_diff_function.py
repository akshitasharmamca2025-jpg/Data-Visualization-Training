# User-defined function to calculate addition and difference
def calculate_addition_difference(num1, num2):
    addition = num1 + num2
    difference = num1 - num2
    return addition, difference

# Main program to get user input and display results
def main():
    # Input numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the user-defined function
    addition, difference = calculate_addition_difference(num1, num2)
    
    # Output the results
    print(f"The addition of {num1} and {num2} is: {addition}")
    print(f"The difference between {num1} and {num2} is: {difference}")

# Run the main function
if __name__ == "__main__":
    main()