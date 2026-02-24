# Read a single character from input
char = input()

# Check if the character is a digit or alphabet
if char.isdigit():
    print("Digit")
elif char.isalpha():
    print("Alphabet")
else:
    print("Neither")
    #--------------------------------------

    #input: 7
    #output: Digit
