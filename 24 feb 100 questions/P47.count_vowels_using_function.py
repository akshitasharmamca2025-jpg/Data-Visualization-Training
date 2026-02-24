# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Read input
string = input("Enter a string: ")

# Call function and print result
result = count_vowels(string)
print("Number of vowels:", result)
#---------------------------------------------------

#Input:
#Enter a string: Programming

#Output:
#Number of vowels: 3