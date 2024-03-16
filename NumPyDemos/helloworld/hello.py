import numpy as np  # import the NumPy library

# NumPy arrays are basically just Python lists with added features.
# dtype is optional. https://numpy.org/doc/stable/user/basics.types.html

# Initializing a NumPy array
arr = np.array([-1, 2, 5], dtype=np.float32)
print('Single Dimension Array: ', repr(arr))

arr = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.float32)
print('Double Dimension Array: ', repr(arr))

# When the elements of a NumPy array are mixed types, then the array's type will be upcast to the highest level type.
arr = np.array([0, 0.1, 2])
print('Single Dimension Array: ', repr(arr))
