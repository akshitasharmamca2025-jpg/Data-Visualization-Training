# Function to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Read input
x = int(input())
y = int(input())

# Print result
print(gcd(x, y))
#---------------------------------

#Input:
48
18

#Output:
6