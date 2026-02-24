# Read input
n = int(input("Enter a non-negative integer: "))

# Initialize factorial
factorial = 1

# Calculate factorial using for loop
for i in range(1, n + 1):
    factorial *= i

# Print the result
print(f"Factorial of {n} is {factorial}")
#---------------------------------------------------------

#Input:
#Enter a non-negative integer: 5

#Output:
#Factorial of 5 is 120