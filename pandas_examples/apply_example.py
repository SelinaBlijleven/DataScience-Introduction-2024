"""
apply_example.py

Use one data column to generate data for another
"""
import numpy as np
import pandas as pd

a, b = 1, 5

x_data = np.linspace(1, 10, 100)
df = pd.DataFrame(x_data, columns=['x'])

# adding 5 to each value
df['y'] = df['x'].apply(lambda x: a * x + b)

# printing first 5 elements of old and new series
print(df.head())
