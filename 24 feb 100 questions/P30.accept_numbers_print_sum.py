# Initialize sum
total = 0

while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break  # Stop input when 0 is entered
    total += num

# Print the result
print("Sum of the entered numbers is:", total)
#-------------------------------------------------

#Input:
#Enter a number (0 to stop): 5
#Enter a number (0 to stop): 10
#Enter a number (0 to stop): -3
#Enter a number (0 to stop): 0

#Output:
#Sum of the entered numbers is: 12.0