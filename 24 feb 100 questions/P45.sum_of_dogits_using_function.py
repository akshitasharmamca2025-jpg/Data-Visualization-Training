# Function to calculate sum of digits
def sum_of_digits(n):
    n = abs(n)  # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Read input
num = int(input("Enter a number: "))

# Calculate sum of digits using the function
digit_sum = sum_of_digits(num)

# Print the result
print(f"Sum of digits of {num} is: {digit_sum}")
#-----------------------------------------------------------------

#Input:
#Enter a number: 1234

#Output:
#Sum of digits of 1234 is: 10