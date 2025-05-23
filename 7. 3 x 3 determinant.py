import numpy as np

# Define a 3x3 matrix (you can modify these values)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 7, 9]])

# Extract elements
a, b, c = A[0]
d, e, f = A[1]
g, h, i = A[2]

# Compute determinant manually 
det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

# Display result
print("Matrix:")
print(A)
print("\nDeterminant:", det)
