# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Read input
num = int(input("Enter a number: "))

# Check prime and print result
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    #--------------------------------------------------------

    #Input:
#Enter a number: 20

#Output:
#20 is not a prime number