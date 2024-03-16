import numpy as np  # import the NumPy library

# NumPy arrays are basically just Python lists with added features.
# dtype is optional. https://numpy.org/doc/stable/user/basics.types.html

# Initializing a NumPy array
arr = np.array([-1, 2, 5], dtype=np.float32)
print('Single Dimension Array: ', repr(arr))

arr1 = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.float32)
print('Double Dimension Array: ', repr(arr1))

# When the elements of a NumPy array are mixed types, then the array's type will be upcast to the highest level type.
arr2 = np.array([0, 0.1, 2])
print('Single Dimension Array: ', repr(arr2))

a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))

arr3 = np.array([10, 11, 12])
print(repr(arr3), arr3.dtype)

arr4 = arr3.astype(np.float32)
print(repr(arr4), arr4.dtype)