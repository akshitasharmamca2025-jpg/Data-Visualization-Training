# Print multiplication tables from 1 to 10
for num in range(1, 11):  # Outer loop for numbers 1 to 10
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):  # Inner loop for 1 to 10
        print(f"{num} x {i} = {num * i}")
    print()  # Blank line after each table
    #--------------------------------------------------

    #Multiplication Table of 1:
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
...
#Multiplication Table of 2:
#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
...