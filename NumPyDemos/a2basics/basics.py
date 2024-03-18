import numpy as np  # import the NumPy library

# NumPy arrays are basically just Python lists with added features.
# dtype is optional. https://numpy.org/doc/stable/user/basics.types.html
# Ranged data = The function acts very similar to the range function in Python, and will always return a 1-D array.
# Like np.array, np.arange performs upcasting. It also has the dtype keyword argument to manually cast the array.


def print_numpy_data(data):
    print('Data: ', data, 'Repr: ', repr(data), 'Type: ', data.dtype)


def show_numpy_ranged_data():
    print('\nShow numpy ranged data')

    # If only a single number, n, is passed in as an argument, np.arange will return an array with all the integers in the range [0, n). Note: the lower end is inclusive while the upper end is exclusive.
    print_numpy_data(np.arange(10))  # 0 to 9, step 1
    print_numpy_data(np.arange(5))  # 0 to 4, step 1
    print_numpy_data(np.arange(5.1))  # 0 to 5, step 1

    # If two numbers, m and n, are passed in, np.arange will return an array with all the integers in the range [m, n).
    print_numpy_data(np.arange(2, 10))  # 2 to 9, step 1
    print_numpy_data(np.arange(-1, 4))  # -1 to 3, step 1
    print_numpy_data(np.arange(-1.5, 4, 2))  # -1.5 to 2.5, step 2

    # If three numbers, m, n, and s, are passed in, np.arange will return an array with all the integers in the range [m, n) using a step size of s.
    print_numpy_data(np.arange(0, 10, 1))  # 0 to 9
    print_numpy_data(np.arange(0, 10, 2))  # 0 to 8, step 2
    print_numpy_data(np.arange(0, 10, 3))  # 0 to 9, step 3
    print_numpy_data(np.arange(10, 0, -1))  # 10 to 1, step -1
    print_numpy_data(np.arange(10, 0, -2))  # 10 to 2, step -2
    print_numpy_data(np.arange(10, 0, -3))  # 10 to 1, step -3


def show_numpy_linspace_data():
    print('\nShow numpy linspace data')

    # np.linspace is similar to np.arange, but instead of specifying the step size, the number of elements in the array is specified.
    # The first two arguments are the start and end of the range, and the third argument is the number of elements in the array.

    print_numpy_data(np.linspace(5, 11, num=3))  # 5 to 11, 4 elements
    print_numpy_data(np.linspace(5, 11, num=4))  # 5 to 11, 4 elements
    print_numpy_data(np.linspace(5, 11, num=5))  # 5 to 11, 4 elements

    print_numpy_data(np.linspace(5, 11, num=4, endpoint=False)
                     )  # 5 to 11, 4 elements
    print_numpy_data(np.linspace(5, 11, num=4, dtype=np.int32)
                     )  # 5 to 11, 4 elements

    print_numpy_data(np.linspace(0, 10, 5))  # 0 to 10, 5 elements
    print_numpy_data(np.linspace(0, 10, 6))  # 0 to 10, 6 elements
    print_numpy_data(np.linspace(0, 10, 11))  # 0 to 10, 11 elements
    print_numpy_data(np.linspace(0, 10, 12))  # 0 to 10, 12 elements
    print_numpy_data(np.linspace(0, 10, 13))  # 0 to 10, 13 elements


def show_numpy_reshaping_data():
    print('\nShow numpy reshaping data')

    # np.reshape is used to change the shape of an array. The array to be reshaped is passed in as the first argument, and the new shape is passed in as the second argument.
    # The new shape must have the same number of elements as the original shape. The new shape can be passed in as a tuple or as a series of numbers.

    # Reshape 1D to 2D
    data = np.arange(6)
    print_numpy_data(data)
    print_numpy_data(data.reshape(2, 3))
    print_numpy_data(data.reshape((2, 3)))

    # Reshape 2D to 1D
    data = np.arange(6).reshape(2, 3)
    print_numpy_data(data)
    print_numpy_data(data.reshape(6))
    print_numpy_data(data.reshape((6)))

    # Reshape 1D to 3D
    data = np.arange(24)
    print_numpy_data(data)
    print_numpy_data(data.reshape(2, 3, 4))
    print_numpy_data(data.reshape((2, 3, 4)))

    # Reshape 3D to 1D
    data = np.arange(24).reshape(2, 3, 4)
    print_numpy_data(data)
    print_numpy_data(data.reshape(24))
    print_numpy_data(data.reshape((24)))

    # Reshape 2D to 3D
    data = np.arange(24).reshape(4, 6)
    print_numpy_data(data)
    print_numpy_data(data.reshape(2, 3, 4))
    print_numpy_data(data.reshape((2, 3, 4)))

    # Reshape 3D to 2D
    data = np.arange(24).reshape(2, 3, 4)
    print_numpy_data(data)
    print_numpy_data(data.reshape(4, 6))
    print_numpy_data(data.reshape((4, 6)))

    # Reshape 2D to 3D
    data = np.arange(24).reshape(4, 6)
    print_numpy_data(data)
    print_numpy_data(data.reshape(2, 3, 4))
    print_numpy_data(data.reshape((2, 3, 4)))

    arr = np.arange(8)
    reshaped_arr = np.reshape(arr, (2, 4))
    print_numpy_data(reshaped_arr)
    print('New shape: {}'.format(reshaped_arr.shape))

    reshaped_arr = np.reshape(arr, (-1, 2, 2))
    print_numpy_data(reshaped_arr)
    print('New shape: {}'.format(reshaped_arr.shape))


show_numpy_ranged_data()

show_numpy_linspace_data()

show_numpy_reshaping_data()
