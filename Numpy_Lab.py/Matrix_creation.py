import numpy as np

# Create array from 1 to 20
arr = np.arange(1, 21)

# Reshape into 4x5 matrix
matrix = arr.reshape(4, 5)

print(matrix)

#output:
#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]]