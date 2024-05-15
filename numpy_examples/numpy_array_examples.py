"""
numpy_array_examples.py

Some commonly used functions from NumPy in action!
"""
import numpy as np

"""
Creating arrays
"""
# From lists
a = np.array([1, 2, 3, 4])

# Multidimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])

# From ranges
# Usage:
# arange(stop)
# arange(start, stop)
# arange(start, stop, step)
c = np.arange(0, 10, 2)     # array([0, 2, 4, 6, 8])
c2 = np.arange(1, 11)       # array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c3 = np.arange(10)          # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# From zeros, ones, or a constant value
d = np.zeros((2, 3))     # 2x3 array of zeros
e = np.ones((2, 3))      # 2x3 array of ones
f = np.full((2, 3), 7)   # 2x3 array of sevens

# Identity matrix (multiplying with 1 for matrices)
# (https://en.wikipedia.org/wiki/Identity_matrix)
g = np.eye(3)

# Random arrays
# We can create different random arrays using the numpy random functions. For each of these we can
# specify a length for a list, or provide the shape for the matrix we wish to generate directly.
# Please note that randint has an equal likelihood for the different values.
h = np.random.rand(2, 3)                # Uniform distribution [0, 1): each value is equally likely
i = np.random.randn(2, 3)               # Standard normal distribution
j = np.random.randint(0, 10, 6)         # Random integers (list of values, 1D)
k = np.random.randint(0, 10, (2, 3))    # Random integers (matrix with specified shape)

"""
Array attributes 
"""
# Shape and size
print(a.shape)          # (4,)
print(b.shape)          # (2, 3)
print(a.size)           # 4
print(b.size)           # 6

# Data type
print(a.dtype)          # dtype('int64')

"""
Reshaping and transposing
https://en.wikipedia.org/wiki/Transpose
"""
# Reshaping
a_reshaped = np.reshape(a, (2, 2))        # array([[1, 2], [3, 4]])

# Transposing
mt = np.transpose(b)              # array([[1, 4], [2, 5], [3, 6]])

