'''----------Section 4: Apply----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd

'''Step 2. Import the dataset from this address.'''
url_4 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'

'''Step 3. Assign it to a variable called crime.'''
crime = pd.read_csv(url_4)
# print(crime)

'''Step 4. What is the type of the columns?'''
# print(crime.dtypes)

'''Step 5. Convert the type of the column Year to datetime64'''
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
# print(crime.dtypes)

'''Step 6. Set the Year column as the index of the dataframe'''
crime = crime.set_index('Year')
# print(crime.head())

'''Step 7. Delete the Total column'''
crime = crime.drop('Total', axis=1)
# print(crime.columns)

'''Step 8. Group the year by decades and sum the values'''
cdd = crime.resample('10AS').sum()

'''Step 9. What is the most dangerous decade to live in the US?'''
cdd['Total'] = cdd['Violent'] + cdd['Property']
most_dangerous_decade = cdd['Total'].idxmax().year