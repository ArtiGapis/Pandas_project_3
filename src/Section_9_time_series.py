'''----------Section: 9 Time Series----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd
import matplotlib.pyplot as plt


'''Step 2. Import the dataset from this 
    https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'''

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv"

'''Step 3. Assign it to a variable apple'''

apple = pd.read_csv(url)
# print(apple.head())

'''Step 4. Check out the type of the columns'''

# print(apple.dtypes)

'''Step 5. Transform the Date column as a datetime type'''

apple['Date'] = pd.to_datetime(apple['Date'])

'''Step 6. Set the date as the index'''

apple = apple.set_index('Date')

'''Step 7. Is there any duplicate dates?'''

duplicates = apple.index.duplicated()
# print(duplicates.any())

'''Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.'''

apple = apple.sort_index(ascending=True)
# print(apple.head())

'''Step 9. Get the last business day of each month'''

last_business_day = apple.resample('BM').apply(lambda x: x.index.max())
# print(last_business_day)

'''Step 10. What is the difference in days between the first day and the oldest'''

difference = apple.index.max() - apple.index.min()
# print(difference.days)

'''Step 11. How many months in the data we have?'''

num_months = apple.resample('M').size().shape[0]
print(num_months)

'''Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches'''

plt.figure(figsize=(13.5, 9))
apple['Adj Close'].plot()
plt.show()
