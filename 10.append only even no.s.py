import numpy as np

arr = np.array([1, 2, 3])
to_add = np.array([4, 5, 6])

# Filter even numbers
even = to_add[to_add % 2 == 0]

# Append
arr = np.append(arr, even)

print(arr)