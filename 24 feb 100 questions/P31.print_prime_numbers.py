# Read input
N = int(input("Enter a positive integer N: "))

print(f"Prime numbers between 1 and {N} are:")

# Loop through numbers from 2 to N
for num in range(2, N + 1):
    is_prime = True
    # Check divisibility from 2 to sqrt(num)
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")
        #-----------------------------------

        #Input:
#Enter a positive integer N: 10

#Output:
#Prime numbers between 1 and 10 are:
#2 3 5 7