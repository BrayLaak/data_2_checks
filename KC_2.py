'''Make a .py (or .ipynb) file that contains the following (your choice of editor does not matter!) and do the following:
find and access a data set in any way you want. You can use an API, a CSV, anything.
Fix TWO issues with the data set using techniques you've learned in class. Here are some common fixes:
    Remove null values
    Fill in null values with 0's or blanks
    fill in blanks
    fix character strings that aren't formatted correctly (you could use regex for this)
    correct column names if they're misnamed
    correct spelling (for example, you might have a Country column with an entry that says "Unted States of America".)
Commit your changes.
Push your changes to GitHub, and make sure to turn in the GitHub link into Google Classroom.'''

import pandas as pd

# pull in data from KC_2_Data.csv
df = pd.read_csv('KC_2_Data.csv')

# Remove "'Unnamed: 0'" column
df = df.drop(columns=['Unnamed: 0'])

# Remove null values
df = df.dropna()

# Ensure that the data types are correct
df['DocumentID'] = df['DocumentID'].astype('int64')
df['Date'] = df['Date'].astype('datetime64[ns]')
df['SKU'] = df['SKU'].astype('int64')
df['Price'] = df['Price'].astype('float64')
df['Discount'] = df['Discount'].astype('int64')
df['Customer'] = df['Customer'].astype('int64')
df['Quantity'] = df['Quantity'].astype('float64')


# print the first 5 rows of the data frame
print(df.head())

# print the last 5 rows of the data frame
print(df.tail())

