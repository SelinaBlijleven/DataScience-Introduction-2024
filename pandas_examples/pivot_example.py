"""
pivot_example.py

Example showing the possibilities of generating pivot tables
for your data using Pandas.
"""
import pandas as pd

# Creating the DataFrame: We create a simple dataset with columns Date, Category, Sub-Category, Sales, and Quantity.
# Create a sample dataset
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sub-Category': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Sales': [100, 150, 200, 250, 300, 350],
    'Quantity': [10, 15, 20, 25, 30, 35]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

"""
Creating the Pivot Table: We use the pd.pivot_table function to create a pivot table:
values='Sales':                 The values we want to aggregate
index=['Date', 'Category']:     The rows of the pivot table will be multi-indexed by Date and Category
columns='Sub-Category':         Use the subcategories as the columns
aggfunc='sum':                  Aggregate the Sales by summing them up
fill_value=0:                   Fill missing values with 0
"""
# Create a pivot table
pivot_table = pd.pivot_table(df,
                             values='Sales',
                             index=['Date', 'Category'],
                             columns='Sub-Category',
                             aggfunc='sum',
                             fill_value=0)

print("\nPivot Table:")
print(pivot_table)

pivot_table.to_csv('pivot_table.csv')

"""
This pivot table aggregates the Quantity by calculating the mean for each Category and Date.
"""
# Another example of a pivot table with different aggregation
pivot_table_quantity = pd.pivot_table(df,
                                      values='Quantity',
                                      index='Category',
                                      columns='Date',
                                      aggfunc='mean',
                                      fill_value=0)

print("\nPivot Table with Quantity (Mean):")
print(pivot_table_quantity)

pivot_table_quantity.to_csv('pivot_table_quantity.csv')
