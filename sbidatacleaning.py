import pandas as pd

# 1. Data Loading and Inspection:
#  Load the dataset from an Excel file.
#  Perform initial inspection of the data.

df = pd.read_excel("C:\\Users\\Admin\\Desktop\\Urvashi\\Data Science Notes\\Classes\\SBIN_Data_XL.xlsx",
                   sheet_name='Sheet1', usecols='A:G', nrows=8251)

# 2. Data Cleaning:
#  Ensure the data types are correct for each column.
#  Handle any missing or duplicate values.

# print(df.duplicated())
df.drop_duplicates()
df.fillna(0)
df['Date'] = pd.to_datetime(df['Date'])

# 3. Data Transformation:
# Add new calculated columns:
# 1. Price Change: Difference between the Close and Open prices.
# 2. Intraday Range: Difference between the High and Low prices.

df['Price Change'] = abs(df['Close'] - df['Open'])
df['Intraday Range'] = abs(df['High'] - df['Low'])

# 4. Data Analysis:
# 1. Perform basic analysis using the new columns.
# 2. Calculate the time periods with the highest and lowest Price Change.
# 3. Calculate the average Intraday Range and identify patterns.

print('Average Price Change is =>', df['Price Change'].mean())
price_change_highest = df['Price Change'].max()
price_change_lowest = df['Price Change'].min()
print('Highest Price Change =>', price_change_highest)
print('Lowest Price Change =>', price_change_lowest)

for index, row in df.iterrows():
    if row['Price Change'] == price_change_highest:
        print('Time period with highest price change is ', row['Time'])

    if row['Price Change'] == price_change_lowest:
        print('Time period with lowest price change is ', row['Time'])


avg_intraday_range = df['Intraday Range'].mean()


df.to_excel("C:\\Users\\Admin\\Desktop\\Urvashi\\Data Science Notes\\Classes\\SBIN_Data_XL.xlsx", index=False)
