import numpy as np

# Define Matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Define Matrix B
B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Perform matrix multiplication
C = np.dot(A, B)  # You can also use A @ B

print(C)


#output: [[ 30 24 18]
#         [ 84 69 54]
#         [ 138 114 90]]
