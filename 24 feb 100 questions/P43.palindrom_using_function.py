# Function to check palindrome
def is_palindrome(s):
    s = s.lower()  # Optional: ignore case
    return s == s[::-1]  # Compare string with its reverse

# Read input
text = input("Enter a string: ")

# Check and print result
if is_palindrome(text):
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')
    #-----------------------------------------------------------------

    #Input:
#Enter a string: Madam

#Output:
#"Madam" is a palindrome