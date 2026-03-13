import numpy as np

# Create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5, 5))

# Find minimum and maximum values
min_val = matrix.min()
max_val = matrix.max()

print("Matrix:")
print(matrix)
print("Min =", min_val)
print("Max =", max_val)

#output :
#Matrix:
#[[23 45 12 89 34]
#[67 11 90 54 32]
#[76 28 19 47 65]
# [14 73 52 39 81]
# [60 21 48 70 16]]

Min = 11
Max = 90