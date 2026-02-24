# Function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Read input
N = int(input("Enter the number of terms: "))

# Generate Fibonacci series using the function
fib_series = fibonacci_series(N)

# Print the result
print("Fibonacci series:")
print(*fib_series)

#----------------------------------------------------------------

#Input:
#Enter the number of terms: 7

#Output:
#Fibonacci series:
#0 1 1 2 3 5 8