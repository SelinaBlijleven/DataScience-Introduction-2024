"""
NumPy Datatypes Cheatsheet

The datatypes for NumPy have a strong relation with datatypes in C, as NumPy is programmed in C.
Regular python lists tend to be much slower, because they have a lot of overhead. NumPy prevents
the overhead by only allowing a singular datatype in each list. While the python array is also efficient,
we will see that NumPy also offers us easy operations for this data, making it the superior choice for
data management of any kind.
"""
import numpy as np

"""
Numpy and Integers

NumPy has several different types of integers. These integers can be unsigned (uint), indicating 
that they are only able to hold 0 or positive values. We can distinguish between these types 
by looking at the number of bits they take up and take the bit for the sign into account to get 
to the following ranges:

Unsigned (positive values only):
np.uint8     8 bits      0 to 2^8-1       0-255         Notice that we have to subtract one to store zero
np.uint16    16 bits     0 to 2^16-1      0-65536   
np.uint32    32 bits     0 to 2^32-1      0-4294967295
np.uint64    64 bits     0 to 2^64-1      0-18446744073709551615

Signed (positive & negative values):
np.int8     8 bits      -2^(8-1)  to 2^(8-1) - 1        -128 to 127
np.int16    16 bits     -2^(16-1) to 2^(16-1) - 1       -32768 to 32767
np.int32    32 bits     -2^(32-1) to 2^(32-1) - 1       -2147483648 to 2147483647
np.int64    64 bits     -2^(64-1) to 2^(64-1) - 1       -9223372036854775808 to 9223372036854775807 
"""
int_types = [
    np.int8, np.int16, np.int32, np.int64,
    np.uint8, np.uint16, np.uint32, np.uint64
]

"""
Floating point numbers

Spicy background article on floating point operations:
https://en.wikipedia.org/wiki/IEEE_754-1985

But all we need to know is:
np.float32  32 bits     Approximately 7 decimal digits
np.float64  64 bits     Approximately 16 digital digits

np.float17
"""
float_types = [np.float32, np.float64]

""" Upcasting mixed integers/floats """
# Creating a NumPy array from a mixed list
mixed_array = np.array([1, 2.5, 3, 4.7, 5])

# Checking the data type of the array
print(
    f"Array with type {mixed_array.dtype}: \n"
    f"{mixed_array}"
)

""" Complex datatypes """
complex_types = [np.complex64, np.complex128]

""" The boolean datatypes uses only one bit """
bool_type = np.bool_

""" Strings have a variable length """
str_type = np.str_

""" Objects also have different sizes """
obj_type = np.object_

import numpy as np

""" Date and Time Datatypes """

# Creating a date array
date_array = np.array(['2023-01-01', '2023-02-01', '2023-03-01'], dtype='datetime64[D]')
print(f"Date array: {date_array}")

# Creating a time array
time_array = np.array(['2023-01-01T12:00', '2023-02-01T13:30', '2023-03-01T15:45'], dtype='datetime64[m]')
print(f"Time array: {time_array}")

# Creating an array with a time delta
time_delta_array = np.array([1, 2, 3], dtype='timedelta64[D]')
print(f"Time delta array: {time_delta_array}")

# Demonstrating operations with datetime
start_date = np.datetime64('2023-01-01')
end_date = start_date + np.timedelta64(10, 'D')
print(f"Start date: {start_date}, End date (10 days later): {end_date}")

# Current date and time
current_datetime = np.datetime64('now')
print(f"Current date and time: {current_datetime}")

""" Data type sizes in bytes (1 byte = 8 bit) """
sizes = {
    np.int8: 1, np.int16: 2, np.int32: 4, np.int64: 8,
    np.uint8: 1, np.uint16: 2, np.uint32: 4, np.uint64: 8,
    np.float16: 2, np.float32: 4, np.float64: 8,
    np.complex64: 8, np.complex128: 16,
    np.bool_: 1,
    np.str_: 0,         # Variable-length string
    np.object_: 0,      # Variable-length object
    np.datetime64: 8
}
