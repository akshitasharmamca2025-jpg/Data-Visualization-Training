# Read input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Make copies of the original numbers for display if needed
x, y = abs(a), abs(b)  # Use absolute values

# Euclidean algorithm using while loop
while y != 0:
    remainder = x % y
    x = y
    y = remainder

# Print the GCD
print(f"GCD of {a} and {b} is: {x}")
#------------------------------------------------------

#Input:
#Enter first number: 48
#Enter second number: 18

#Output:
#GCD of 48 and 18 is: 6