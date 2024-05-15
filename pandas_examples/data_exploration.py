"""
data_exploration.py
"""
import pandas as pd
import seaborn as sns

df = sns.load_dataset('planets')

print(df.info())
print(df.describe())
print(df.head())
print()
print(df.dtypes.values)
