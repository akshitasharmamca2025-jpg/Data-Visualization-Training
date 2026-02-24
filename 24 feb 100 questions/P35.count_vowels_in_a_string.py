# Read input
text = input("Enter a string: ")

# Initialize vowel count
vowel_count = 0
vowels = "aeiouAEIOU"

# Loop through each character
for char in text:
    if char in vowels:
        vowel_count += 1

# Print the result
print("Number of vowels in the string:", vowel_count)

#-----------------------------------------------------------

#Input:
#Enter a string: Hello World

#Output:
#Number of vowels in the string: 3