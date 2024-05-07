"""
default_integer_size.py

Use this script to check the default integer size, in case you are curious.

This can be influenced by several factors:
1. CPU architecture
2. Your operating system
3. Python interpreter and NumPy installation
4. Compiler options
5. Library dependencies
"""
import numpy as np

# Check the default integer data type
default_int_type = int

# Check the size of the default integer data type in bytes
size_in_bytes = np.dtype(default_int_type).itemsize

if size_in_bytes == 4:
    print("Default integer data type in NumPy is int32.")
elif size_in_bytes == 8:
    print("Default integer data type in NumPy is int64.")
else:
    print("Default integer data type in NumPy is not int32 or int64.")
