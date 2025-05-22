import numpy as np

arr = np.random.randint(0, 100, (5, 5))  # Example random 5x5 array
print("Original array:\n", arr)

# Extract border elements
top = arr[0, :]
bottom = arr[-1, :]
left = arr[1:-1, 0]
right = arr[1:-1, -1]

# Combine all border elements into one array
border = np.concatenate([top, right, bottom[::-1], left[::-1]])
print("Border elements:\n", border)