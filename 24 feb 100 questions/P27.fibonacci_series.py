# Read input
N = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1
count = 0

# Generate Fibonacci series using while loop
while count < N:
    print(a, end=" ")
    a, b = b, a + b  # Update a and b to next Fibonacci terms
    count += 1
    #---------------------------------------------------------------------------

 #   Input:
#Enter the number of terms: 7

#Output:
#0 1 1 2 3 5 8