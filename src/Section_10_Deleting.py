'''----------Section 10: Deleting----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd
import numpy as np

'''Step 2. Import the dataset from this doc/wine.data'''
'''Step 3. Assign it to a variable called wine'''
wine = pd.read_csv("../doc/wine.data", header=None)
# print(wine)

'''Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns'''
wine = wine.drop([0, 3, 6, 8, 10, 12, 13], axis=1)
# print(wine.head())

'''Step 5. Assign the columns as below:'''

wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
# print(wine.head())

'''Step 6. Set the values of the first 3 rows from alcohol as NaN'''

wine.loc[0:2, 'alcohol'] = pd.np.nan
# print(wine.head())

'''Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN'''

wine.loc[3:4, 'magnesium'] = np.nan
# print(wine['magnesium'].head())

'''Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium'''

wine['alcohol'].fillna(10, inplace=True)
wine['magnesium'].fillna(100, inplace=True)
# print(wine[['alcohol','magnesium']].head())
# print(wine)

'''Step 9. Count the number of missing values'''

num_missing_1 = wine.isna().sum().sum()
# print("Missing values:", num_missing_1)

'''Step 10. Create an array of 10 random numbers up until 10'''

random_array = np.random.randint(0, 10, size=10)
# print(random_array)

'''Step 11. Use random numbers you generated as an index and assign NaN value to each of cell.'''

wine.loc[random_array] = np.nan
# print(wine)

'''Step 12. How many missing values do we have?'''

num_missing_2 = wine.isna().sum().sum()
# print("Missing values:", num_missing_2)

'''Step 13. Delete the rows that contain missing values'''

wine.dropna(axis=0, inplace=True)

'''Step 14. Print only the non-null values in alcohol'''

# print(wine[wine['alcohol'].notnull()]['alcohol'])

'''Step 15. Reset the index, so it starts with 0 again'''

wine.reset_index(drop=True, inplace=True)
