# Read input
text = input("Enter a string: ")

# Initialize reversed string
reversed_text = ""

# Loop through the string in reverse order
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Print the result
print("Reversed string:", reversed_text)
#---------------------------------------------------------

#Input:
#Enter a string: Hello World

#Output:
#Reversed string: dlroW olleH