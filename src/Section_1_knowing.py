'''----------Section 1: Getting and knowing your data----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd

'''Step 2. Import the dataset from this address.'''
'''Step 3. Assign it to a variable called users and use the 'user_id' as index'''

url_1 = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
df = pd.read_csv(url_1, sep='|', index_col='user_id')

'''Step 4. See the first 25 entries'''
# print(df.head(25))

'''Step 5. See the last 10 entries'''
# print(df.tail(10))

'''Step 6. What is the number of observations in the dataset?'''
# print(df.shape[0])

'''Step 7. What is the number of columns in the dataset?'''
# print(df.shape[1])

'''Step 8. Print the name of all the columns.'''
# print(df.columns)

'''Step 9. How is the dataset indexed?'''
# print(df.index)

'''Step 10. What is the data type of each column?'''
# print(df.dtypes)

'''Step 11. Print only the occupation column'''
# print(df['occupation'])

'''Step 12. How many different occupations are in this dataset?'''
# print(df['occupation'].nunique())

'''Step 13. What is the most frequent occupation?'''
# print(df['occupation'].value_counts().head(1))

'''Step 14. Summarize the DataFrame.'''
# print(df.describe())

'''Step 15. Summarize all the columns'''
# print(df.info())

'''Step 16. Summarize only the occupation column'''
# print(df['occupation'].value_counts())

'''Step 17. What is the mean age of users?'''
# print(df['age'].mean())

'''Step 18. What is the age with least occurrence?'''
# print(df['age'].value_counts().tail(1))
