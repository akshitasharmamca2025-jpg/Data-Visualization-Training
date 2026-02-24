# Read input
num = int(input("Enter a number: "))
original_num = num  # Store original number
num_abs = abs(num)  # Use absolute value for calculation

# Find number of digits
n_digits = len(str(num_abs))

# Calculate sum of digits raised to the power of number of digits
sum_of_powers = 0
temp = num_abs
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n_digits
    temp //= 10

# Check if number is Armstrong
if sum_of_powers == num_abs:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    #------------------------------------------------

    #input:
#Enter a number: 153

#Output:
#153 is an Armstrong number