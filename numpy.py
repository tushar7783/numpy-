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
