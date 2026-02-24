# Read input
N = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

print("Fibonacci series:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b  # Update a and b to next terms

    #-------------------------------------------------------

    #Input: 
#Enter the number of terms: 7

#Output:
#Fibonacci series:
#0 1 1 2 3 5 8