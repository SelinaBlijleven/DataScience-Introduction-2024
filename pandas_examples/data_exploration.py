"""
data_exploration.py

These functions cover most of what we need to know about a dataframe in a human-readable format.
The DataFrame also has several properties to extract specifics in a machine format.
"""
import pandas as pd
import seaborn as sns

df = sns.load_dataset('planets')

print(df.info())
print(df.describe())
print(df.head())
