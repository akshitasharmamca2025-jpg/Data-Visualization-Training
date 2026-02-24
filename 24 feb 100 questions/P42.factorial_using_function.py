# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Read input
num = int(input("Enter a non-negative integer: "))

# Calculate factorial using the function
fact = factorial(num)

# Print the result
print(f"Factorial of {num} is {fact}")
#-----------------------------------------------

#Input:
#Enter a non-negative integer: 5

#Output:
#Factorial of 5 is 120