import pandas as pd

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
                'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                'hours_per_week', 'native_country', 'income']
df = pd.read_csv(url, names=column_names, na_values=' ?', skipinitialspace=True)

# Display the first few rows of the dataframe
print(f"Original Data ({len(df)} rows):")
print(df.head())

# Cleaning steps
# 1. Drop rows with missing values
df.dropna(inplace=True)

# 2. Remove leading and trailing whitespaces from categorical columns
df['workclass'] = df['workclass'].str.strip()
df['education'] = df['education'].str.strip()
df['marital_status'] = df['marital_status'].str.strip()
df['occupation'] = df['occupation'].str.strip()
df['relationship'] = df['relationship'].str.strip()
df['race'] = df['race'].str.strip()
df['sex'] = df['sex'].str.strip()
df['native_country'] = df['native_country'].str.strip()
df['income'] = df['income'].str.strip()

# Display the cleaned dataframe
print(f"\nCleaned Data ({len(df)} rows):")
print(df.head())
