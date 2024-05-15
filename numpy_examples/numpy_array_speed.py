"""
numpy_array_speed.py

I had ChatGPT write this script to make a point: you need to use NumPy for any kind of heavy number lifting. Through
experimentation, I have found that 100000000 is the maximum number of zeroes before my current setup hits a memory
limit.

The reason for this is the overhead needed to store a list using mixed types (which is Python's default), which makes
computation slow. NumPy not only allows us to create type-specific arrays, but also to perform efficient computations
using the data. It is essential for scientific Python!
"""
import numpy as np
import time

# Number of elements in the array/list
size = 100000000

# Creating a NumPy array
start_time1 = time.time()
np_arr = np.arange(size)
numpy_time = time.time() - start_time1

# Creating a Python list
start_time2 = time.time()
py_list = list(range(size))
python_list_time = time.time() - start_time2

# Accessing elements
# For NumPy array
start_time4 = time.time()
for _ in range(1000):
    val = np_arr[size // 2]
numpy_access_time = (time.time() - start_time4) / 1000

# For Python list
start_time5 = time.time()
for _ in range(1000):
    val = py_list[size // 2]
python_list_access_time = (time.time() - start_time5) / 1000

print("Creation Time:")
print("NumPy Array:", numpy_time)
print("Python List:", python_list_time)

# If we are very fast, we might have a time of 0
if numpy_time != 0:
    print(f"NumPy is {round(python_list_time/numpy_time, 2)} times faster!")

print("\nAccess Time (per access):")
print("NumPy Array:", numpy_access_time)
print("Python List:", python_list_access_time)
