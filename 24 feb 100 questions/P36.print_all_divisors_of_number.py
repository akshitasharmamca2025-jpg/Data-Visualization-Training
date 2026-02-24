# Read input
num = int(input("Enter a positive integer: "))

print(f"Divisors of {num} are:")

# Loop through numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        #---------------------------------------

        #Input:
#Enter a positive integer: 12

#Output:
#Divisors of 12 are:
#1 2 3 4 6 12