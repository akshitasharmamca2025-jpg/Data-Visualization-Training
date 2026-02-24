# Function to find maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find maximum using the function
max_num = maximum(num1, num2, num3)

# Print the result
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_num}")

#------------------------------------------------------------------------------

#Input:
#Enter first number: 12
#Enter second number: 45
#Enter third number: 30

#Output:
#The maximum of 12.0, 45.0, and 30.0 is: 45.0