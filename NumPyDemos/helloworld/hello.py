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

arr5 = np.array([np.nan, 1, 2])
print(repr(arr5))

arr6 = np.array([np.nan, 'abc'])
print(repr(arr6))

#np.array([np.nan, 1, 2], dtype=np.int32) # ValueError => cannot convert float NaN to integer
np.array([np.nan, 1, 2], dtype=np.float32)


def show_infinity():
    print(np.inf)
    print(-np.inf)

    print(np.inf > 1000000)

    arr = np.array([np.inf, 5])
    print(repr(arr))

    arr = np.array([-np.inf, 1])
    print(repr(arr))

    # np.array([np.inf, 3], dtype=np.int32) # ValueError => cannot convert float inf to integer
    np.array([np.inf, 3], dtype=np.float32)

show_infinity()