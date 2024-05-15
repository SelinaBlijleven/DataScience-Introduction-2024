"""
knmi_example.py

Read and compare weather data for two different stations
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Filenames
path = os.getcwd() + "/data/"
filename1 = path + "etmgeg_260.txt"
filename2 = path + "etmgeg_279.txt"
columns_of_interest = ['STN','YYYYMMDD','TG','TN','TX']

# Get the column names
names = "STN,YYYYMMDD,DDVEC,FHVEC,   FG,  FHX, FHXH,  FHN, FHNH,  FXX,\
FXXH,   TG,   TN,  TNH,   TX,  TXH, T10N,T10NH,   SQ,   SP,    Q,   DR,   RH,  RHX,\
RHXH,   PG,   PX,  PXH,   PN,  PNH,  VVN, VVNH,  VVX, VVXH,   NG,   UG,   UX,  UXH,\
UN,  UNH, EV24"
columns = names.replace(' ', '').split(',')

# Read the files
bilt = pd.read_csv(filename1, skiprows=53, header=None, names=columns, na_values="     ")
hoogeveen = pd.read_csv(filename2, skiprows=53, header=None, names=columns, na_values="     ")

# Stick the entries together
df = pd.concat([bilt, hoogeveen])

# Set temperature to celsius (currenlty 0.1 celcius)
df[['TG','TN','TX']] = 0.1 * df[['TG','TN','TX']]

# Add the human-readable date column
df['Datum'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Use a subselection of the data: only the last 100 measurements
df = df.sort_values(by="Datum", ascending=False).iloc[:100]

# Add the human-readable station column
df['Station'] = df['STN'].map(
    {
        260: 'De Bilt',
        279: 'Hoogeveen'
    }
)

# Set the index to the date and station
df.set_index(['Datum', 'Station'])

# Unstack the data
df_unstacked = df.set_index(['Datum', 'Station'])[['TG','TN','TX']].unstack()

# Drop everything we cannot compare
df_unstacked.dropna(inplace=True)

# Plot the temperatures
plt.figure(figsize=(10, 6))
plt.plot(df_unstacked.index, df_unstacked[('TG', 'De Bilt')], label='De Bilt')
plt.plot(df_unstacked.index, df_unstacked[('TG', 'Hoogeveen')], label='Hoogeveen')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Means etc. of the columns
print(df_unstacked.describe())

# Boxplots
# Extract the data for boxplot
data = [df_unstacked[('TG', 'De Bilt')], df_unstacked[('TG', 'Hoogeveen')]]
labels = ['De Bilt', 'Hoogeveen']

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=labels)
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_unstacked.index, df_unstacked[('TG', 'De Bilt')], label='De Bilt', alpha=0.5)
plt.scatter(df_unstacked.index, df_unstacked[('TG', 'Hoogeveen')], label='Hoogeveen', alpha=0.5)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()

# Difference dataframe
diff = df_unstacked[('TG', 'Hoogeveen')] - df_unstacked[('TG', 'De Bilt')]

plt.figure(figsize=(10, 6))
plt.hist(df_unstacked[('TG', 'De Bilt')], bins=30, alpha=0.5, label='De Bilt')
plt.hist(df_unstacked[('TG', 'Hoogeveen')], bins=30, alpha=0.5, label='Hoogeveen')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.title('Temperature Distribution')
plt.legend()
plt.grid(True)
plt.show()

# Assuming 'diff' is a defined series or array
plt.figure(figsize=(10, 6))
plt.plot(diff)
plt.axhline(0, color='red', linewidth=1)
plt.xlabel('Index')  # Customize as necessary, e.g., 'Date' or other x-axis label
plt.ylabel('Difference')  # Customize as necessary based on the context of 'diff'
plt.title('Plot of Differences')
plt.grid(True)
plt.show()

print(f"There were {np.sum(diff < 0)} days when it was colder in Hoogeveen than de Bilt.")
