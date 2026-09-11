import numpy as np

# 1-D array with a single element
arr = np.array(['a'])

# 1-D array with multiple elements
arr_1 = np.array(['a', 'b'])

# 2-D array (rows and columns)
arr_2 = np.array([
    ['a', 'b'],
    ['c', 'd']
])

# 3-D array (depth, rows, columns)
arr_3 = np.array([
    [['a', 'b'], ['c', 'd']],
    [['a', 'b'], ['c', 'd']],
    [['a', 'b'], ['c', 'd']]
])

# Print array and its dimensions
print(arr)
print(arr.ndim)      # ndim = number of dimensions

print(arr_1)
print(arr_1.ndim)

print(arr_2)
print(arr_2.ndim)

print(arr_3)
print(arr_3.ndim)

# Shape shows size in each dimension
# (3, 2, 2) means:
# 3 blocks, each containing 2 rows and 2 columns
print(arr_3.shape)


# ===================================================
# SLICING
# ===================================================

array = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
])

print(array)

print('-----------------------------------------------')

# Syntax:
# array[start:end:step]

# =====================
# ROW SLICING
# =====================

# First row
print(array[0])

print('-----------------------------------------------')

# Rows 0 to 2 (excluding row 3)
print(array[0:3:])

# From row 0 to second-last row
print(array[0:-1:])

# All rows with step size 1
print(array[::1])

print('-----------------------------------------------')
print('reverse')

# Reverse all rows
print(array[::-1])

# =====================
# COLUMN SLICING
# ==================

print('-----------------------------------------------')

# Select all rows and columns 0 to 2
# ":" before comma means all rows
# "0:3" after comma means columns 0,1,2
print(array[:, 0:3])

# Select all rows and all columns up to column index 3
print(array[:, :4])

# Select entire array
print(array[:, :])
print('-----------------------------------------------')

# Arithmetic Operations
# Scalar Arithmetic: operation is performed on every element of the array

arrray = np.array([1, 2, 3, 4])

print(arrray + 1)    # Add 1 to each element
print(arrray - 1)    # Subtract 1 from each element
print(arrray * 10)   # Multiply each element by 10
print(arrray / 4)    # Divide each element by 4
print(arrray ** 2)   # Square each element

print('-----------------------------------------------')

# Mathematical Functions (Vectorized Operations)
# NumPy applies the function to all elements automatically

print(np.sqrt(arrray))      # Square root of each element
print(np.round(arrray, 2))  # Round values to 2 decimal places

radii = np.array([32, 55, 66, 33])

# Area of circles: πr²
print(np.pi * radii ** 2)

print('-----------------------------------------------')

# Element-wise Operations
# Corresponding elements are operated on together

print(arrray + radii)   # Addition
print(arrray - radii)   # Subtraction
print(arrray * radii)   # Multiplication
print(radii / arrray)   # Division
print(arrray ** 2)      # Square of each element

print('-----------------------------------------------')

# Comparison Operations

scores = np.array([91, 89, 99, 100, 55, 54])

print(scores)

# Returns a Boolean array
# True where condition is satisfied, otherwise False

print(scores == 100)  # Check which values are equal to 100
print(scores > 60)    # Check which values are greater than 60

# Boolean Indexing
# Select elements less than 60 and replace them with 0

scores[scores < 60] = 0

print(scores)   # Updated array

