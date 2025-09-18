import pandas as pd
import matplotlib.pyplot as plt
import io
import re


# 1. Load the dataset
# We use io.StringIO to treat the string as a file
df = pd.read_csv(io.StringIO(water_csv_content))

# 2. Clean the data
# Replace special characters with NaN and then convert to numeric
df.replace(to_replace=[r'^<', r'^>'], value='', regex=True, inplace=True)
df.replace(to_replace=[r'^-', r'^$'], value='0', regex=True, inplace=True)
for col in df.columns:
    if col not in ['country', 'region']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop any remaining rows with missing data
df.dropna(inplace=True)

# 3. Perform basic data analysis
print("Statistical Summary of Water Access Data:")
print(df.describe())

# 4. Create a line chart to visualize a trend
# Plot the trend of 'total_basic' water access over the years
plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['total_basic'], marker='o')
plt.title('Trend of Basic Water Access in Afghanistan')
plt.xlabel('Year')
plt.ylabel('Percentage of Population with Basic Access (%)')
plt.grid(True)
plt.show()
