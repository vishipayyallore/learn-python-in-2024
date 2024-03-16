import numpy as np  # import the NumPy library

# Initializing a NumPy array
arr = np.array([-1, 2, 5], dtype=np.float32)

# Print the representation of the array
print('Single Dimension Array: ', repr(arr))

arr = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.float32)

print('Double Dimension Array: ', repr(arr))
