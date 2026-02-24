# Read input
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent (integer): "))

# Initialize result
result = 1

# Handle negative exponents
if exponent >= 0:
    for _ in range(exponent):
        result *= base
else:
    for _ in range(-exponent):
        result *= base
    result = 1 / result  # Invert for negative exponent

# Print the result
print(f"{base} raised to the power {exponent} is: {result}")
#-----------------------------------------------------------------

#Input:
#Enter the base: 2
#Enter the exponent (integer): 3

#Output:
#2.0 raised to the power 3 is: 8.0